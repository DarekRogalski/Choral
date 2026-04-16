from compare_with_reference import show_differences

# 🔹 plik referencyjny (LU / Vulgata)
with open("ps001_ref.txt", encoding="utf-8") as f:
    ref = f.read()

# 🔹 Twój wynik
with open("ps001_out.txt", encoding="utf-8") as f:
    test = f.read()

show_differences(ref, test)