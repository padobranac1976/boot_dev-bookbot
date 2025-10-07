def count_words(text):
    words = text.split()
    return len(words)

def char_stats(text):
    stats = {}
    for c in text.lower():
        if c in stats:
            stats[c] += 1
        else:
            stats[c] = 1
    return stats