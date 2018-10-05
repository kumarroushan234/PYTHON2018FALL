s = input("enter a string of your choice: ")
while s != "":
    string_len = len(s)
    ch = s[0]
    s = s.replace(ch, "")
    string_len1 = len(s)
    if string_len1 == string_len-1:
        print(ch)
        break
else:
    print("invalid input")