# Two Sum
# Write a Python function two_sum(nums, target) that takes a list of integers nums and an integer target. The function should return the indices of the two numbers in the list that add up to the target. You may assume that each input will have exactly one solution, and you may not use the same element twice.

# input: [2, 7, 11, 15], 9
# output: [0, 1]   because nums[0] + nums[1] = 2 + 7 = 9

def two_sum(nums, target):
    # Create a dictionary to store the complement and its index


    # Iterate through the list

        # Calculate the complement


        # Check if complement is in the map


        # Otherwise, add the current number and its index to the map



print(two_sum([2, 7, 11, 15], 9))
