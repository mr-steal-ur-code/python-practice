# Create a Python function that takes a dictionary as input and returns a new dictionary where the keys and values are swapped.

# input = {"a": 1, "b": 2, "c": 3}
# output = {1: 'a', 2: 'b', 3: 'c'}

def swap_keys_and_values(input):
    output = {}
    for key, value in input.items():
        output[value] = key
    return output


print(swap_keys_and_values({"a": 1, "b": 2, "c": 3}))
