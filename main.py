
def get_book_text(path):
    with open(path) as book:
        return (book.read())

def main ():
    r_path="books/frankenstein.txt"
    print(get_book_text(r_path))
    
if __name__ == "__main__":
    main()
