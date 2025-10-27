# write a new function that accepts text from the book  as a string
# and returns the number of words in the string

# move this function out from main.py to stats.py

def count_words(book_text):
    words = book_text.split()
    return len(words)

# Add a new function that takes a string and returns
# the number of times each character (including symbols and spaces) appears in the string

def char_frequency(book_text):
    frequency = {}
    for char in book_text.lower():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# write a new function that takes the dictionary of characters and their counts
# and returns a sorted list of dictionaries
def sort_on(items):
    return items["num"]

def numerical_sort(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    char_list.sort(key=sort_on, reverse=True) 

    return char_list
    