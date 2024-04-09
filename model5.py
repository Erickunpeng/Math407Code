import numpy as np
from scipy.optimize import linprog

# Objective function coefficients (Maximize Profit)
# For maximization problems, you need to multiply the coefficients by -1
# because linprog is designed to minimize the objective function.
c = [-1.50 * 0.97 + 0.68, -1.00 * 0.97 + 0.27, -1.00 * 0.97 + 0.31, -1.00 * 0.97 + 0.45]

# Inequality constraints matrix (A_ub for 'upper bound')
# We multiply by -1 for >= constraints to convert them to <= as required by linprog
A_ub = [
    [-0.45, -0.07, -0.12, -0.27],  # Protein constraint (>= 22%, converted to <=)
    [0.12, 0.38, 0.25, 0.40],      # Starch content <= 30% (no need to multiply by -1)
]

# Inequality constraint vector (b_ub for 'upper bound')
b_ub = [
    -22,  # Protein minimum requirement
    30,   # Starch maximum requirement
]

# Bounds for each variable (ensuring non-negativity and availability)
x_bounds = [(0, 1500), (0, 500), (0, 1000), (0, 2000)]

# Solve the problem
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=x_bounds, method='highs')

# Display the results
if result.success:
    print(f"Optimal amounts (kg) of food types to use: {result.x}")
    print(f"Maximum profit: ${-1 * result.fun}")  # Multiply by -1 to convert back to a maximization result
else:
    print("No solution found.")
