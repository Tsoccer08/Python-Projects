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

    # Make sure the array is not empty
    assert len(power_values) > 0, "Power array should not be empty."

    length = len(power_values)

    # Prompt for sub-array size
    try:
        sub_size = int(input("Enter the sub-array size: "))
    except ValueError:
        print("Error: Sub-array size must be an integer.")
        return

    if sub_size <= 0 or sub_size > length:
        print(
            "Error: Sub-array size must be greater than 0 and "
            "less than or equal to the array length."
        )
        return

    # Make sure the sub-array size is valid
    assert 1 <= sub_size <= length, "Sub-array size out of valid range."

    # Calculate the sum of the first window
    current_sum = 0

    for i in range(sub_size):
        current_sum += power_values[i]

    highest_avg = current_sum / sub_size

    # Make sure the initial average is valid
    assert highest_avg >= 0, "Initial average should not be negative."

    # Sliding window
    for j in range(sub_size, length):
        current_sum -= power_values[j - sub_size]
        current_sum += power_values[j]

        current_avg = current_sum / sub_size

        if current_avg > highest_avg:
            highest_avg = current_avg

    # Display the result
    print(f"Highest average power: {highest_avg:.2f}")


if __name__ == "__main__":
    main()
