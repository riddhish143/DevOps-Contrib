def bubble_sort(arr):
    """Bubble Sort Algorithm"""
    pass


def selection_sort(arr):
    """Selection Sort Algorithm"""
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