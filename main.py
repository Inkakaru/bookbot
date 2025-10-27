# Write a new function called get_book_text.
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

# Write a main function that uses get_book_text
# with a relative path to your frankenstein.txt 
# print contents to console

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = count_words(book)
    characters = char_frequency(book)
    print(f"Found {num_words} total words")
    print(characters)

# Import the count_words function from stats.py
from stats import count_words
from stats import char_frequency
# don't change below this line (Boots magic code)
if __name__ == "__main__":
    main()

