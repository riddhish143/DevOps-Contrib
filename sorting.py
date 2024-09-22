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


# Radix sort in Python
# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radix_sort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
    
    return array


def get_algorithm_choice():
    """Get user choice for sorting algorithm."""
    print("Choose a sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Heap Sort")
    print("7. Radix Sort")
   
    choice = input("Enter the number of the algorithm: ")
    return choice


def get_array_input():
    """Get array input from the user."""
    arr = input("Enter the array elements separated by spaces (e.g., 0.78 0.17 0.39): ")
    arr = list(map(int, arr.split()))
    return arr


# Example usage
if __name__ == "__main__":

    sample_array = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.55, 0.88, 0.99]
    
    # Uncomment the sorting function you want to test
    # bubble_sort(sample_array)
    # selection_sort(sample_array)
    # insertion_sort(sample_array)
    # merge_sort(sample_array)
    # quick_sort(sample_array)
    # shail merge 
    # heap_sort(sample_array)
    sorted_array = merge_sort(sample_array)

    
    print("Sorted array:", sorted_array)
    sample_array = get_array_input()
    choice = get_algorithm_choice()

    # Sorting based on user's choice
    if choice == "1":
        sorted_array = bubble_sort(sample_array)
    elif choice == "2":
        sorted_array = selection_sort(sample_array)
    elif choice == "3":
        sorted_array = insertion_sort(sample_array)
    elif choice == "4":
        sorted_array = merge_sort(sample_array)
    elif choice == "5":
        sorted_array = quick_sort(sample_array)
    elif choice == "6":
        sorted_array = heap_sort(sample_array)
    elif choice == "7":
        sorted_array = radix_sort(sample_array)
    else:
        print("Invalid choice! Exiting.")
        sorted_array = None

    if sorted_array is not None:
        print("Sorted array:", sorted_array)

