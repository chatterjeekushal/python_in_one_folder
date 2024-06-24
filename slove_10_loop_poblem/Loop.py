





# 1. Counting Positive Numbers
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# positive_number_count=0

# for num in numbers:
#     if(num>0):
#         print(num)
#         positive_number_count+=1
# print("final count of positive number is",positive_number_count)







# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n


# n=10

# sun_even=0

# for i in range(1,n+1):
#     if(i%2==0):
#         sun_even=sun_even+i
# print("sum of even number is ",sun_even)




# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

n=2

table=0

for t in range(1,11):
    if(t==5):
        t=8
        continue
    
    print(n,"x",t,"=",n*t)





# 4. Reverse a String
# Problem: Reverse a string using a loop.


name="kushal"

# print(name[5])
# print(name[4])
# print(name[3])
# print(name[2])
# print(name[1])
# print(name[0])

# name=input("enter your string")


# i=len(name)-1


# while i>=0:
#     print(name[i])
#     i-=1






# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

# input_str="teeter"

# for char in input_str:
#     if (input_str.count(char)==1):
#         print("char is ",char)
#         break








# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.


# fac_n = 6
# fac_res = 1

# while fac_n >0:
#     fac_res *= fac_n
#     fac_n -= 1

# print(fac_res)







# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.


# while True:
#     number=int(input("enter value 1 and 10 :"))
#     if(1<=number <=10):
#         print("thanks")
#         break
#     else:
#         print("invalid number try agin")







# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate


items = ["apple", "banana", "orange", "apple", "mango"]

for item in items:
    if(items.count(item)):
        print("your duplcate item is ",item)
        break
    else:
        print("your item is ",item)


# # prosses2

# uniqye_item=set()

# for item in items:
#     if item in uniqye_item:
#         print("duplicate",item)
#         break
#     uniqye_item.add(item)





#resive the duplicate value

myset=("kushal","rana","kushal")




for item in myset:
    if(myset.count(item)):
        print("your duplcate item is ",item)
        break
    else:
        print("your item is ",item)



