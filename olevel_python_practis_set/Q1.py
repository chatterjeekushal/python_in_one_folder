

# wright a python function that takes a string as parameter and retuns a string with every successive repetitive character replaced by & e.g parameter may become par&met&&



def convert(string):
    ch = ""  # Initialize ch inside the function
    for i in string:
        if i not in ch:
            ch += i
        else:
            ch += '&'
    return ch

result = convert("parameter")
print(result)




