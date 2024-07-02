
# python program to find ascii  value of character

char=input("enter the char: ")

if len(char) < 1:
     print("Please enter exactly one character.")
else:
    # Find the ASCII value
    ascii_value=ord(char)
    
    # Print the ASCII value
    print(f"The ASCII value of '{char}' is {ascii_value}.")