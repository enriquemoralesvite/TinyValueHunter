def SearchMinFromList(L):
    # Initialize minValue with the first element of the list
    minValue = L[0]  
    counter = 0  #Start from the first index
    position = 0 # Track the position of the minimum value
    # Iterate over the list starting from the first element
    while counter < len(L):
        if L[counter] < minValue:
            minValue = L[counter]
            position = counter + 1
        counter += 1  # Move to the next element
    sortedList = sorted(L)
    return minValue, position, sortedList

# Example usage:
L = [23, -4, 0, 73, -10, 13]
minValue, position, sortedList = SearchMinFromList(L)
print("The minimum value is:", minValue, "is located in the position",position)
print ("The sorted list is:", sortedList)
