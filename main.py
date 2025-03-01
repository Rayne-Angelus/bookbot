from stats import get_num_words
from stats import count_chars
from stats import sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) == 2:
        book = get_book_text(sys.argv[1])
        number_of_words = get_num_words(book)
        chars_by_type = count_chars(book)
        sorted_chars_by_type = sort_dict(chars_by_type)
        print(f"Found {number_of_words} total words")
        for i in sorted_chars_by_type:
            key_value = list(i.keys())[0]
            if key_value.isalpha():
                print(f"{key_value}: {i[key_value]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
