def move_zeroes(nums):
 non_zero = [x for x in nums if x !=0]
 zero = [x for x in nums if x == 0]
 return non_zero + zero
 
 
nums = [0,1,0,3,12]
print(move_zeroes(nums))