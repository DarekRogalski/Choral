# Dodaje akcenty jeśli funkcja accent_text jest odkomentowana i usuwa numery wersów - f. remove_verse_numbers
# projekt/
# │
# ├── accentor_core.py        ← silnik
# ├── psalter_pipeline.py     ← przetwarzanie 150 psalmów
# ├── vulgate_dict.py         ← SŁOWNIK (klucz!)
# ├── validator.py            ← kontrola jakości
# │
# ├── psalms_raw/
# └── psalms_out/
#
# użycie:
# python psalter_tool.py

import os
from accentor_core import accent_text, remove_verse_numbers

IN_DIR = "texty_in"
OUT_DIR = "texty_out"

def run():
    os.makedirs(OUT_DIR, exist_ok=True)

    for f in sorted(os.listdir(IN_DIR)):
        if not f.endswith(".txt"):
            continue

        with open(os.path.join(IN_DIR, f), encoding="utf-8") as file:
            txt = file.read()

        #out = remove_verse_numbers(txt)
        out = accent_text(txt)

        with open(os.path.join(OUT_DIR, f), "w", encoding="utf-8") as file:
            file.write(out)

        print("✔", f)

    print("\n✅ Numery usunięte!")

def verify(ref, generated):
    if ref == generated:
        print("✅ IDENTYCZNE Z LU")
    else:
        print("❌ RÓŻNICE WYKRYTE")

if __name__ == "__main__":
    run()