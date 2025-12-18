from stats import get_num_words, get_num_chars

def main():
    fd  = "books/frankenstein.txt"
    text = get_book_text(fd)
    number_of_words = get_num_words(text)
    myDict = get_num_chars(text)
    msg = f"Found {number_of_words} total words"
    
    print(msg)
    print(myDict)

 
def get_book_text(path):
    file_content = None
    with open(path) as f:
        file_content = f.read()        
    return file_content

main()