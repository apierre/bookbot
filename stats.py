def get_num_words(book_contents):
    book_contents_split = book_contents.split()
    counter = 0

    for words in book_contents_split:
        counter += 1
    return counter

def get_num_chars(book_contents):
    dictionaryCounter = {}
    for char in book_contents:
        if char in dictionaryCounter:
            dictionaryCounter[char] += 1
        else:
            dictionaryCounter[char] = 1
    return dictionaryCounter