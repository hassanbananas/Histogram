# Prerequisites:
# matplotlib
# python3-tk (or any other matplotlib GUI backend)

import os
import matplotlib.pyplot as plt
from collections import Counter

# Dictionary file path
dict_path = '/usr/share/dict/words'

if os.path.exists(dict_path):
    with open(dict_path, 'r') as file:
        # Read words in file
        words = file.read()

    # Initialize counter
    letter_count = Counter()

    # Count each letter
    for letter in words:
        if letter.isalpha():
            letter_count[letter.lower()] += 1

    # Sort alphabetically
    letters_sorted =sorted(letter_count.items())

    # Separate for plotting
    letters, counts = zip(*letters_sorted)

    # Plotting
    plt.bar(letters, counts)
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Histogram of Letter Frequencies in Dictionary File')
    plt.show()

else:
    print(f"File not found at {dict_path}")