from accentor_core import accent_word

TESTS = {
    "stetit": "stétit",
    "sedit": "sédit",
    "nocte": "nócte",
    "via": "vía",
    "omnia": "ómnia",
}

def run():
    errors = 0

    for word, good in TESTS.items():
        out = accent_word(word)
        if out != good:
            print("❌", word, out, "≠", good)
            errors += 1
        else:
            print("✔", word)

    print("\nBłędy:", errors)

if __name__ == "__main__":
    run()