from collections import Counter
import re

def extract_words(text):
    return re.findall(r"[A-Za-z]+", text.lower())

def build_missing_dict(raw_text, accented_text):
    raw_words = extract_words(raw_text)
    acc_words = extract_words(accented_text)

    mapping = {}

    for r, a in zip(raw_words, acc_words):
        if r != a:
            mapping[r] = a

    return mapping