# Polynomial Root Finding Using Newton-Raphson and Bisection Method

This project implements an algorithm for finding all the roots of a polynomial using two numerical methods: **Newton-Raphson** and **Bisection Method**. It leverages the strengths of both methods to ensure efficiency and robustness when finding the zeros of real-valued polynomial functions. The algorithm is designed to handle polynomials of any degree, with coefficients provided as an input array.

## Methods

- **Newton-Raphson Method**: A fast, iterative method with quadratic convergence for roots when a good initial guess is available.
- **Bisection Method**: A robust bracketing method with guaranteed convergence, used when sign changes are detected over an interval.

## Solution Overview

1. **Read polynomial coefficients from a file.**
2. **Recursively find all roots:**
   - a. Compute the derivative of the given polynomial, using the power rule for derivatives.
   - b. Calculate an interval that likely contains all roots, using coefficients to estimate the bounds.
   - c. Find roots using Newton-Raphson method (faster).
   - d. If not found, find roots using Bisection method (slower).
3. **Sort the found roots.**
4. **Print the found roots and the execution time.**

## Usage

1. **Input**: Polynomial coefficients should be provided in a file.
2. **Output**: The program outputs the found roots and the execution time.
