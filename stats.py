def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    num_chars = {}
    for char in text.lower():
        num_chars[char] = num_chars.get(char, 0) + 1
    return num_chars

def sort_on(dict):
    return dict["count"]

def sort_dict_by_num(dict):
    dict_list = []
    for key in dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["count"] = dict[key]
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list