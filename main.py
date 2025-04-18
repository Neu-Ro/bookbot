from stats import get_book_text
from stats import number_of_words
from stats import key_for_letters
from stats import number_of_characters
from stats import letter_count_organizer
import sys

if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book = get_book_text(str(sys.argv[1]))
    word_count = number_of_words(book)
    string_count = number_of_characters(book)
    report = letter_count_organizer(string_count)



    print("============ BOOKBOT ============")
    print("Analyzing book...")
    print("----------- Word Count ----------")
    print("Found", word_count ,"total words")
    print("--------- Character Count -------")
    for pair in report:
        print(pair["letter"],": ",pair["count"], sep="")
    print("============= END ===============")