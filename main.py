def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    def word_count(file_contents):
        words = file_contents.split()
        i = 0
        for w in words:
            i+=1
        return i
    i = word_count(file_contents)
    

main()
