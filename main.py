
import sys 

from stats import word_counter
from stats import characters_counter,sorted_report

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)

    count = word_counter(text)
    characters = characters_counter(text)
    report = sorted_report(characters)



    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char, freq in report:
        print(f"{char}: {freq}")

    

main()
