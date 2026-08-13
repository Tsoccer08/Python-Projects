# Segregation Sort
#
# Implements a recursive segregation sort algorithm using a middle
# element as the pivot. The array is partitioned around the pivot,
# then the left and right partitions are sorted recursively.


def segregation_sort(array, left, right):
    """Recursively sort a portion of an array."""

    if left < right:
        pivot = find_pivot(array, left, right)
        partition_index = partition_array(
            array, left, right, pivot
        )

        segregation_sort(array, left, partition_index - 1)
        segregation_sort(array, partition_index, right)


def find_pivot(array, left, right):
    """Return the middle element as the pivot."""

    pivot_index = (left + right) // 2
    return array[pivot_index]


def partition_array(array, left, right, pivot):
    """Partition an array around the pivot value."""

    i = left
    j = right

    while i <= j:
        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    return i


def sort(array):
    """Sort an entire array using segregation sort."""

    if len(array) > 1:
        segregation_sort(array, 0, len(array) - 1)


def main():
    """Run a collection of sorting tests."""

    test_cases = [
        ("Empty List", [], []),
        ("Minimal Input", [7], [7]),
        ("Smallest Non-Trivial Case", [9, 3], [3, 9]),
        (
            "Already Sorted",
            [1, 2, 3, 4, 5, 6, 7],
            [1, 2, 3, 4, 5, 6, 7]
        ),
        (
            "Zig-Zag Pattern",
            [7, 1, 6, 2, 5, 3, 4],
            [1, 2, 3, 4, 5, 6, 7]
        ),
        (
            "Misaligned Partitions",
            [3, 1, 2, 5, 4, 6, 7],
            [1, 2, 3, 4, 5, 6, 7]
        ),
        (
            "Duplicate Values",
            [4, 2, 4, 4, 3, 2, 1],
            [1, 2, 2, 3, 4, 4, 4]
        ),
        (
            "Negative Integers",
            [-3, 5, -1, 4, 0],
            [-3, -1, 0, 4, 5]
        ),
        (
            "General Case",
            [8, 3, 7, 1, 9, 2, 6, 4, 5],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
    ]

    print("Segregation Sort Tests\n")

    for name, values, expected in test_cases:
        original = list(values)
        sort(values)

        assert values == expected, (
            f"{name} failed: expected {expected}, got {values}"
        )

        print(f"PASS: {name}")
        print(f"  Before: {original}")
        print(f"  After:  {values}\n")

    print("All test cases passed successfully!")


if __name__ == "__main__":
    main()
