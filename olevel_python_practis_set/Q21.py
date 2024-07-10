
# wright a python program to show the character and count to its repetition count repeated characters in a string


string='jhcdgvdytcdygzdbcvxhcfssdrftydcfszdcgszfvcdzcfgszytrsgvd'

dict={}

for char in string:
    if(char in dict.keys()):
        dict[char]+=1
    else:
        dict[char]=1

        
for k ,v in dict.items():
    print(k,'=>',v)



