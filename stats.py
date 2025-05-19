
def get_words(contents):
    return contents.split()

def get_word_count(word_list):
    return len(word_list)

def get_num_words(file_contents):
    words = file_contents.split()
    return get_word_count(words)

def get_num_char(file_contents):
    contents = file_contents.lower()
    char_count = {}
    for char in contents:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_dict(dict):
    return sorted(dict.items(), key=lambda x:x[1], reverse=True)