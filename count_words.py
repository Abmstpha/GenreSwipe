import json

file_path = 'public/words.json'

try:
    # Read the data from the file
    with open(file_path, 'r', encoding='utf-8') as f:
        words_data = json.load(f)

    # Get the total number of words
    word_count = len(words_data)

    print(f'Total number of words in {file_path}: {word_count}')

except FileNotFoundError:
    print(f'Error: The file {file_path} was not found.')
except json.JSONDecodeError:
    print(f'Error: Could not decode JSON from {file_path}.')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
