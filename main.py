with open("books/frankenstein.txt") as f:
        file_contents = f.read() ## Open book and load it into a variable.

def word_count(file_contents):
    ''' 
    Takes a given string (file_contents) and returns the word count as an int. 
    '''
    words = file_contents.split()
    i = 0
    for w in words:
        i+=1
    return i


def letter_count(file_contents):
    '''
    Takes a given string, and returns a dictionary containing {letter: count} where count is the number of times
    that character appears in the text.
    '''
    lowered = file_contents.lower()
    count = {}
    for l in lowered:
        if l.isalpha() == True:
            count[l] = count.get(l, 0) + 1
    return count

def sort_letters(count):
    '''
    This should probably just be what letter_count returns.
    It's a list of dictionaries like [{"letter": a, "val": 1234 }, ...] where val is the character count.
    '''
    sorted_char = []
    for c in count:
        sorted_char.append({"letter": c, "val": count[c]})
    
    def sort_on(item):
        return item["val"]
    
    sorted_char.sort(reverse=True, key=sort_on)
    return sorted_char


def printout(wc,chars):
    line = "================================================================================\n"

    print(f'frankenstein has {wc} words.\n' + line )
    print(f'{chars}')



def main():
    wc = word_count(file_contents)
    chars = letter_count(file_contents)
    chars_sorted = sort_letters(chars)
    printout(wc,chars_sorted)


main()
