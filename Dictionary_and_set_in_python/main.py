


# dict={

#     "key":"value",
#     "name":"kushal",
#     "learning":"python",
# "age":19,
# "is_adult":True,
# "marks":[67,98,34]
# }


# print(dict)

# print(type(dict))


#  # print dict value by his key
# print(dict["name"]) 
# print(dict["age"]) 


# # change key value

# dict["name"]="rana"

# # create new key value

# dict["suremane"]="chatterjee"

# print(dict)



# # create null dict

# null_dict={}

# null_dict["code"]="java"

# print(null_dict)





student={

    "name":"rahul kumar",
    "subject":{

        "phy":97,
        "chem":98,
        "math":90,

    }


}


# print(student[0])

print(student.keys())

# type casting into list

print(list(student.keys()))


# length of ditci

print(len(student))


# return student values

print(student.values())


# returns all key value paire as tuples

print(student.items())


#returns the key according to value

print(student.get("name"))


# returns the specified items to the Dictionary

student.update({"city":"kolkata"})

print(student)








# practic set



my_dict={

    "table":["a price of furntiture","list of facts and figures"],
    "cat":"a small animal"
}

print(my_dict)


# wap to enter marks of 3 subject from the user and store them in a dictionary start with an emty dictionary and add one by one use subject name as key and marks as value


dict2={}

key=input("enter your key")
value=input("enter your value")
dict2.update({key:value})


print(dict2)




















