def search_insert_position(nums, target):
    # Initialize the left pointer at the start of the array
    left = 0
    # Initialize the right pointer at the end of the array
    right = len(nums) -1

    # Continue searching while the search space is valid
    while left <= right:
        # Calculate the middle index of the current search space
        mid = left + (right - left) // 2

        # If the target is found at mid return immediately
        if nums[mid] == target:
            return mid
        # If the target is greater than nums[mid] , ignore left half including mid 
        elif nums[mid] < target:
            left = mid + 1
        # If target is smaller than nums[mid], ignore the right half including the mid
        else:
            right = mid - 1

    return left