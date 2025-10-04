import json
from collections import Counter

file_path = 'public/words.json'

print(f'Checking for duplicates in {file_path}...\n')

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        words_data = json.load(f)

    # Extract all word values
    words_list = [entry.get('word') for entry in words_data if entry.get('word')]

    # Count occurrences of each word
    word_counts = Counter(words_list)

    # Find words that appear more than once
    duplicates = {word: count for word, count in word_counts.items() if count > 1}

    if duplicates:
        print('Found the following duplicates:')
        for word, count in duplicates.items():
            print(f'  - "{word}" appears {count} times')
    else:
        print('No duplicate words found.')

except FileNotFoundError:
    print(f'Error: The file {file_path} was not found.')
except json.JSONDecodeError:
    print(f'Error: Could not decode JSON from {file_path}.')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
