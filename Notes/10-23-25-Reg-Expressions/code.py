import re
file_path = "/home/rjae/4143-Java-and-Python/Notes/10-21-25-Text-Processing/Frankenstein.txt"

# Program 1: Extract all words that start with a capital letter
with open(file_path, encoding="utf-8") as fin:
    text = fin.read()

    # \b is a regex word boundary, not an escape slash because of the `r` beforehand
    caps = re.findall(r"\b[A-Z][a-z]*\b", text)
    print(caps)

# Program 2: Extract all numbers in the text
with open(file_path, encoding="utf-8") as fin:
    text = fin.read()

    # Note: Several ways to do this regex (and pretty much everything else has numerous ways)
    # `r"\d+"` or 
    nums = re.findall(r"\d[0-9]*", text)
    print(nums)

# Program 3: Find all words that end with `ing`
with open(file_path, encoding="utf-8") as fin:
    text = fin.read()

    ing = re.findall(r"\b\w+ing", text)
    print(ing)

# Program 4: Replace any sequence of multiple spaces with a single space
with open(file_path, encoding="utf-8") as fin:
    sentence = "Too many     spaces.                   Fix         this\n sentence."

    # newSentence = re.sub(r"\s+", " ", sentence)
    newSentence = re.sub(r"\s{2,}", " ", sentence)

    print(newSentence)

# Program 5: Find and print all sentences starting with the word "Upon"
with open(file_path, encoding="utf-8") as fin:
    text = fin.read()
    upon = re.findall(r"\bUpon[^.!?]*[.?!]", text)
    print(upon)

# Program 6: Extract and print all words that are exactly 10 characters long
with open(file_path, encoding="utf-8") as fin:
    text = fin.read()
    ten = re.findall(r"\b[A-Z][a-z]{10}\b", text)
    print(ten)
