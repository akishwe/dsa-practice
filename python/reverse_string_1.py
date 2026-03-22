def reverse_string(string):
    # Create a variable to hold the left pointer
    left = 0
    # Create a variable to hold the right pointer
    right = len(string) -1

    # Loop until the left pointer is less than the right pointer
    while left < right:
        # Swap the characters at the left and right pointers
        string[left], string[right] = string[right], string[left]
        # Move the left pointer to the right and the right pointer to the left
        left += 1
        right -= 1

    return string

# Example usage:
print(reverse_string(["h", "e", "l", "l", "o"]))  # ["o", "l", "l", "e", "h"]