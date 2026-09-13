def factorial_iterative(n):
    """Calculates factorial using an iterative loop."""
    # Time Complexity: O(n)  
    # Space Complexity: O(1)
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """Calculates factorial using recursion."""
    # Time Complexity: O(n) 
    # Space Complexity: O(n) 
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Example usage
if __name__ == "__main__":
    num = 5
    print(f"Iterative factorial of {num}: {factorial_iterative(num)}")
    print(f"Recursive factorial of {num}: {factorial_recursive(num)}")