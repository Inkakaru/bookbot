# Write a new function called get_book_text.
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

# Write a main function that uses get_book_text
# with a relative path to your frankenstein.txt 
# print contents to console

#final challenge: remove hardcoded book paths
#at the start of main.py import the built-in sys module
# modify get_book_text to accept a file path argument

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book= get_book_text(sys.argv[1])
    num_words = count_words(book)
    characters = char_frequency(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_characters = numerical_sort(characters)

    for x in sorted_characters:
        char =x['char']
        num = x['num']
        print(f"{char}: {num} \n")
    print("============= END ===============")

# Import the count_words function from stats.py
from stats import count_words
from stats import char_frequency
from stats import numerical_sort
# don't change below this line (Boots magic code)
if __name__ == "__main__":
    main()

