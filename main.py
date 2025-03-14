from stats import count_words
from stats import count_characters

def main ():
    book_path="books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dic = count_characters(text)
    print(f"{num_words} words found in the document")
    print(char_dic)

def get_book_text(path):
    with open(path) as book:
        return (book.read())


main()