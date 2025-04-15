def merge_sort(arr):
    # Base case: If the array has 1 or no elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Step 2: Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Step 3: Merge the sorted halves
    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0

    # Step 4: Compare elements from both halves and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from the left half
    while i < len(left):
        result.append(left[i])
        i += 1

    # Append any remaining elements from the right half
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Example Usage
if __name__ == "__main__":
    unsorted_array = [38, 27, 43, 3, 9, 82, 10]
    sorted_array = merge_sort(unsorted_array)
    print("Unsorted Array:", unsorted_array)
    print("Sorted Array:", sorted_array)
