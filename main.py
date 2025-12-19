from stats import get_num_words, get_num_chars, sort_on
import sys


def main():
    if len(sys.argv) != 2:
        msg = f"Usage: python3 main.py <path_to_book>"
        print(msg)
        sys.exit(1)
    
    fd = sys.argv[1]
    text = get_book_text(fd)
    number_of_words = get_num_words(text)
    myDict = get_num_chars(text)
    rptDict = sort_on(myDict)

    report(fd, number_of_words, rptDict)
 
def get_book_text(path):
    file_content = None
    with open(path) as f:
        file_content = f.read()
    return file_content


def report(relative_path, word_count, rpt_dict):
    msg = f"============ BOOKBOT ============"
    print(msg)
    msg = f"Analyzing book found at {relative_path}..."
    print(msg)

    msg = f"----------- Word Count ----------"
    print(msg)
    msg = f"Found {word_count} total words"
    print(msg)

    msg = f"--------- Character Count -------"
    print(msg)

    for record in rpt_dict:
        msg = f"{record["char"]}: {record["num"]}"
        print(msg)
    
    msg = f"============= END ==============="
    print(msg)
    return

main()