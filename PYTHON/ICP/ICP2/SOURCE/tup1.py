numbers = input("Enter numbers : ") # you can add str(input()) method
my_list = numbers.split(",")
my_tuple = tuple(my_list)
print("your list is ", my_list)
print("(",my_tuple[0],",",my_tuple[-1],")")