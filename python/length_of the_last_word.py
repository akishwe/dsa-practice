def length_of_the_last_word(sentence):
    last_word_length = 0
    index = len(sentence) - 1
    
    # Skip trailing spaces
    while index >= 0 and sentence[index] == ' ':
        index -= 1

    # Count characters of last word
    while index >= 0 and sentence[index] != ' ':
        last_word_length += 1
        index -= 1

    return last_word_length


# Example sentence
sentence = "Hello World from Python   "

# Function call
result = length_of_the_last_word(sentence)

print("Length of last word:", result)
