from stats import get_num_words

def main():
    fd  = "books/frankenstein.txt"
    text = get_book_text(fd)
    number_of_words = get_num_words(text)
    msg = f"Found {number_of_words} total words"
    print(msg)
 
def get_book_text(path):
    file_content = None
    with open(path) as f:
        file_content = f.read()        
    return file_content

main()