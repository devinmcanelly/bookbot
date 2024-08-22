with open("books/frankenstein.txt") as f:
        file_contents = f.read() ## Open book and load it into a variable.

def letter_count(file_contents):
    '''
    Takes a given string, and returns a dictionary containing {letter: count} where count is the number of times
    that character appears in the text, and the len() for a word count.
    '''
    lowered = file_contents.lower()
    count = {}
    for l in lowered:
        if l.isalpha():
            count[l] = count.get(l, 0) + 1
    sorted = []
    for c in count:
        sorted.append({"letter": c, "val": count[c]})
    
    def sort_on(item):
        return item["val"]
    
    sorted.sort(reverse=True, key=sort_on)
    return sorted, len(lowered.split())


def printout(wc,chars):
    line = "================================================================================\n"
    short_line = "==============="
    print(line + f'frankenstein has {wc} words.\n' + short_line + short_line )
    for c in chars:
        print(f'{c["letter"]} was used {c["val"]} times')
        print(short_line)



def main():
    chars, wc = letter_count(file_contents)
    printout(wc,chars)


main()
