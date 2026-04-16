# Tworzy plik z wszystkimi psalmami w formacie latex:
# \begin{psalmus}
# \latNPs{...}\polPs{...}%
# \latNPs{...}\polPs{...}%
# \latNPs{...}\polPs{...}%
# \end{psalmus}
#

import os

INPUT_DIR = "out"        # pliki po merge
OUTPUT_FILE = "breviary_psalter.tex"

def format_psalm(lines):
    result = []
    result.append("\\begin{psalmus}")

    for line in lines:
        line = line.strip()
        if not line:
            continue

        result.append(line)

    result.append("\\end{psalmus}\n")
    return "\n".join(result)


def main():
    psalms = []

    for i in range(1, 151):
        num = str(i).zfill(3)
        fname = os.path.join(INPUT_DIR, f"ps{num}_out.txt")

        if not os.path.exists(fname):
            print(f"⚠️ brak: {fname}")
            continue

        with open(fname, encoding="utf-8") as f:
            lines = f.readlines()

        psalm = format_psalm(lines)
        psalms.append(f"% ===== Psalm {i} =====\n" + psalm)

        print(f"✔ ps{num}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n\n".join(psalms))

    print("\n✅ Gotowy plik:", OUTPUT_FILE)


if __name__ == "__main__":
    main()