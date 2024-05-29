import numpy as np
from scipy.optimize import linprog

# Coefficients of the objective function (note the negative sign for maximization)
c = [-9, 9, -3, 3, -1]

# Coefficients of the inequality constraints
A_ub = [[0, 0, 0, 0, 1],
        [1, -1, 1, -1, 1],
        [-1, 1, -1, 1, -1],
        [4, -4, 2, -2, 1],
        [-4, 4, -2, 2, -1],
        ]

# Right-hand side of the inequality constraints
b_ub = [2, 1, 1, -6, 8]

# Bounds for each variable
x_bounds = (0, None)  # Variables are non-negative

# Solving the LP using the 'highs' method
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[x_bounds, x_bounds, x_bounds, x_bounds, x_bounds], method='highs')

if result.success:
    print("Optimal value:", -result.fun)  # Negate the result to get the max value
    print("Optimal variables:", result.x)
else:
    print("Status:", result.message)
    if result.status == 3:  # Check if the problem is unbounded
        print("The problem is unbounded.")
    elif result.status == 2:  # Check if the problem is infeasible
        print("The problem is infeasible.")

