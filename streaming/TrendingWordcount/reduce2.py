#!/usr/bin/env python3
import sys

current_date_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    date_word, count = line.rsplit('\t', 1)
    count = int(count)

    date_str, word = date_word.split('\t')
    date_word_tuple = (date_str, word)

    if current_date_word == date_word_tuple:
        current_count += count
    else:
        if current_date_word:
            print(f"{current_date_word[0]}, {current_date_word[1]}, {current_count}")
        current_date_word = date_word_tuple
        current_count = count

if current_date_word:
    print(f"{current_date_word[0]}, {current_date_word[1]}, {current_count}")
