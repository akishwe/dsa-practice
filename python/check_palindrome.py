def is_palindrome(string):
    # This pointer will start from the beginning of the string(first character)
    start = 0

    # This pointer will start from the end of the string (last character)
    # len(string) gives the total number of characters in the string
    # We subsctract 1 because indexing starts from 0
    end = len(string) - 1

    while start < end:

        # If characters at start and end pointers do not match
        if string[start] != string[end]:
            return False # Not a palindrome
        # Move start pointer to the right
        start += 1

        # Move end pointer to the left
        end -= 1

    # If we reach here, all characters matched
    return True

# Example usage
string = "madam"
if is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")