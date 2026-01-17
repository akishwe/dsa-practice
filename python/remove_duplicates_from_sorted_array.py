def remove_duplicates(nums):

    # If the input array is empty,there are no elements to process.
    # So return 0 as the count of unique elements.
    if not nums:
        return 0
    # 'count' keeps track of the position to place the next unique element.
    # The first element is always unique in a sorted array.
    count = 1


    # Start iterating from the second element(Index 1) to the end of the array.
    # We compare each element with the previous one.
    for i in range(1, len(nums)):

        # If the current element is different from the previous one,
        # it means we have found a new unique element.
        if nums[i] != nums[i - 1]:
            # Place this unique element at the 'count' index.
            # This overwrites duplicates and keeps the array compact.
            nums[count] = nums[i]
            # Increment the 'count' of unique elements.
            # where a unique element should be placed next.
            count += 1

    # 'count' now represents the number of unique elements in the array.
    # The first 'count' elements of 'nums' are the unique elements.
    return count
    

# Example usage:
nums = [0,0,1,1,1,2,2,3,3,4]
result = remove_duplicates(nums)
print("Length after removing duplicates:", result)
print("Array after removing duplicates:", nums[:result])