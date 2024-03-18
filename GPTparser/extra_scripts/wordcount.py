#!/usr/bin/env python3

# uses regex to separate characters into words and exclude characters, symbols, numbers, etc.

# use countwords file.jsonl

import sys
import re

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # Match only sequences of alphabetic characters
            words = re.findall(r'\b[A-Za-z]+\b', content)
            num_words = len(words)
            print(f"The file '{filename}' contains {num_words} words.")
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python count_words.py <filename>")
    else:
        filename = sys.argv[1]
        count_words_in_file(filename)

if __name__ == "__main__":
    main()
