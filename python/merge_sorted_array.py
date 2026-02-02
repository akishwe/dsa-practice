def merge_sorted_array(first_list,first_count,second_list,second_count):

     # Start from the last valid element in first_list
    first_index = first_count - 1

    # Start from the last element in second_list
    second_index = second_count - 1

    # Start filling from the end of first_list
    fill_position = first_count + second_count - 1

    # Merge both lists starting from the end
    while first_index >= 0 and second_index >= 0:
        # Compare elements from the end of both lists
        if first_list[first_index] > second_list[second_index]:
            # Place the larger element at the current fill position
            first_list[fill_position] = first_list[first_index]
            first_index -= 1
        else:
            first_list[fill_position] = second_list[second_index]
            second_index -= 1

        fill_position -= 1  # Move the fill position to the left

    # If any elements remain in second_list, copy them over
    # (No need to copy first_list elements—they are already in place)
    while second_index >= 0:
        first_list[fill_position] = second_list[second_index]
        second_index -= 1
        fill_position -= 1

    return first_list

first_list = [1, 2, 3, 0, 0, 0]
second_list = [2, 5, 6]

result = merge_sorted_array(first_list, 3, second_list, 3)

print(result)

