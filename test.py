def merge_sort(array):
    if len(array) <= 1:
        return array  # Base case: A single element is already sorted

    # Split the array into two halves
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_array = []
    i = j = 0

    # Merge elements from left and right arrays in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Append remaining elements, if any
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    print(sorted_array)
    return sorted_array


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10, 1]
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)


""" OUTPUT PROCESS:
[27, 38] - first two compared, sorted and merged
[3, 43]  - second two compared, sorted and merged
[3, 27, 38, 43] 
[9, 82]
[1, 10]
[1, 9, 10, 82]
[1, 3, 9, 10, 27, 38, 43, 82]
Sorted Array: [1, 3, 9, 10, 27, 38, 43, 82]


"""