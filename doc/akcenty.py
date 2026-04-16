# przygotuj plik psalmy.txt
# w bashu: python akcenty.py
# i otrzymamy psalmy_akcenty.txt
#
#

import re

VOWELS = "aeiouyáéíóúý"
DIPHTHONGS = ["ae", "oe", "au", "eu"]

def is_vowel(c):
    return c.lower() in VOWELS

def syllabify(word):
    word = word.lower()
    syllables = []
    i = 0
    current = ""

    while i < len(word):
        current += word[i]

        # sprawdź dyftong
        if i + 1 < len(word) and word[i:i+2] in DIPHTHONGS:
            current += word[i+1]
            i += 1

        # jeśli następny znak to samogłoska → nowa sylaba
        if i + 1 < len(word) and is_vowel(word[i]) and is_vowel(word[i+1]):
            syllables.append(current)
            current = ""

        # koniec słowa
        if i == len(word) - 1:
            syllables.append(current)

        i += 1

    return syllables


def is_heavy(syllable):
    # długa jeśli kończy się na 2 spółgłoski
    consonants = re.sub(r'[aeiouyáéíóúý]', '', syllable)
    return len(consonants) >= 2 or any(d in syllable for d in DIPHTHONGS)


def add_accent(word):
    original = word

    # usuń znaki interpunkcyjne na czas obróbki
    core = re.sub(r'[^a-zA-Z]', '', word)
    if not core:
        return word

    syllables = syllabify(core)

    # jednosylabowe → bez akcentu
    if len(syllables) == 1:
        return original

    # wybór sylaby akcentowanej
    if len(syllables) == 2:
        accent_index = 0
    else:
        penult = syllables[-2]
        if is_heavy(penult):
            accent_index = len(syllables) - 2
        else:
            accent_index = len(syllables) - 3

    # dodanie akcentu
    accented = ""
    for i, syl in enumerate(syllables):
        if i == accent_index:
            for j, c in enumerate(syl):
                if is_vowel(c):
                    syl = syl[:j] + add_acute(c) + syl[j+1:]
                    break
        accented += syl

    # przywróć oryginalne znaki (np. przecinki)
    return re.sub(core, accented, original, flags=re.IGNORECASE)


def add_acute(c):
    mapping = {
        'a': 'á', 'e': 'é', 'i': 'í',
        'o': 'ó', 'u': 'ú', 'y': 'ý',
        'A': 'Á', 'E': 'É', 'I': 'Í',
        'O': 'Ó', 'U': 'Ú', 'Y': 'Ý'
    }
    return mapping.get(c, c)


def accent_text(text):
    words = re.findall(r'\w+|\W+', text)
    return ''.join(add_accent(w) if w.isalpha() else w for w in words)


# =========================
# 🔽 UŻYCIE
# =========================

if __name__ == "__main__":
    with open("psalmy.txt", "r", encoding="utf-8") as f:
        text = f.read()

    result = accent_text(text)

    with open("psalmy_akcenty.txt", "w", encoding="utf-8") as f:
        f.write(result)

    print("Gotowe!")