import re

def merge_files(lat_file, pl_file, out_file):
    with open(lat_file, encoding="utf-8") as f:
        lat_lines = f.readlines()

    with open(pl_file, encoding="utf-8") as f:
        pl_lines = f.readlines()

    if len(lat_lines) != len(pl_lines):
        print("⚠️ Różna liczba linii!")
        print("LAT:", len(lat_lines), "PL:", len(pl_lines))

    result = []

    for i, lat in enumerate(lat_lines):
        lat = lat.rstrip("\n")

        # jeśli nie ma polskiej linii → zostaw pustą
        pl = pl_lines[i].strip() if i < len(pl_lines) else ""

        # 🔥 zamiana \polPs{}
        new_line = re.sub(
            r'\\polPs\{\}',
            f'\\polPs{{{pl}}}',
            lat
        )

        result.append(new_line)

    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(result))

    print("✅ Gotowe:", out_file)


if __name__ == "__main__":
    merge_files("ps001_lat.txt", "ps001_pl.txt", "ps001_out.txt")