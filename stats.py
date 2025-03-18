
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

def sort_dict(dict):
    # create a list of dictionaries
    list =[]
    for char, count in dict.items():
        list.append({"char":char, "count":count})
    #sort the list of dictionaries 
    list.sort(reverse=True, key=lambda x: x['count'])   
    return list