def longest_word(string):
    words = string.split()
    # Declare a variable to keep track of the longest word found
    longest = ""

    # Iterate through each word in the list
    for word in words:
        # Check if the length of the current word is greater than the length of the longest word found so far
        if len(word) > len(longest):
            # If it is  return the current word as the longest word
            longest = word

    return longest

# Example usage:
text = "The quick brown fox jumps over the lazy dog"
print(longest_word(text)) 