import sys
import string


def count_unique_word():
    words = {}  # create an empty dictionary
    strip = string.whitespace + string.punctuation + string.digits + "\"’"
    for filename in sys.argv[1:]:
        with open(filename) as file:
            for line in file:
                for word in line.lower().split():
                    word = word.strip(strip)
                    if len(word) > 2:
                        words[word] = words.get(word, 0) + 1
    for word in sorted(words):
        print("’{0}’ occurs {1} times.".format(word, words[word]))
