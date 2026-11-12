import re
from collections import Counter

POSITIVE = {"good", "clean", "fast", "helpful", "improved"}
NEGATIVE = {"bad", "dirty", "slow", "rude", "smoke", "broken"}
NEGATORS = {"not", "never", "no"}


def score(text):
    words = text.lower().replace(".", " ").replace(",", " ").split()
    total = 0
    previous = None
    for word in words:
        value = 1 if word in POSITIVE else -1 if word in NEGATIVE else 0
        if previous in NEGATORS:
            value = -value
        total += value
        previous = word
    return total


def label(text):
    value = score(text)
    return "positive" if value > 0 else "negative" if value < 0 else "neutral"


STOP = {"the", "is", "are", "a", "an", "and", "of", "to", "in", "from", "was", "were"}


def summarise(text, k=2):
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    words_by_sentence = [
        [w.lower() for w in re.findall(r"[A-Za-z]+", s)
         if w.lower() not in STOP]
        for s in sentences
    ]
    counts = Counter(w for words in words_by_sentence for w in words)
    scored = [
        (sum(counts[w] for w in words), i, sentence)
        for i, (words, sentence) in enumerate(zip(words_by_sentence, sentences))
    ]
    chosen = sorted(sorted(scored, key=lambda x: (-x[0], x[1]))[:k], key=lambda x: x[1])
    return " ".join(item[2] for item in chosen)


if __name__ == "__main__":
    for complaint in [
        "Roads are clean and the bus was fast.",
        "Smoke from the factory, air is bad.",
        "The staff were not helpful.",
        "Not bad, service improved."
    ]:
        print(f"{label(complaint):8} | {complaint}")
