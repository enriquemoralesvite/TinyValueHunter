def SearchMinFromList(L):
    # Initialize minValue with the second element of the list
    minValue = L[0]  # L[1] because the pseudocode starts with index 1
    counter = 0  # Start from the second index (3rd element)
    
    # Iterate over the list starting from the second element (index 2)
    while counter < len(L):
        L[counter]
        if L[counter] < minValue:
            minValue = L[counter]
        counter += 1  # Move to the next element
    
    return minValue

# Example usage:
L = [23, -4, 0, 73, -10, 13]
result = SearchMinFromList(L)
print("The minimum value is:", result)
