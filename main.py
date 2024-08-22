def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    def word_count(file_contents):
        words = file_contents.split()
        i = 0
        for w in words:
            i+=1
        return i
    
    def letter_count(file_contents):
        lowered = file_contents.lower()
        count = {}
        for l in lowered:
            if l.isalpha() == True:
                count[l] = count.get(l, 0) + 1
                # loop over count and add each key into a new list. {"alpha": c, "count" = count of num}
                # sort by num
        return count
    
    def sort_letters(count):
        sorted_char = []
        
        for c in count:
            sorted_char.append({"letter": c, "val": count[c]})
        print(sorted_char)


        
    def printout(wc,chars):
        print(f'frankenstein has {wc} words.\n {chars.sort(reverse=True, key=sort_on)}')
    
    chars = letter_count(file_contents)
    wc = word_count(file_contents)
    
    printout(wc,chars)
    

main()
