S1 = input("Input a string:")
d=l=0
for c in S1:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Total no of Letters=", l)
print("Total no of Digits=", d)
