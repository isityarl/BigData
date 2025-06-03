#!/usr/bin/env python3
import sys
import random
import re

pirate_dict = {
    "for": "fo",
    "sure": "sho",
    "the": "da",
    "and": "an'",
    "hello": "ahoy",
    "yes": "aye",
    "my": "me",
    "friend": "matey",
}

def to_pirate_speak(text):
    words = text.split()
    new_words = []
    for word in words:
        lower_word = word.lower().strip(".,!?:;")
        if lower_word in pirate_dict:
            word = pirate_dict[lower_word]

        if word.endswith("ing"):
            word = word[:-3] + "in'"

        if random.random() < 0.05:
            word = re.sub(r'[aeiouAEIOU][^aeiou]*$', 'izzle', word)

        if random.random() < 0.01:
            word += " kno’ wha’ I’m sayin’?"

        new_words.append(word)

    return ' '.join(new_words)

for line in sys.stdin:
    pirate_text = to_pirate_speak(line.strip())
    print(pirate_text)
