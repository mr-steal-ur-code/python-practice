# Find the Longest Substring Without Repeating Characters
# Description: Given a string s, find the length of the longest substring without repeating characters.

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.


def length_of_longest_substring(s: str) -> int:
    # Initialize a set to track the characters in the current window

    # Pointers for the sliding window

    # Iterate over the string with the right pointer

    # If the character at the right pointer is already in the set, remove characters from the left until it's no longer in the set

    # Add the current character to the set and update the maximum length


print(length_of_longest_substring("pwwkew"))
print(length_of_longest_substring("abccde"))
print(length_of_longest_substring("bbbbb"))
