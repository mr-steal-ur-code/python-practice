# Find the First Non-Repeating Character in a String
# Write a JavaScript function firstNonRepeatingChar that takes a string as input and returns the first non-repeating character in the string. If all characters are repeating, return null.


def first_non_repeating_char(s):
    char_count = {}

    # Count occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first character with a count of 1
    for char in s:
        if char_count[char] == 1:
            return char

    # If no non-repeating character is found
    return None


print(first_non_repeating_char("swiss"))   # "w"
print(first_non_repeating_char("success"))  # "u"
print(first_non_repeating_char("aabbcc"))  # None
