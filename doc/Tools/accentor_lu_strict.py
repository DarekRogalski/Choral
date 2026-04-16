import re
from vulgate_dict_full import ACCENT_DICT

VOWELS = "aeiouy"
ACCENTS = {'a':'á','e':'é','i':'í','o':'ó','u':'ú','y':'ý'}

def normalize_latin(text):
    return (
        text
        .replace("æ", "ae")
        .replace("Æ", "Ae")
        .replace("œ", "oe")
        .replace("Œ", "Oe")
    )

def has_accent(word):
    return any(c in "áéíóúýÁÉÍÓÚÝ" for c in word)

def is_vowel(c):
    return c in VOWELS

def add_acute(c):
    return ACCENTS.get(c, c)

def fallback_accent(word):
    # LU STRICT = minimalny fallback
    # tylko słowa 3+ sylabowe
    w = word.lower()

    vowels = [i for i,c in enumerate(w) if is_vowel(c)]
    if len(vowels) < 3:
        return word  # NIE akcentujemy

    idx = vowels[-2]  # penultima
    w = list(w)
    w[idx] = add_acute(w[idx])
    return ''.join(w)

def accent_word(word):
    core = re.sub(r'[^A-Za-záéíóúýÁÉÍÓÚÝ]', '', word)
    if not core:
        return word

    # ✅ NOWE: jeśli już ma akcent → NIE ruszaj
    if has_accent(core):
        return word

    key = core.lower()

    # słownik
    if key in ACCENT_DICT:
        return word.replace(core, ACCENT_DICT[key])

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