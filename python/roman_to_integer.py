def roman_to_integer(string):
    # Dictionary to map Roman numerals to their integer values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # This will store the final integer value
    total = 0
    # This will keep track of of previous numeral value (right side)
    prev_value = 0

    # Iterate over the string in reverse order
    for char in reversed(string):

        # Validate the character is a valid Roman numeral
        if char not in roman_map:
            raise ValueError(f"Invalid Roman numeral character: {char}")
        
        # Get the integer value of the current Roman numeral
        current_value = roman_map[char]

        # Determine weather to add or subtract the current value
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        # Update previous value for  next iteration
        prev_value = current_value

    # Return the final computed integer value
    return total

# Example usage:
roman_numeral = "MCMXCIV"
integer_value = roman_to_integer(roman_numeral)
print(f"The integer value of the Roman numeral {roman_numeral} is {integer_value}.")