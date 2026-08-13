# 1. Name:
#      Troy Justesen
# 2. Assignment Name:
#      Lab 13: Power
# 3. Assignment Description:
#      This program reads power measurement data from a JSON file and 
#      finds the highest average power from a sub-array size using a
#      sliding window algorithm.
# 4. What was the hardest part? Be as specific as possible.
#      This one wasn't too bad, where the only part I needed to figure 
#      out was how to properly validate if there was an array in 
#      the file or not.
# 5. How long did it take for you to complete the assignment?
#      1 hour 23 minutes.

import json


def main():
    # Prompt for filename
    filename = input("Enter power data filename: ")

    # Read file
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: File does not exist.")
        return

    # Validate JSON structure
    if "array" not in data:
        print("Error: JSON file must contain 'array' as the first key.")
        return

    power_values = data["array"]

    if not isinstance(power_values, list):
        print("Error: 'array' must be a list.")
        return

    if not all(isinstance(value, int) for value in power_values):
        print("Error: All values in the array must be integers.")
        return

    # Assert: error if array is empty
    assert len(power_values) > 0, "Power array should not be empty."

    length = len(power_values)

    # Prompt for sub-array size
    try:
        sub_size = int(input("Enter the sub-array size: "))
    except ValueError:
        print("Error: Sub-array size must be an integer.")
        return

    if sub_size <= 0 or sub_size > length:
        print("Error: Sub-array size must be greater than 0 and less " \
        "than or equal to the array length.")
        return

    # Assert: valid sub-array bounds
    assert 1 <= sub_size <= length, "Sub-array size out of valid range."

    # Compute initial sum
    current_sum = 0
    for i in range(sub_size):
        current_sum += power_values[i]

    highest_avg = current_sum / sub_size

    # Assert: average sanity check
    assert highest_avg >= 0, "Initial average should not be negative."

    # Sliding window
    for j in range(sub_size, length):
        current_sum -= power_values[j - sub_size]
        current_sum += power_values[j]

        current_avg = current_sum / sub_size

        if current_avg > highest_avg:
            highest_avg = current_avg

    # Output result
    print(f"Highest average power: {highest_avg:.2f}")


main()