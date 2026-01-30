def plus_one(digits):

    # Start checking digits from the right side
    # because addition starts from the right side
    for i in range(len(digits) -1 , -1,-1):

        # Check if the current digit is less than 9
        # Because if its less than 9, adding 1 will not cause a carry
        if digits[i] < 9:
            digits[i] += 1
            return digits
        
        # If digit is 9 we cannot store 10 in one place
        # So we store 0 and carry 1 to the left
        digits[i] = 0

    # If we finish the whole loop this means the whole loop has 999 than 
    # So we need to add 1 at the front
    return [1] + digits
