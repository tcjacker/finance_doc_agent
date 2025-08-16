def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.
    
    Args:
        arr: List of comparable elements
    
    Returns:
        List: Sorted array in ascending order
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize - if no swapping occurs, array is sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return arr


def bubble_sort_descending(arr):
    """
    Sorts an array in descending order using bubble sort.
    
    Args:
        arr: List of comparable elements
    
    Returns:
        List: Sorted array in descending order
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            # Swap if the element found is less than the next element
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr


# Example usage
if __name__ == "__main__":
    # Test the bubble sort function
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    
    sorted_array = bubble_sort(test_array.copy())
    print("Sorted array (ascending):", sorted_array)
    
    desc_sorted = bubble_sort_descending(test_array.copy())
    print("Sorted array (descending):", desc_sorted)