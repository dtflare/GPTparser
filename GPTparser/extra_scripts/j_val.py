#!/usr/bin/env python3

# Add to $PATH and run from within current directory with the parsed .json files
# Will output Valid/Invalid and any errors.
# To run: $ j_val
# To edit invalid file, I recommend using: https://jsonlint.com/

import json
import os
import sys

def validate_json(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r') as file:
                    json.load(file)
                print(f"Valid JSON: {filename}")
            except json.JSONDecodeError as e:
                print(f"Invalid JSON in {filename}: {e}")

def main():
    # Use the current directory if no argument is provided
    directory = sys.argv[1] if len(sys.argv) == 2 else "."
    
    validate_json(directory)

if __name__ == "__main__":
    main()
