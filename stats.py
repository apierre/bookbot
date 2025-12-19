def get_num_words(book_contents):
    book_contents_split = book_contents.split()
    counter = 0

    for words in book_contents_split:
        counter += 1
    return counter

def get_num_chars(book_contents):
    dictionaryCounter = {}

    for char in book_contents.lower():
        if char in dictionaryCounter:
            dictionaryCounter[char.lower()] += 1
        else:
            dictionaryCounter[char.lower()] = 1
    return dictionaryCounter



def sort_on(items):
    charCountList = []

    for char in items:
        if char.isalpha():
            charCountList.append({"char":char, "num":items[char]})
    
    charCountList.sort(reverse=True, key=helper_sort)
    return charCountList

def helper_sort(items):
    return items["num"]