import numpy as np
from time import time 

# calc f prime
def polynomial_derivative(poly):
    n = len(poly)
    # If the polynomial is a constant (n=1), the derivative is 0
    if n == 1:
        return [0]
    
    # Calculate the derivative coefficients
    derivative_coeffs = [(n - i - 1) * poly[i] for i in range(n - 1)]
    
    return derivative_coeffs


# f(x0)
def f_value_in_point_x(poly, x):
    result = 0
    for coefficient in poly:
        result = result * x + coefficient
    return result 


# newton function
def newton_method(x0, f, f_prime, tol=1e-5, epsilon=1e-6, max_iterations=100):

    for _ in range(max_iterations):
        y = f_value_in_point_x(f, x0)
        yprime = f_value_in_point_x(f_prime, x0)

        if abs(yprime) < epsilon:
            break

        x1 = x0 - y / yprime

        if abs(x1 - x0) <= tol:
            return x1

        x0 = x1

    return None   
    
        
# bisection function
def bisection(f, a, b, tol=1e-5):
    fa = f_value_in_point_x(f, a)
    fb = f_value_in_point_x(f, b)
    
    if fa * fb > 0:
        return None
    
    while np.abs(a-b) > tol:
        c = (a + b) / 2
        fc = f_value_in_point_x(f, c)
        
        if fa * fc <= 0:
            b = c
        else:
            a = c
            
    return (a + b) / 2
    

# Calculate the bound for the roots of the polynomial
def calc_bound_interval(f):
    a_n = abs(f[0])
    sum_abs_coeffs = sum(abs(coef) for coef in f[1:])
    return max(1, sum_abs_coeffs / a_n)
    

# Recursive function to find all roots of the polynomial
def find_roots(f):
    # base case: Linear: ax + b = 0
    if (len(f) == 2):
        return [-f[1] / f[0]]
    
    # Edge case for trivial polynomials
    if len(f) <= 1:
        return []
    
    f_prime = polynomial_derivative(f)
    intervals = find_roots(f_prime)
    
    bound_interval = calc_bound_interval(f)
    intervals = [-bound_interval] + intervals + [bound_interval]
    
    roots = []
    for i in range (len(intervals)-1):
        a = intervals[i]
        b = intervals[i+1]

        if f_value_in_point_x(f, a) * f_value_in_point_x(f, b) <= 0:
            initial_point = (a + b) / 2
        
            # Find root in the interval [a, b]
            root = newton_method(initial_point, f, f_prime)
            if (root is None):
                root = bisection(f, a, b)
                
            if (root is not None):
                roots.append(root)

    # Sort roots
    roots = sorted(roots)

    return roots
        

def read_polynomial_from_file(filename):
    coefficients = []

    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read each line in the file
            for line in file:
                # Strip any leading/trailing whitespace and convert to float
                coefficient = float(line.strip())
                coefficients.append(coefficient)

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except ValueError:
        print("Error: The file contains non-numeric values.")
        return None

    return coefficients

# Main
filename = 'Python/poly_coeff(997).txt'
poly = read_polynomial_from_file(filename)

# Measure execution time for find_roots function
print("\nOur Solution:")
tt = time()
result_1 = find_roots(poly)
print("Time:", time() - tt)
print("The roots of the polynomial are:", result_1)

# Measure execution time for numpy function
print("\nNumpy Solution:")
tt = time()
result_2 = np.roots(poly)
print("Time:", time() - tt)
real_roots = result_2[np.isreal(result_2)]
print("The roots of the polynomial are:", real_roots)