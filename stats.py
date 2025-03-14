
def count_words(book):
   count=0
   words=book.split()
   for word in words:
       count += 1 
   return (count)

def count_characters(book):
    char_counts = {}
    lower_text = book.lower()
    for char in lower_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts