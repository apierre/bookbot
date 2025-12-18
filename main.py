def main():
    fd  = "books/frankenstein.txt"
    text = get_book_text(fd)
    number_of_words = get_book_words(text)
    msg = f"Found {number_of_words} total words"
    print(msg)
 
def get_book_text(path):
    file_content = None
    with open(path) as f:
        file_content = f.read()        
    return file_content

def get_book_words(book_contents):
    book_contents_split = book_contents.split()
    counter = 0

    for words in book_contents_split:
        counter += 1
    return counter


main()