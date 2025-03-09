from stats import get_num_words

def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_num_words(book_text)
    print("{num_words} words found in the document".format(num_words=str(word_count)))

main()