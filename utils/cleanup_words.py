import json

file_path = 'public/words.json'

# Words to remove (Epicene Nouns and Adjectives)
words_to_remove = {
    'list', 'of words to remove', 
}

try:
    # Read the original data
    with open(file_path, 'r', encoding='utf-8') as f:
        words_data = json.load(f)

    # Filter out the words to be removed
    cleaned_data = [entry for entry in words_data if entry.get('word') not in words_to_remove]

    # Write the cleaned data back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, indent=2, ensure_ascii=False)

    print(f'Successfully removed {len(words_data) - len(cleaned_data)} words from {file_path}')

except FileNotFoundError:
    print(f'Error: The file {file_path} was not found.')
except json.JSONDecodeError:
    print(f'Error: Could not decode JSON from {file_path}.')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
