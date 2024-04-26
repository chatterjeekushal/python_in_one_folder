
# poblem 1

# . Age Group Categorization

# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).


# age= int( input("enter your age :"))

# if(age<13):
#     print("you are child")
# elif(age >=13 and age<=19):
#     print("you are teenager")
# elif(age>=20 and age<=59):
#     print("you are adult")
# elif(age>=60):
#     print("you are senior")
# else:
#     print("500 pogram error")



# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.


# perage=25
# day="wednesday"

# price=12 if perage>=18 else 8

# if (day=="wednesday"):
#     price=price-2

# print("tikit price is ",price)



# #3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

# marks=int(input("enter your marks :"))

# if(marks>=101):
#     print("plese enter valid number")
#     exit()

# if(marks>=90 and marks<=100):
#     print("grade A")
# elif(marks>=80 and marks<=89):
#     print("GRADE B")
# elif(marks>=70 and marks<=79):
#     print("grade c")
# elif(marks>=60 and marks <=69):
#     print("grade D")
# else:
#     print("grade F")







# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe



# banana=input("enter fruit color :")

# if(banana=="green"):
#     print("unripe")
# elif(banana=="yellow"):
#     print("ripe")
# elif(banana=="brown"):
#     print("overripe")
# else:
#     print("enter valid color")




# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).


# weather=input("enter weather day :")

# if(weather=="sunny"):
#     print("go for a walk")
# elif(weather=="rainy"):
#     print("read a book")
# elif(weather=="snowy"):
#     print("bild a show man")
# else:
#     print("i have no data for this weather")





# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).




# distance=float(input("enter your distance :"))

# if(distance<3):
#     print("walk")
# elif(distance<=15):
#     print("bike")
# else:
#     print("car")



# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

# password=input("enter your password :")

# if(len(password)<6):
#     print("weak")
# elif(len(password)<=10):
#     print("medium")
# else:
#     print("strong")