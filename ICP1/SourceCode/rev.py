def reverse(S1):
  str = ""
  for i in S1:
    str = i + str
  return str
 
S1 = input("Input a string:")
 
print ("The original string  is : ",end="")
print (S1)
 
print ("The reversed string is : ",end="")
print (reverse(S1))