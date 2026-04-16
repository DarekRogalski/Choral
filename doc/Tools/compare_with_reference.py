import re

def normalize(text):
    return (
        text
        .replace("æ", "ae")
        .replace("Æ", "Ae")
        .replace("œ", "oe")
        .replace("Œ", "Oe")
    )

def tokenize(text):
    text = normalize(text)
    return re.findall(r"[^\W\d_]+", text, re.UNICODE)

def show_differences(ref, test):
    ref_words = tokenize(ref)
    test_words = tokenize(test)
    ref_words = [w.lower() for w in ref_words]
    test_words = [w.lower() for w in test_words]

    max_len = min(len(ref_words), len(test_words))
    errors = 0

    for i in range(max_len):
        # if ref_words[i] != test_words[i]:
        #     print(f"\033[91m{i}: REF={ref_words[i]:<15} | TWOJE={test_words[i]}\033[0m")
        #     errors += 1
        if ref_words[i] != test_words[i]:
            if ref_words[i].lower() == test_words[i].lower():
                print(f"{i}: ⚠️ tylko akcent → REF={ref_words[i]} | TWOJE={test_words[i]}")
            else:
                print(f"{i}: ❌ inne słowo → REF={ref_words[i]} | TWOJE={test_words[i]}")

    # brakujące słowa
    if len(ref_words) != len(test_words):
        print("\n⚠️ Różna liczba słów!")
        print("REF:", len(ref_words), " TWOJE:", len(test_words))

    print(f"\n❌ Liczba różnic: {errors}")