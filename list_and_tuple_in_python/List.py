

marks=[94.4,87.5,95.5,66.4,45.1]

print(marks)

print(type(marks))

#print list item by index

print(marks[0])

print(len(marks))

student=["karan",85,"delhi"]

print(student)
print(student[2])

student[0]="arjun"

print(student)

marks2=[87,64,33,95,76]

print(marks2[1:4]) #[64,33,95]

print(marks2[-3:-1]) #[33,95]


list=[2,1,3]

list.append(4)

print(list)

list2=[6,8,5]

list2.sort()

print(list2)

list3=[5,2,7]

list3.sort(reverse=True)

print(list3)

list4=[5,2,7]

list4.reverse()

print(list4)

list5=[9,4,1]

list5.insert(1,6)

print(list5)

list6=[78,76,45]

list6.remove(76)

print(list6)

list7=[78,76,45]

list7.pop(1)

print(list7)



# practis set

# user1=input("enter your name")

# user2=input("enter your name")

# user3=input("enter your name")

# student=[user1,user2,user3]


# print(student)



palindrom=[1,2,3,2,1]

palindrom1=palindrom.copy()

palindrom1.reverse()

if(palindrom1==palindrom):
    print("palindrom true")

else:
    print("palindrom false")




# loop in list

my_list_data=[1,7,8,4,76]

for data in my_list_data:
    print(f" my data {data}")
    
    

i=0

while i<len(my_list_data):
    print(f"{i} and {my_list_data[i]}")
    i+=1
