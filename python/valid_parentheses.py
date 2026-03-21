def valid_parentheses(string):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or stack.pop() != bracket_map[char]:
                return False
    return not stack

# Example usage:
print(valid_parentheses("(){}[]"))  # True
print(valid_parentheses("([{}])"))  # True  
print(valid_parentheses("(]"))      # False