import random

def partition(arr, low, high):
    """
    Partition the array around the pivot element.
    
    Parameters:
    arr (list): The array to partition.
    low (int): The starting index of the portion to partition.
    high (int): The ending index of the portion to partition.
    
    Returns:
    int: The index of the pivot element after partitioning.
    """
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:  # If current element is smaller than or equal to pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap the elements
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap the pivot element with the element at i+1
    return i + 1

def quick_select(arr, low, high, k):
    """
    Quick Select algorithm to find the k-th smallest element.
    
    Parameters:
    arr (list): The array to search.
    low (int): The starting index of the portion to search.
    high (int): The ending index of the portion to search.
    k (int): The index of the k-th smallest element to find (zero-based).
    
    Returns:
    int: The k-th smallest element in the array.
    """
    if low <= high:
        # Partition the array and get the index of the pivot element
        pi = partition(arr, low, high)

        # If pivot is at k, return the element at k
        if pi == k:
            return arr[pi]
        # If k is less than pivot index, recurse on the left sub-array
        elif pi > k:
            return quick_select(arr, low, pi - 1, k)
        # If k is greater than pivot index, recurse on the right sub-array
        else:
            return quick_select(arr, pi + 1, high, k)
    return None

def quick_select_main(arr, k):
    """
    Helper function to initiate Quick Select with correct k value.
    
    Parameters:
    arr (list): The array to search.
    k (int): The k-th smallest element to find (one-based).
    
    Returns:
    int: The k-th smallest element in the array.
    """
    # Adjust k to be zero-based
    return quick_select(arr, 0, len(arr) - 1, k - 1)

def main():
    """
    Main function to generate the array, prompt for k, and display the k-th smallest element.
    """
    # Generate a random array of 1000 elements
    array = [random.randint(1, 10000) for _ in range(1000)]
    print("Random array generated.")
    
    # Prompt the user to enter the value of k
    k = int(input("Enter the value of k (1 to 1000): "))
    if k < 1 or k > 1000:
        print("Invalid input! Please enter a value between 1 and 1000.")
        return
    
    # Find the k-th smallest element
    kth_smallest = quick_select_main(array, k)
    print(f"The {k}-th smallest element in the array is: {kth_smallest}")

# Entry point of the program
if __name__ == "__main__":
    main()
    
input("Press Enter to close the program.")
