# Write a Python function that takes a sentence as input and returns a new sentence with the words reversed and special characters removed.
import re


def reverse_words(str: str):
    cleaned = re.sub(r'[^a-zA-Z" "]', "", str)
    return " ".join(cleaned.split()[::-1])


print(reverse_words("Hello, how are you?"))
