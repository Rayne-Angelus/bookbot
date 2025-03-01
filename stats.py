def get_num_words(book_text):
    num_words = book_text.split()
    return len(num_words)

def count_chars(book_text):
    char_counts = {}
    for i in book_text:
        i = i.lower()
        if i in char_counts:    
            char_counts[i] = char_counts[i] + 1
        else:
            char_counts[i] = 1
    return char_counts

def sort_on(dict_item):
    return list(dict_item.values())[0]

def sort_dict(dictionary):
    sorted_list = []
    for i in dictionary:
        sorted_list.append({i: dictionary[i]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list