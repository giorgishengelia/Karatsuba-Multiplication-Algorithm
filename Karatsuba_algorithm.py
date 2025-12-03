# Karatsuba Multiplication Algorithm 

def karatsuba(x, y):
    # Base case: if numbers are small, use standard multiplication
    if x < 10 or y < 10:
        return x * y

    # Determine the number of digits in the larger number
    n = max(len(str(x)), len(str(y)))
    
    # Split point for dividing the numbers
    m = n // 2

    # Divide x and y into two halves
    # x = x_high * 10^m + x_low
    # y = y_high * 10^m + y_low
    x_high = x // (10 ** m)
    x_low = x % (10 ** m)
    y_high = y // (10 ** m)
    y_low = y % (10 ** m)

    # Recursively calculate the three products
    p1 = karatsuba(x_high, y_high)  # x_high * y_high
    p2 = karatsuba(x_low, y_low)    # x_low * y_low
    p3 = karatsuba(x_high + x_low, y_high + y_low) # (x_high + x_low) * (y_high + y_low)

    # Combine the results using the Karatsuba formula
    # x * y = p1 * 10^(2m) + (p3 - p1 - p2) * 10^m + p2
    return p1 * (10 ** (2 * m)) + (p3 - p1 - p2) * (10 ** m) + p2

# Example usage:
num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627
result = karatsuba(num1, num2)
print(f"The product of {num1} and {num2} is: {result}")