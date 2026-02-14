def fibonacci_up_to_n_terms(n):
    # Return empty list if n is less than or equal to 0
    if n <= 0:
        return []
    # Return 0 if only the first term is requested
    elif n == 1:
        return [0]
    
    # Initialize the Fibonacci sequence with the first two terms
    fib_sequence = [0,1]

    # Generate the remaining terms until we reach n terms
    for i in range(2, n):
        # Calculate the next term by summing the last two terms in the sequence
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        # Append the next term to the Fibonacci sequence
        fib_sequence.append(next_term)

    return fib_sequence


# Example usage:
n = 10
print(f"Fibonacci sequence up to {n} terms: {fibonacci_up_to_n_terms(n)}")
