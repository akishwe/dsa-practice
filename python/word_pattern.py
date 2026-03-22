def word_pattern(pattern,string):
    # Split the string into words
    words = string.split()

    # Check if the number of words matches the length of the pattern
    if len(words) != len(pattern):
        return False
    
    # Create a dictionary to map pattern characters to words
    char_to_word = {}
    used_words = set()

    for char, word in zip(pattern, words):
        if char in char_to_word:
            # If the character is already mapped to a word, check if it matches the current word
            if char_to_word[char] != word:
                return False
            else:
                # If the character is not mapped to a word, check if the current word is already used by another character
                if word in used_words:
                    return False
                # Map the character to the current word and add the word to the set of used words
                char_to_word[char] = word
                used_words.add(word)
    return True


# Example usage:
print(word_pattern("abba", "dog cat cat dog"))  # True
print(word_pattern("abba", "dog cat cat fish"))  # False
            