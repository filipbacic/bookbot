from stats import get_num_words, get_num_chars, sort_dict_by_num

def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    num_chars_sorted = sort_dict_by_num(num_chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at {path}...".format(path=book_path))
    print("----------- Word Count ----------")
    print("Found {count} total words".format(count=word_count))
    print("--------- Character Count -------")
    for dict in num_chars_sorted:
        char = dict["char"]
        if char.isalpha():
            print("{char}: {count}".format(char=char, count=dict["count"]))
    print("============= END ===============")


main()