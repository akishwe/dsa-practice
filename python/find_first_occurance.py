def find_first_occurrence(haystack, needle):

    if not needle:
        return 0
    # Save the length of the haystack
    haystack_length = len(haystack)
    # Save the length of the needle 
    needle_length = len(needle)

    # Loop through the haystack 
    for i in range(haystack_length - needle_length +1):
        # Check if the sub string from the haystack matches the needle
        if haystack[i:i+ needle_length] == needle:
            return i

    return -1

haystack = "sadbutsad"
needle = "sad"
print(find_first_occurrence(haystack, needle))