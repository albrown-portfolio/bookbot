from stats import count_words
from stats import count_characters
from stats import sort_dict

def get_book_text(path):
    with open(path) as book:
        return (book.read())

def print_counts(dict_list):
    for item in dict_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")

def main ():
    book_path="books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dic = count_characters(text)
    dict_list = sort_dict(char_dic)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_counts(dict_list)
    print("============= END ===============")
main()