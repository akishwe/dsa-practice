def find_max(array):
    # Assign the first element as the initial maximum
    max_value = array[0]

    # Iterate through each element in the array
    for num in array:
        # Check if the current element is greater than the current maximum
        if num > max_value:
            # If it is, update the maximum value
            max_value = num
    # After the loop, return the maximum value found
    return max_value

numbers = [3, 5, 1, 9, 2]


result = find_max(numbers)
print("The maximum value is:", result) 