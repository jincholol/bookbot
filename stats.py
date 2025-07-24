def get_num_words(text):

    word_list = (text.split())
    get_num = len(word_list)
    return get_num

def get_char_count(text):

    text_count = {}
    for char in text:
        char = char.lower()
        if char in text_count:
            text_count[char] += 1
        else:
            text_count[char] = 1
    return text_count

def sort_report(items):
    return items["num"]

def sorted_dictionaries(char_count):

    collect_dicts = []
    for char, count in char_count.items():
        new_dict = {"char": char, "num":count}
        collect_dicts.append(new_dict)
    collect_dicts.sort(reverse=True, key=sort_report)
    return collect_dicts
    

