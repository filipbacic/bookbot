def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    return len(text.split())

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = count_words(book_text)
    print("{num_words} words found in the document".format(num_words=str(word_count)))

main()