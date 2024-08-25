def merge_sort(array):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(array) <= 1:
        return
    
    # Find the middle point to split the array into two halves
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Recursively sort both halves
    merge_sort(left_part)
    merge_sort(right_part)

    # Initialize indices for left part, right part, and the merged array
    left_arr_index = 0
    right_arr_index = 0
    sorted_index = 0

    # Merge the two halves together while both halves have elements
    while left_arr_index < len(left_part) and right_arr_index < len(right_part):
        # Compare the current elements of both halves
        if left_part[left_arr_index] < right_part[right_arr_index]:
            # If the current element in the left half is smaller, place it in the sorted array
            array[sorted_index] = left_part[left_arr_index]
            # Move to the next element in the left half
            left_arr_index += 1
        else:
            # If the current element in the right half is smaller or equal, place it in the sorted array
            array[sorted_index] = right_part[right_arr_index]
            # Move to the next element in the right half
            right_arr_index += 1
        
        # Move to the next position in the sorted array
        sorted_index += 1

    # Copy any remaining elements from the left part, if any
    while left_arr_index < len(left_part):
        array[sorted_index] = left_part[left_arr_index]
        left_arr_index += 1
        sorted_index += 1

    # Copy any remaining elements from the right part, if any
    while right_arr_index < len(right_part):
        array[sorted_index] = right_part[right_arr_index]
        right_arr_index += 1
        sorted_index += 1

# Test the merge_sort function
if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array:')
    print(numbers)
