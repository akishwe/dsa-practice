def second_non_repeating_character(string):
    # Create a empty dictionary to store character frequencies
    freq = {}

    # Loop through each character in the string
    for char in string:

        # Check if the character already exists in the dictionary
        if char in freq:
            # If it exists increment its count by 1
            freq[char] = freq[char] + 1
        else:
            # If it does not exist, add it to the dictionary with count 1
            freq[char] = 1

    # Variable to count how many non repeating character have been found
    count = 0

    # Loop through the string again to maintain the order of each character 
    for char in string:
        # Check if the character's frequency is 1 (non-repeating)
        if freq[char] == 1:
            # Increment the non-repeating character count
            count += 1

            # If this is the second non-repeating character, return it
            if count == 2:
                return char

    return -1


# Example usage
string = "swiss"
result = second_non_repeating_character(string)
print(result)  
        
