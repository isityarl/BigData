#!/usr/bin/env python3
import sys
import re

def safe_decode(line):
    try:
        return line.decode('utf-8')
    except UnicodeDecodeError:
        return line.decode('latin-1')

def is_valid_word(word):
    if len(word) < 2 or len(word) > 20:
        return False
    if re.search(r'(.)\1{3,}', word):
        return False
    if re.search(r'\d', word):
        return False
    if not re.match(r'^[a-zA-Z]+$', word):
        return False
    return True

for line in sys.stdin.buffer:
    try:
        line = safe_decode(line).strip()
        columns = line.split(",")
        if len(columns) > 4:
            date_str = columns[2][4:10]
            day = date_str.split()[1]
            if day == "0":
                continue
            tweet_text = columns[4].lower().strip()
            words = re.findall(r'\w+', tweet_text)
            for word in words:
                if is_valid_word(word):
                    print(f"{date_str}\t{word}\t1")
    except Exception as e:
        continue
