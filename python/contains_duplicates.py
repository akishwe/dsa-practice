def contains_duplicates(nums):
    # Store the elements here 
    seen = set()
    # Loop through each element
    for num in nums:
        # If the element is in seen we found a duplicate
        if num in seen:
            return True
        
        # Add the num to the array
        seen.add(num)

    return False

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
result = contains_duplicates(nums)
print(result)
