def binarySearch(paraList, targetValue):
    """
    Searches for a target value in a sorted list using binary search.

    Args:
        paraList (list): A sorted list of integers.
        targetValue (int): The value to search for in the list.

    Returns:
        bool: True if the target value is found in the list, False otherwise.

    Example:
        >>> binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
        True
        >>> binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
        False
    """
    size = len(paraList)
    if(len(paraList) == 0):   
        return False   # Return False if the list is empty
    midValue = paraList[int(size/2)]
    subList = list()  # Initialize an empty sublist

    if(midValue == targetValue):
        return True  # Value found
    
    if(midValue > targetValue):
        if(size == 1):
            subList = []
        subList = paraList[:int(size/2)]
        # Recursively search in the left half
        if(binarySearch(subList, targetValue)):
            return True
        else:
            return False

    elif(midValue < targetValue):
        # If the mid value is less than the target
        if(size == 1):
            subList = []
        subList = paraList[int(size/2):]
        # Recursively search in the right half
        if(binarySearch(subList, targetValue)):
            return True
        else:
            return False


listLength = int(input("Enter number of list items: "))
sampleList = list()
for i in range(listLength):
    print("Enter list item: ", end='')
    entry = int(input())
    sampleList.append(entry)
    

target = int(input("Enter item to search for: "))
found = binarySearch(sampleList, target)

if(found):
    print(f"{target} found within list.\n")
else:
    print(f"{target} not found within list.\n")



