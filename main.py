def main():
    fd  = "books/frankenstein.txt"
    text = get_book_text(fd)
 
def get_book_text(path):
    with open(path) as f:
        print(f.read())

main()
