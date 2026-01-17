def count_even_odd_numbers(array):

    # Variable to keep track of even numbers are found so far
    even_count = 0
    # Variable to keep track of odd numbers are found so far
    odd_count = 0

    # Iterate through each number in the array
    for num in array:
        # Check if the current number is divisible by 2
        if num % 2 == 0:
            # Id its even, increment the even count
            even_count += 1
        else:
            # If its not even, it must be odd, increment the odd count
            odd_count += 1

    # Return the counts of even and odd numbers
    return even_count, odd_count


# Example usage:
array = [10, 21, 32, 43, 54, 65, 76]
even_count, odd_count = count_even_odd_numbers(array)
print("Even number count:", even_count)
print("Odd number count:", odd_count)
