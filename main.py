def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    print(get_book_text("./books/frankenstein.txt"))

main()