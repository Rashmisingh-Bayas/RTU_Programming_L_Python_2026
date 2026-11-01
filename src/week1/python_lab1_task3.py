"""
Task 3 – Function with Combined Logic
-------------------------------------
Write a function `analyze_sentence(text)` that returns a tuple of three values,
in this order:
1. total character count of the text exactly as given, spaces included (len)
2. word count, where words are separated by whitespace (.split())
3. True if "python" appears anywhere in the text, ignoring case, else False
   (a simple substring check: "Pythonic" and "PYTHON!" both count)

Return type: (int, int, bool)

In the main block: read a sentence, call the function, and print a summary.

Example run:
    Enter a sentence: I love Python
    Characters: 13
    Words: 3
    Contains 'Python': True

Examples (these are also used to check your work):
>>> analyze_sentence("I love Python")
(13, 3, True)
>>> analyze_sentence("  Hello   world  ")
(17, 2, False)
>>> analyze_sentence("PYTHONIC code!")
(14, 2, True)
>>> analyze_sentence("")
(0, 0, False)
"""


def analyze_sentence(text: str) -> tuple[int, int, bool]:
    """Return (length, word count, contains 'python') for the given text."""

    # 1. Character count: len() counts every character, including spaces
    char_count = len(text)

    # 2. Word count: .split() breaks the string into a list of words based on whitespace
    words = text.split()
    word_count = len(words)

    # 3. Check for 'python' ignoring case.
    # We convert the text to lowercase, then check if "python" is inside it.
    # This handles "Python", "PYTHON", and "Pythonic".
    contains_python = "python" in text.lower()

    # Return the three results as a tuple
    return (char_count, word_count, contains_python)


if __name__ == "__main__":
    # Keep all input() calls inside this block, otherwise the autograder
    # cannot import your file.

    # Ask the user for a sentence
    user_sentence = input("Enter a sentence: ")

    # Call the function and unpack the tuple into three variables
    chars, words, has_python = analyze_sentence(user_sentence)

    # Print the results exactly as requested
    print(f"Characters: {chars}")
    print(f"Words: {words}")
    print(f"Contains 'Python': {has_python}")