def bubble_sort(data):
    """
    Sorts a list in ascending order using the bubble sort algorithm.

    :param data: A list of comparable elements.
    :return: The sorted list.
    """
    n = len(data)
    # Traverse through all list elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

# Example usage:
if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Unsorted list: {sample_list}")
    sorted_list = bubble_sort(sample_list.copy())  # Use copy to keep original list
    print(f"Sorted list: {sorted_list}")
