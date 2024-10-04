def filter_and_sort(lst):
    # Step 1: Remove duplicates by converting the list to a set
    unique_elements = set(lst)

    # Step 2: Sort the unique elements in descending order
    sorted_list = sorted(unique_elements, reverse=True)

    return sorted_list


# Example usage
# Output: [9, 7, 5, 3, 2, 1]
print(filter_and_sort([5, 1, 9, 2, 9, 5, 1, 3, 7]))
