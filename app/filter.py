from better_profanity import profanity
import re
from .badwords_loader import load_malayalam_badwords

profanity.load_censor_words()
MALAYALAM_BADWORDS = load_malayalam_badwords()
malayalam_pattern = re.compile("|".join(re.escape(word) for word in MALAYALAM_BADWORDS), re.IGNORECASE)

def is_clean(text: str):
    if profanity.contains_profanity(text):
        return False, "English abusive content detected"
    if malayalam_pattern.search(text):
        return False, "Malayalam abusive content detected"
    return True, "Clean message"
