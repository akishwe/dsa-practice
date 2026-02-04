def check_palindrome_number(num):
    # Add a check to handle negative numbers and numbers ending with 0 (except 0 itself)
    if num < 0 or (num % 10 == 0 and num != 0):
        return False
    
    reversed_half = 0
    # reverse half of the number 
    while num > reversed_half:

        last_digit = num % 10
        reversed_half = reversed_half * 10 + last_digit
        num // 10
    # For even length numbers: x == reversed_half
    # For odd length numbers: x == reversed_half // 10
    return num == reversed_half or num == reversed_half // 10 
    