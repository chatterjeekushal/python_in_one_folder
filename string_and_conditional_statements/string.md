

>>> num_list="0123456789"
>>> num_list[:]          
'0123456789'
>>> num_list[3:]
'3456789'
>>> num_list[:7] 
'0123456'
>>> num_list[0:7:2]
'0246'
>>> num_list[0:7:3] 
'036'
>>> num_list[-8]    
'2' 
>>> num_list[-1] 
'9' 
>>> num_list[-2:-7]
''  
>>> num_list[-2:-1] 
'8' 
>>> num_list[-2:-3] 
''  
>>> 


>>> chai="masala chai"
>>> chai
'masala chai'
>>> print(chai.lower())
masala chai
>>> print(chai.upper()) 
MASALA CHAI
>>> chai="   masala  chai"
>>> chai
'   masala  chai'
>>> print(chai.strip())
masala  chai



>>> chai="lemon chai"
>>> print(chai.replace("lemon","ginger"))
ginger chai
>>> chai   
'lemon chai'
>>> 

>>> chai="lemon , ginger , masala , mint"
>>> print(chai.split(,))
  File "<stdin>", line 1   
    print(chai.split(,))   
                     ^     
SyntaxError: invalid syntax
>>> print(chai.split(","))
['lemon ', ' ginger ', ' masala ', ' mint']
>>> 


>>> chai="masala chai"
>>> print(chai.find("chai"))
7   
>>> chai="masala chai chai chai"
>>> print(chai.count("chai))
  File "<stdin>", line 1
    print(chai.count("chai))
                     ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print(chai.count("chai"))
3   
>>> 


Type "help", "copyright", "credits" or "license" for more information.
>>> chai_type="masala"      
>>> quantity=2
>>> order="i ordered {} cups of {} chai"
>>> order
'i ordered {} cups of {} chai'
>>> print(order.format(quantity,chai_type))
i ordered 2 cups of masala chai
>>> 


>>> chai_variety=["lemon","masala","ginger"]
>>> chai_variety
['lemon', 'masala', 'ginger']
>>> print(" ".join(chai_variety))
lemon masala ginger
>>> print("-".join(chai_variety))  
lemon-masala-ginger
>>> print(", ".join(chai_variety))
lemon, masala, ginger



>> chai="he said ,\"masala chai is owo\" "
>>> chai
'he said ,"masala chai is owo" '
>>> chai="masal \n chai"
>>> chai
'masal \n chai'
>>> print(chai)
masal 
 chai 
>>> chai=r"masala/n chai"
>>> print(chai)
masala/n chai



>>> chai=r"c:\user\pwd\"
  File "<stdin>", line 1
    chai=r"c:\user\pwd\"
         ^
SyntaxError: unterminated string literal (detected at line 1)
>>> chai=r"c:\user\pwd\" 
  File "<stdin>", line 1
    chai=r"c:\user\pwd\"
         ^
SyntaxError: unterminated string literal (detected at line 1)
>>> chai=r"c:\user\pwd"   
>>> chai
'c:\\user\\pwd'
>>> chai="c:\\user\\pwd"
>>> print(chai)
c:\user\pwd
>>> 




>>> chai="masala chai"
>>> print("masala" in chai)
True
>>> print("ginger" in chai) 
False
>>> 