def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print(get_book_text("/home/grimmtyr/workspace/github.com/Grimmtyr/bookbot/books/frankenstein.txt"))

main()