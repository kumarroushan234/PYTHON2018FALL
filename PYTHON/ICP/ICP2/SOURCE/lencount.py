def main():
    fname = input("Enter filename: ")
    infile=open(fname, 'r')

    numLines = numWords = numChars = 0
 
    for line in infile:
        line = line.replace('\n', '')
        words = line.split()
        numLines += 1 - line.count(' ')
        numWords += len(words) 
        numChars += len(line) - line.count(' ')
    print("Lines: ", numLines)
    print("Words: ", numWords)
    print("Characters: ", numChars)
        
        
main()
