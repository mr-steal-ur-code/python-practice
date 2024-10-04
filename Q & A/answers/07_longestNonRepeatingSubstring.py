# Find the Longest Substring Without Repeating Characters
# Description: Given a string s, find the length of the longest substring without repeating characters.

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.


def length_of_longest_substring(s: str) -> int:
    # Initialize a set to track the characters in the current window
    char_set = set()

    # Pointers for the sliding window
    left = 0
    max_length = 0

    # Iterate over the string with the right pointer
    for right in range(len(s)):
        # If the character at the right pointer is already in the set, remove characters from the left until it's no longer in the set
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add the current character to the set and update the maximum length
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


print(length_of_longest_substring("pwwkew"))
print(length_of_longest_substring("abccde"))
print(length_of_longest_substring("bbbbb"))
