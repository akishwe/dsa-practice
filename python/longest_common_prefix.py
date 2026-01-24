def longest_common_prefix(strs):

    if not strs:
        return ""
    
    # Start with the first string as the prefix
    prefix = strs[0]

    for s in strs[1:]:

    # Shrink the prefix until it matches the start of the string s
        while not s.startswith(prefix):
            prefix = prefix[:-1]

            # If the prefix is reduced to an empty string, there is no common prefix
            if not prefix:
                return ""
    return prefix

strs = ["flower", "flow", "flight"]
result = longest_common_prefix(strs)
print(f"The longest common prefix is: '{result}'")
