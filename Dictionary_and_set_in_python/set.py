



colaction={1,2,3,4,5,"hello","world","world",7}

print(colaction)
print(type(colaction))
print(len(colaction))



# syntax to create emty set

emty_set= set()

print(type(emty_set))


# set mathod

emty_set.add(3) # add element in set
emty_set.add(5)
emty_set.add(3)
emty_set.add(7)

emty_set.remove(7) #remove element in set

emty_set.clear() # clear all set element

print(emty_set)



element={"hello",76,89,(23,76,87)}

print(element.pop()) # return random set element
print(element.pop())



# set union mathod in python

# set union mathod join two set but deplicate set value not count and print

set1={1,2,3,4}
set2={4,5,6,7}

print(set1.union(set2))





# set intersection mathod in python

# set intersection mathod print the comon element betwin two set

set1={1,2,3,4}
set2={4,5,6,7}

print(set1.intersection(set2))





# practis set

# you are given a list of student assume one clasroom is required for 1 subject how many classroom are nedded by all

classromm={"python","java","python","javascript","java","python","java","c++","c"}

print(len(classromm))




