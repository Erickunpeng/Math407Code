from scipy.optimize import minimize

# Define the polynomial function
def polynomial(t, a, b, c):
    return t**3 + a*t**2 + b*t + c

# Objective function to maximize f(3)
def objective(x):
    a, b, c = x
    return -polynomial(3, a, b, c)  # negative because we are using minimize

# Constraints for values at t = 0, 1, 2 within [-1, 1]
def constraint1(x):
    a, b, c = x
    return 1 - abs(polynomial(0, a, b, c))

def constraint2(x):
    a, b, c = x
    return 1 - abs(polynomial(1, a, b, c))

def constraint3(x):
    a, b, c = x
    return 1 - abs(polynomial(2, a, b, c))

# Initial guesses for a, b, c
x0 = [0, 0, 0]

# Define constraints dictionary
cons = [{'type': 'ineq', 'fun': constraint1},
        {'type': 'ineq', 'fun': constraint2},
        {'type': 'ineq', 'fun': constraint3}]

# Use 'SLSQP' optimization method with bounds
result = minimize(objective, x0, method='SLSQP', constraints=cons, bounds=[(-10, 10), (-10, 10), (-10, 10)])

a_opt, b_opt, c_opt = result.x

# Output the optimal parameters and maximum value at t = 3
print("Optimal parameters: a =", a_opt, "b =", b_opt, "c =", c_opt)
print("Maximum value at t=3:", -result.fun)
