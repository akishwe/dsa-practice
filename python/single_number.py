def single_number(nums):
    result =0

    for num in nums:
        result ^= num
    return result

nums = [2,2,1]
result = single_number(nums)
print(result)