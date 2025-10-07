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

def sort_on(items):
    return items["num"]

    
def convert_dict(dictonary):
    dict_list = []
    for k, v in dictonary.items():
        if not k.isalpha():
            continue
        dict_list.append({"char" : k, "num" : v})
        dict_list.sort(reverse=True, key=sort_on)
    return dict_list