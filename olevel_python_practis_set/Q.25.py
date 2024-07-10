
# wright a program to count the number occurrence of a specific character in a string

mY_str = "nielit"

get_str = ""
get_count = 1

for text in mY_str:
    if text in get_str:
        print(text,mY_str.count(text))
        
    else:
        get_str += text


    