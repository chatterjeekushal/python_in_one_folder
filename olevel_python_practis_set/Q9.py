
#wright a program to test whether a passed letter is vowel or not

char=input("enter char: ")

vow=["a","e","i","o","u","A","E","I","O","U"]

if char in vow:
    print(f"the charactor {char} is vowel")
else:
    print(f"the charactor {char} is  not vowel")