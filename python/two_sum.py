def two_sum(nums, target):
    # This dictionary will store the numbers we have seen so for
    #Example: if nums = [2, 7, 11, 15] and target = 9
    seen = {}

    # Go through each number one by one
    for i, num in enumerate(nums):
    #Figure out what number you will need to reach the target
    # For example, if the current number is 2 and the target is 9,
    # the complement will be 7
        complement = target - num
    # Check if the complement number is already in the seen dictionary
        if complement in seen:
            # If it is, return the indices of the two numbers
            return (seen[complement], i)
        # If not, add the current number to the seen dictionary
        seen[num] = i
        # If no solution is found, return an empty list
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)