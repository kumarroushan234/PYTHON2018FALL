
# fout = open(r'C:\Users\sri.motipalli\Downloads\out.txt', 'w')
with open(r'C:\Users\navya\python\f2.txt') as f2:
    f2_text = f2.read()
    exclude = set(f2_text.lower().split()) # Get all the the words from file2 and also convert them to lower case
    print(exclude)

tmp = []
# Store all the lines from file1 in a tmp list
with open(r'C:\Users\navya\python\f1.txt', "r") as f:
    for line in f:
        tmp.append(line)

# Now open file1 in write mode so that the content present in file1 can be over written
fout = open(r'C:\Users\navya\python\f1.txt', "w")
for line in tmp:
    list_of_words = line.split()
    for word in list_of_words:
        if word.lower() not in exclude: # If the word is not present in file2, write the word to file1
            fout.write(word)
            fout.write(' ') # Give a space between every word
    fout.write('\n') # This is to generate new line

f.close()
