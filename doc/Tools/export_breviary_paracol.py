import os
import re

INPUT_DIR = "out"
OUTPUT_FILE = "breviary_psalter.tex"

def split_lat_pol(line):
    m = re.match(r'\\latNPs\{(.*?)\}\\polPs\{(.*?)\}%?', line)
    if not m:
        return None, None
    return m.group(1), m.group(2)

def format_psalm(lines, num):
    result = []

    result.append(f"% ===== Psalm {num} =====")
    result.append("\\begin{psalmus}")
    result.append("\\begin{paracol}{2}")

    for line in lines:
        line = line.strip()
        if not line:
            continue

        lat, pl = split_lat_pol(line)

        if lat is None:
            continue

        result.append(f"\\latNPs{{{lat}}}%")
        result.append("\\switchcolumn")
        result.append(f"\\polPs{{{pl}}}%")
        result.append("\\switchcolumn*")

    result.append("\\end{paracol}")
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

        psalm = format_psalm(lines, i)
        psalms.append(psalm)

        print(f"✔ ps{num}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n\n".join(psalms))

    print("\n✅ Gotowy plik:", OUTPUT_FILE)


if __name__ == "__main__":
    main()