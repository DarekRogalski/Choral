# projekt/
# │
# ├── latin_accentor.py
# ├── psalter_tool.py
# │
# ├── psalms_raw/
# │   ├── ps001.txt
# │   ├── ps002.txt
# │   ├── ...
# │   └── ps150.txt
# │
#└── psalms_accented/
#
# użycie:
# python psalter_tool.py

import os
from latin_accentor import accent_text

INPUT_DIR = "psalms_raw"
OUTPUT_DIR = "psalms_accented"

def process_all():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for filename in sorted(os.listdir(INPUT_DIR)):
        if not filename.endswith(".txt"):
            continue

        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename)

        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()

        accented = accent_text(text, pedagogical=True)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(accented)

        print(f"✔ {filename}")

    print("\n✅ Gotowe — cały Psałterz przetworzony.")


if __name__ == "__main__":
    process_all()