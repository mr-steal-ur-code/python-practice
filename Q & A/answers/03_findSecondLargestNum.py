def second_largest(lst):
    # Step 1: Remove duplicates by converting the list to a set
    unique_elements = list(set(lst))

    # Step 2: Check if there are at least two unique elements
    if len(unique_elements) < 2:
        return None

    # Step 3: Sort the unique elements in descending order
    unique_elements.sort(reverse=True)

    # Step 4: Return the second largest element
    return unique_elements[1]


# Example usage
lst = [7, 3, 9, 1, 9]
result = second_largest(lst)
print(result)  # Output: 7
