def second_largest_element(array):
    # Edge case : if the array has less than 2 elements
    if len(array) < 2:
        return -1  # Not enough elements for second largest
    # Initialize the largest and second largest variables
    largest = array[0]
    second_largest = array[1]

    # Ensure largest is greater than second largest
    if array[0] < array[1]:
        largest = array[1]
        second_largest = array[0]
    else:
        largest = array[0]
        second_largest = array[1]

    # Traverse the array starting from the third element
    for i in range(2, len(array)):
        # If the current element is greater than the largest
        # update second largest first and then largest
        if array[i] >  largest:
            second_largest = largest
            largest = array[i]
        # If the current element is smaller than the largest
        # but greater than the second largest update the second largest
        elif array[i] > second_largest and array[i] != largest:
            second_largest = array[i]
    #Return the second largest element
    return second_largest

array = [12, 35, 1, 10, 34, 1]
result = second_largest_element(array)
print(result)