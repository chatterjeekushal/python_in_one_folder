
# wright a python program to reverse a list of for example

my_list = [10, 11, 12, 13, 14, 15]

# Reverse the list
rev_list = my_list[::-1]

print(rev_list)



# use loop

i = len(my_list)-1

# Corrected while loop
while i >= 0:
    print(my_list[i])
    i -= 1


