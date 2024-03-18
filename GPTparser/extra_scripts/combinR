#!/usr/bin/env python3

# Will combine all individual .json files into one .jsonl dataset
# Creates individual JSON objects as separate lines per Chat Completions format for OpenAI Fine-Tuning
# Add to $PATH, and run from inside directory with individual .json files: $ combinR output_dataset.jsonl

import os
import json
import sys
from pathlib import Path

def main():
    # run with ./script.py output.jsonl
    if len(sys.argv) < 2:
        print("Usage: combine <output_file_name>")
        sys.exit(1)
    output_file_name = sys.argv[1]

    # apply within directory with valid JSON files
    current_dir = Path.cwd()

    dataset = []

    # flexible json.load to apply to arrays or objects = flexible. and works with list of messages or single message object.
    for file_path in current_dir.glob("*.json"):
        with open(file_path, 'r') as f:
            file_data = json.load(f)
            if isinstance(file_data, list):
                dataset.extend(file_data)
            else:
                dataset.append(file_data)

    # Now you have a single list 'dataset' containing all the data from the files
    print(f"Combined dataset contains {len(dataset)} samples.")

    # this will go through each line and writes them each as a JSON object per OPENAI formatting.
    with open(output_file_name, "w") as outfile:
        for entry in dataset:
            # JSON objects put on lines
            json.dump(entry, outfile)
            outfile.write('\n')  # newline character separates objects

    print(f"Combined dataset saved as {output_file_name}")

if __name__ == "__main__":
    main()
