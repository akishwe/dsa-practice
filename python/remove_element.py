def remove_element(nums, val):

    # Pointer k will keep track of the position of the next non-val element
    k = 0

    # Iterate through each element in the array
    for num in nums:

        # If the current element is not equal to val, we keep it
        if num != val:

            # Place it at the k-th position
            nums[k] = num

            # Move k to the next position
            k += 1

    return k
    
# Example usage
nums = [3, 2, 2, 3]
val = 3
new_length = remove_element(nums, val)
print(f"New length after removing {val} is: {new_length}")