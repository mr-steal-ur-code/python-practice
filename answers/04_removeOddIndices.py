def remove_odd_indices(lst):
    # Step 1: Use list slicing to get elements at even indices
    # start : stop : step
    result = lst[::2]

    # Step 2: Return the new list
    return result


# Example usage
lst = [10, 21, 32, 43, 54, 65, 76]
result = remove_odd_indices(lst)
print(result)  # Output: [10, 32, 54, 76]
