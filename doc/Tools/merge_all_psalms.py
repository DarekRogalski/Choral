import os
import re

INPUT_DIR = "in"          # katalog z plikami
OUTPUT_DIR = "out"       # katalog wynikowy

def normalize_stars(text):
    text = text.replace("~*", "~\\red{*}")
    text = text.replace(" *", "~\\red{*}")
    return text

def merge_pair(lat_path, pl_path, out_path):
    with open(lat_path, encoding="utf-8") as f:
        lat_lines = f.readlines()

    with open(pl_path, encoding="utf-8") as f:
        pl_lines = f.readlines()

    if len(lat_lines) != len(pl_lines):
        print(f"⚠️ {os.path.basename(lat_path)}: różna liczba linii (LAT={len(lat_lines)}, PL={len(pl_lines)})")

    result = []

    for i, lat in enumerate(lat_lines):
        lat = lat.rstrip("\n")
        pl = pl_lines[i].strip() if i < len(pl_lines) else ""

        # 🔥 wstawienie do \polPs{}
        new_line = lat.replace("polPs{}", "polPs{" + pl + "}")
    

        # 🔥 poprawka - zmienia gwiazdki na makro
        new_line = normalize_stars(new_line)
        new_line = add_percent_end(new_line)

        result.append(new_line)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(result))

def add_percent_end(line):
    line = line.rstrip()
    if not line.endswith("%"):
        line += "%"
    return line

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for i in range(1, 273):
        #num = str(i).zfill(3)

        lat_file = os.path.join(INPUT_DIR, f"ps{i}_lat.txt")
        pl_file  = os.path.join(INPUT_DIR, f"ps{i}_pl.txt")
        out_file = os.path.join(OUTPUT_DIR, f"ps{i}_out.txt")

        if not os.path.exists(lat_file):
            print(f"❌ Brak: {lat_file}")
            continue

        if not os.path.exists(pl_file):
            print(f"❌ Brak: {pl_file}")
            continue

        merge_pair(lat_file, pl_file, out_file)
        print(f"✔ ps{i}")

    print("\n✅ Wszystkie możliwe psalmy połączone.")


if __name__ == "__main__":
    main()