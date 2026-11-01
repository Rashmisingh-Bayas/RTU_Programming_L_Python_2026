"""
Task 4 – Text-based Arithmetic Analyzer
---------------------------------------
Create a text-based analyzer made of small helper functions.

Rules used by all functions:
- Words are pieces of text separated by whitespace (use .split()).
- A NUMBER is a word that is a whole integer, optionally with a leading
  minus sign, e.g. "7", "42", "-3".
  Punctuation at the end of a word is ignored, so "5," "10." "8!" count
  as 5, 10 and 8. Use word.rstrip(".,!?;:") to remove it.
  Decimals ("3.5") and mixed words ("abc123") are NOT numbers.
- You do not need the `re` module; .split(), .rstrip() and .isdigit()
  are enough.

Helper functions:
- count_characters(text) -> int    : characters that are not whitespace
- count_words(text)      -> int    : number of words
- extract_numbers(text)  -> list   : list of ints, in the order they appear
- analyze_text(text)     -> dict   : combines the helpers (see below)

analyze_text() returns a dict with exactly these keys:
    "characters" : int   (from count_characters)
    "words"      : int   (from count_words)
    "numbers"    : list  (from extract_numbers)
    "sum"        : int   (sum of the numbers, 0 if there are none)
    "average"    : float (average of the numbers, 0.0 if there are none,
                          NOT rounded)

In the main block: read a line of text, call analyze_text(), and print a
summary. Round the average to 2 decimals when printing.

Example run:
    Enter text: I have 3 apples and 5 pears
    Characters (no spaces): 21
    Words: 7
    Numbers: [3, 5]
    Sum: 8
    Average: 4.00

Examples (these are also used to check your work):
>>> count_characters("a b  c")
3
>>> count_words("I have 3 apples and 5 pears")
7
>>> extract_numbers("Scores: 10, -4 and 7! but not 3.5 or abc123")
[10, -4, 7]
>>> result = analyze_text("I have 3 apples and 5 pears")
>>> result["characters"], result["words"], result["numbers"]
(21, 7, [3, 5])
>>> result["sum"], result["average"]
(8, 4.0)
>>> analyze_text("no numbers here")["average"]
0.0
"""


def count_characters(text: str) -> int:
    """Count characters that are not whitespace."""
    count = 0
    # Loop through every character in the string
    for char in text:
        # .isspace() checks if it's a space, tab, or newline
        if not char.isspace():
            count += 1
    return count


def count_words(text: str) -> int:
    """Count number of whitespace-separated words."""
    # .split() automatically breaks the string into a list of words
    words = text.split()
    return len(words)


def extract_numbers(text: str) -> list[int]:
    """Return a list of the integers found in text, in order."""
    numbers = []

    # Split the text into words
    words = text.split()

    for word in words:
        # Remove punctuation from the end of the word
        clean_word = word.rstrip(".,!?;:")

        # A neat trick to check if a string is a valid integer:
        # If we try to convert it and it fails, it's not a number.
        try:
            number = int(clean_word)
            numbers.append(number)
        except ValueError:
            # If int() fails (like for "3.5" or "abc123"), we just skip it
            pass

    return numbers


def analyze_text(text: str) -> dict:
    """Return a dict with characters, words, numbers, sum and average."""
    # Call our helper functions
    chars = count_characters(text)
    words = count_words(text)
    nums = extract_numbers(text)

    # Calculate sum (sum of an empty list is 0, which is perfect)
    total_sum = sum(nums)

    # Calculate average carefully to avoid dividing by zero
    if len(nums) > 0:
        average = total_sum / len(nums)
    else:
        average = 0.0

    # Return the final dictionary
    return {
        "characters": chars,
        "words": words,
        "numbers": nums,
        "sum": total_sum,
        "average": average,
    }


if __name__ == "__main__":
    # Keep all input() calls inside this block, otherwise the autograder
    # cannot import your file.

    # Read a line of text from the user
    user_text = input("Enter text: ")

    # Analyze it
    result = analyze_text(user_text)

    # Print the summary, rounding the average to 2 decimals
    print(f"Characters (no spaces): {result['characters']}")
    print(f"Words: {result['words']}")
    print(f"Numbers: {result['numbers']}")
    print(f"Sum: {result['sum']}")
    print(f"Average: {result['average']:.2f}")
