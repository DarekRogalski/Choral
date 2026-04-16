import os
import re

INPUT_DIR = "out"
OUTPUT_FILE = "breviary_psalter.tex"

def split_lat_pol(line):
    m = re.match(r'\\latNPs\{(.*?)\}\\polPs\{(.*?)\}%?', line)
    if not m:
        return None, None
    return m.group(1), m.group(2)

def extract_initial(text):
    m = re.match(r'([A-Za-zÁÉÍÓÚÝáéíóúý])(.+)', text)
    if not m:
        return text
    first, rest = m.groups()
    return f"\\initium{{{first}}}{rest}"

def format_psalm(lines, num):
    result = []
    result.append("\\sloppy")
    result.append(f"% ===== Psalm {num} =====")
    result.append(f"\\rubrica{{Psalmus {num}}}")

    result.append("\\begin{paracol}[1.15]{2}")

    first = True

    for line in lines:
        line = line.strip()
        if not line:
            continue

        lat, pl = split_lat_pol(line)
        if lat is None:
            continue

        if first:
            lat = extract_initial(lat)
            first = False

        result.append(f"\\latNPs{{{lat}}}%")
        result.append("\\switchcolumn")
        result.append(f"\\polPs{{{pl}}}%")
        result.append("\\switchcolumn*")

    result.append("\\end{paracol}")
    result.append("\\medskip\n")

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

    print("\n✅ LU gotowe:", OUTPUT_FILE)

if __name__ == "__main__":
    main()