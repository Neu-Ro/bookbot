def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
        return(file_contents)

def number_of_words(complete_book):
    split = complete_book.split()
    return(len(split))

def number_of_characters(complete_book):
    letters_list = list(complete_book)
    characters = {}
    
    for letter in letters_list:
        lowercase_letter = letter.lower()
        if lowercase_letter in characters:
            characters[lowercase_letter] = characters[lowercase_letter]+1
        else:
            characters[lowercase_letter] = 1

    return(characters)

def key_for_letters(value):
    return(value["count"])

def letter_count_organizer(letter_count):
    
    sorted_letter = []

    for x, y in letter_count.items():
        if x.isalpha():
            sorted_letter.append({"letter":x,"count":y})

    sorted_letter.sort(reverse=True, key=key_for_letters)

    return(sorted_letter)