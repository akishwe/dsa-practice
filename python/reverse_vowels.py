def reverse_vowels(string):
    # Create a set of vowels for quick lookup
    vowels = set('aeiouAEIOU')
    # Convert the string to a list to allow for reversal of characters
    string = list(string)

    # Create two pointers to track the left and right ends of the string
    left = 0
    right = len(string) -1

    # Loop until the left pointer is less than the right pointer
    while left < right:
        # If the character at the left pointer is not a vowel move the left pointer to the right
        if string[left] not in vowels:
            left += 1
        # If the character at the right pointer is not a vowel move the right pointer to the left
        elif string[right] not in vowels:
            right -= 1
        else:
            # Swap the characters at the left and right pointers and move both pointers towards the center
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1
    # Join the list back into a string and return it
    return ''.join(string)

# Example usage:
print(reverse_vowels("hello"))  # "holle"
print(reverse_vowels("leetcode"))  # "leotcede"