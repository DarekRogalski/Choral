import re
from vulgate_dict import ACCENT_DICT

VOWELS = "aeiouy"
ACCENTS = {'a':'á','e':'é','i':'í','o':'ó','u':'ú','y':'ý'}

def normalize_latin(text):
    return (
        text
        .replace("æ", "ae")
        .replace("Æ", "Ae")
        .replace("œ", "oe")
        .replace("Œ", "Oe")
        .replace("ǽ", "aé")
    )

def remove_verse_numbers(text):
    lines = text.splitlines()
    lines = [re.sub(r'^\d+:\d+[a-zA-Z]?\s+', '', line) for line in lines]
    return "\n".join(lines)

def has_accent(word):
    return any(c in "áéíóúýÁÉÍÓÚÝ" for c in word)

def is_vowel(c):
    return c in VOWELS

def add_acute(c):
    return ACCENTS.get(c, c)

# 🔥 fallback (gdy brak w słowniku)
def fallback_accent(word):
    # w = word.lower()
    w = word
    vowels = [i for i,c in enumerate(w) if is_vowel(c)]

    if len(vowels) <= 1:
        return word

    if len(vowels) == 2:
        idx = vowels[0]
    else:
        idx = vowels[-2]  # uproszczona penultima

    new = list(w)
    new[idx] = add_acute(new[idx])

    return ''.join(new)

def accent_word(word):
    core = re.sub(r'[^A-Za-záéíóúýÁÉÍÓÚÝ]', '', word)
    if not core:
        return word

    # ✅ NOWE: jeśli już ma akcent → NIE ruszaj
    if has_accent(core):
        return word

    # pierwsze słowo ma pozostać z wielkiej litery!
    key = core

    # słownik
    if key in ACCENT_DICT:
        ww = ACCENT_DICT[key]
        w = word.replace(core, ww)
        return w

    # fallback
    return word.replace(core, fallback_accent(core))

def accent_text(text):
    # ✅ NORMALIZACJA NA START
    text = normalize_latin(text)

    tokens = re.findall(r'\w+|\W+', text)

    return ''.join(
        accent_word(t) if re.match(r'^[A-Za-záéíóúýÁÉÍÓÚÝ]+$', t) else t
        for t in tokens
    )