from collections import Counter
import re

def count_word_frequency(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words)

    top_words = word_counts.most_common(10)
    with open('word_frequencies.txt', 'w') as output_file:
        for word, count in top_words:
            output_file.write(f"{word}: {count}\n")
            print(f"{word}: {count}")

count_word_frequency('large_text_file.txt')