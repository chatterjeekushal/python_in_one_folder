
# error handiling in python

a=input("enter the number: ")

print(f"multiplication table of {a} is :")

try:

    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")

except:
    print("sory some error")

print("end of pogram")


