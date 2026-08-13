# 1. Name:
#    Troy Justesen
# 2. Assignment Name:
#    Lab 13 : Segregation Sort Program
# 3. Assignment Description:
#    This program implements the segregation sort algorithm. It sorts arrays
#    by selecting a middle pivot, partitioning values around the pivot, and
#    recursively sorting the left and right subarrays.
# 4. What was the hardest part? Be as specific as possible.
#    The hardest part was determining the correct way to partition the
#    array by finding that pivot in the center and making sure it finds
#    the correct values to swap.
# 5. How long did it take for you to complete the assignment?
#    Approximately 1 hour 20 minutes.

# Function to perform segregation sort recursively
def segregation_sort(array, left, right):

    # Check if the current subarray has more than one element
    if left < right:

        # Find the pivot value from the middle of the array
        pivot = find_pivot(array, left, right)

        # Partition the array around the pivot
        partition_index = partition_array(array, left, right, pivot)

        # Recursively sort the left partition
        segregation_sort(array, left, partition_index - 1)

        # Recursively sort the right partition
        segregation_sort(array, partition_index, right)


# Function to select the pivot (middle element)
def find_pivot(array, left, right):

    # Calculate the index of the middle element
    pivot_index = (left + right) // 2

    # Return the pivot value
    return array[pivot_index]


# Function to partition the array around the pivot
def partition_array(array, left, right, pivot):

    # Initialize left pointer
    i = left

    # Initialize right pointer
    j = right

    # Continue until pointers cross
    while i <= j:

        # Move left pointer until a value >= pivot is found
        while array[i] < pivot:
            i += 1

        # Move right pointer until a value <= pivot is found
        while array[j] > pivot:
            j -= 1

        # If pointers have not crossed, swap values
        if i <= j:

            # Swap the elements at i and j
            array[i], array[j] = array[j], array[i]

            # Move both pointers inward
            i += 1
            j -= 1

    # Return the partition index for the right subarray
    return i


# Wrapper function to simplify sorting the entire array
def sort(array):

    # Only sort if the array has more than one element
    if len(array) > 1:
        segregation_sort(array, 0, len(array) - 1)


# Driver function to test segregation sort
def main():

    # Display program introduction
    print("Segregation Sort Program\n")

    # Define test cases: (description, input array, expected sorted array)
    test_cases = [
        ("Empty List", [], []),
        ("Minimal Input", [7], [7]),
        ("Smallest Non-Trivial Case", [9, 3], [3, 9]),
        ("Best Case (Already Partitioned)", [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
        ("Worst Case (Zig-Zag Pattern)", [7, 1, 6, 2, 5, 3, 4], [1, 2, 3, 4, 5, 6, 7]),
        ("Misaligned Partitions", [3, 1, 2, 5, 4, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
        ("Duplicate Values", [4, 2, 4, 4, 3, 2, 1], [1, 2, 2, 3, 4, 4, 4]),
        ("Negative Integers", [-3, 5, -1, 4, 0], [-3, -1, 0, 4, 5]),
        ("General Case", [8, 3, 7, 1, 9, 2, 6, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9])
    ]

    # Loop through each test case
    for name, arr, expected in test_cases:

        # Print the test case name and original array
        print(f"Test Case: {name}")
        print(f"Before: {arr}")

        # Make a copy to avoid modifying the original array
        arr_copy = list(arr)

        # Sort the array using segregation sort
        sort(arr_copy)

        # Print the sorted array
        print(f"After:  {arr_copy}")

        # Verify the result matches expected output
        assert arr_copy == expected, f"Test {name} failed! Got {arr_copy}"

        # Pause between test cases for demonstration
        input("Press ENTER for next test...\n")

    # Print success message after all tests pass
    print("\nAll test cases passed successfully!")


# Entry point of the program
if __name__ == "__main__":
    main()