def find_max_min(numbers):
    """Finds the maximum and minimum values in a list of numbers.

    Args:
      numbers: A list of numbers.

    Returns:
      A tuple containing the maximum   
   and minimum values.
    """

    if not numbers:
        raise ValueError("List cannot be empty.")

    max_value = numbers[0]
    min_value = numbers[0]

    for num in numbers[1:]:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    return max_value, min_value


# Example usage:
my_list = [5, 2, 8, 1, 9, 3]
max_num, min_num = find_max_min(my_list)
print("Maximum value:", max_num)
print("Minimum value:", min_num)
