def longest_substring(s: str):
    # Dictionary to store the last seen index of each character
    # Key character, Value last index
    last_seen = {}
    
    # starting index of the current substring
    start = 0
    # Maximum length of the substring found
    max_len = 0
    # Longest substring found so far
    longest_substring = ""
    
    # Iterate through each character in the substring
    for end, char in enumerate(s):
        # If the character is already in the dictionary and its last seen index is within the current substring
        # is inside the current substring is a duplicate
        if char in last_seen and last_seen[char] >= start:
            # Update the starting index to the index after the last seen index of the duplicate character
            start = last_seen[char] + 1
        # Update the last seen index of the character to the current index
        last_seen[char] = end
        
        # Check if the current window length is greater than the maximum length found so far
        current_length = end - start + 1
        if current_length > max_len:
            max_len = current_length
            longest_substring = s[start:end + 1]
            
    return longest_substring


input_string = "abcabcbb"
result = longest_substring(input_string)
print(f"The longest substring without repeating characters in '{input_string}' is '{result}'")
