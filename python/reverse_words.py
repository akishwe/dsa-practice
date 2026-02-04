def reverse_words(string):
    words = string.split()
    words.reverse()
    return " " .join(words)