from stats import get_num_words, get_num_char, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_highest_val(key):
    return 

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    contents = get_book_text(sys.argv[1])
    word_count = get_num_words(contents)
    char_count = get_num_char(contents)
    sorted_char = sort_dict(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for key in sorted_char:
        if key[0].isalpha():
            print(f"{key[0]}: {key[1]}")
    print("============= END ===============")

main()