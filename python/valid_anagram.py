def valid_anagram(s: str, t: str) -> bool:

    # Check if the lengths of both strings are equal
    # If not, they cannot be anagrams
    if len(s) != len(t):
        return False
    
    # Create a dictionary to count the frequency of each character in the first string
    char_count = {}

    # Loop through each character in the first string 
    for char in s:
        # Increment the count for each character in the dictionary if it exists
        # Otherwise, initialize it to 1
        char_count[char] = char_count.get(char, 0) + 1

    # Loop through each character in the second string
    for char in t:
        # If the character is not found in the dictionary or its count is zero
        # It means the string are not anagrams
        if char not in char_count or char_count[char] == 0:
            return False
        # Decrement the count for each character in the dictionary
        char_count[char] -= 1
    return True

s = "anagram"
t = "nagaram"
result = valid_anagram(s,t)
print(result)