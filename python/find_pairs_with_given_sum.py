def find_pairs(arr,k):
    # Declare the list to store pairs
    pairs = []
    # Get total number of elements in the array
    n = len(arr)

    # Loop through the first element and this iteration will be fixed for the inner loop
    for i in range(n):
        # Loop through the next element from first element
        for j in range(i+1,n):
            # Check if the iterations are equal to the target
            if arr[i] + arr[j] == k:
                # Append it to the pairs list
                pairs.append(arr[i],arr[j])
    
    return pairs

# Example
arr = [1, 5, 7, -1, 5]
k = 6

print(find_pairs(arr,k))


