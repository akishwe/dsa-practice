def missing_number(nums):
    # Total elements in array 
    nums_length = len(nums)
    # Start with n because range n only goes up to n -1
    total = nums_length

    # Loop through from 0 to n-1
    for i in range(nums_length):
        # Add the expected number from the full range
        total += i
        # Subtract the actual number present in the array 
        total -= nums[i]

    return total

nums = [3, 0, 1]
result = missing_number(nums)

print("Missing number is:", result)