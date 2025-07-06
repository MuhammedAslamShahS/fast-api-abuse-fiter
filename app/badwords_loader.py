import os

def load_malayalam_badwords(filepath="app/malayalam_badwords.txt"):
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
