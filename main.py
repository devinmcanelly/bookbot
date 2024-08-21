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
        return count
    
    # def sort(count):
    #     return count[]
    letters = letter_count(file_contents)
    words = word_count(file_contents)
    print(letters)
    

main()
