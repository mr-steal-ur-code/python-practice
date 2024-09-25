import re


def count_word_frequencies(text):
    # Step 1: Convert the text to lowercase and remove punctuation
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Removes punctuation

    # Step 2: Split the text into words
    words = text.split()

    # Step 3: Create an empty dictionary to store word counts
    word_count = {}

    # Step 4: Count the frequency of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Step 5: Return the dictionary
    return word_count


# Example usage
text = "The quick brown fox jumps over the lazy dog. The dog barked."
result = count_word_frequencies(text)
print(result)
