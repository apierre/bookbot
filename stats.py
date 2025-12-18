def get_num_words(book_contents):
    book_contents_split = book_contents.split()
    counter = 0

    for words in book_contents_split:
        counter += 1
    return counter