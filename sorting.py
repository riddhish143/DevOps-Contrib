def bubble_sort(arr):
    """Bubble Sort Algorithm"""
    pass


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
    pass

def merge_sort(arr):
    """Merge Sort Algorithm"""
    pass

def quick_sort(arr):
    """Quick Sort Algorithm"""
    pass


def heap_sort(arr):
    """Heap Sort Algorithm"""
    pass


def counting_sort(arr):
    """Counting Sort Algorithm"""
    pass


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
    sorted_array = bucket_sort(sample_array)
    
    print("Sorted array:", sorted_array)