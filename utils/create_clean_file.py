import json

input_file = '../public/words.json'
output_file = '../public/words.json'  # Overwrite the original file

print(f'Reading from {input_file} and writing unique words to {output_file}...\n')

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        words_data = json.load(f)

    unique_words = set()
    cleaned_data = []

    for entry in words_data:
        word = entry.get('word')
        if word and word not in unique_words:
            unique_words.add(word)
            cleaned_data.append(entry)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, indent=2, ensure_ascii=False)

    removed_count = len(words_data) - len(cleaned_data)
    if removed_count > 0:
        print(f'Successfully removed {removed_count} duplicate(s).')
    else:
        print('No duplicates were found.')
    
    print(f'Cleaned data has been saved to {output_file}.')

except FileNotFoundError:
    print(f'Error: The file {input_file} was not found.')
except json.JSONDecodeError:
    print(f'Error: Could not decode JSON from {input_file}.')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
