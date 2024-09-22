def bubble_sort(arr):
    """Bubble Sort Algorithm"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
    pass

def insertion_sort(arr):
    """Insertion Sort Algorithm"""
    n = len(arr)
    if n <= 1:
        return
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr

def merge_sort(arr):
    """Merge Sorting Algorithm"""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
    


def quicksort(arr):

  if len(arr) <= 1:
    return arr

  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]

  return quicksort(left) + middle + quicksort(right)


def heap_sort(arr):
    """Heap Sort Algorithm"""
    pass


def counting_sort(arr):
    """Counting Sort Algorithm"""

    M = max(arr)
    count_array = [0] * (M + 1)

    for num in arr:
        count_array[num] += 1

    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]

    output_array = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        output_array[count_array[arr[i]] - 1] = arr[i]
        count_array[arr[i]] -= 1

    return output_array


def bucket_sort(array):
    """Bucket Sort Algorithm"""
    if len(array) == 0:
        return array

    # Create empty buckets
    bucket_count = 10  # Number of buckets
    buckets = [[] for _ in range(bucket_count)]

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(bucket_count * j)  # Adjusted for float values
        if index_b == bucket_count:  # Handle the case where j is 1.0
            index_b -= 1
        buckets[index_b].append(j)

    # Sort the elements of each bucket
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))  # Sort each bucket

    return sorted_array


# Example usage
if __name__ == "__main__":
    sample_array = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.55, 0.88, 0.99]
    
    # Uncomment the sorting function you want to test
    # bubble_sort(sample_array)
    # selection_sort(sample_array)
    # insertion_sort(sample_array)
    # merge_sort(sample_array)
    # quick_sort(sample_array)
    # heap_sort(sample_array)
    sorted_array = merge_sort(sample_array)

    
    print("Sorted array:", sorted_array)
