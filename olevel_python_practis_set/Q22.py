

# wright a program to print all armstong numbers in a given range note : an aramstrong number is a number is a number who sum of cubes of digits is qual to the number itself

# Take input from the user
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

# Loop through the range
for num in range(lower, upper + 1):
    order = len(str(num))  # Get the number of digits in the number
    sum = 0
    temp = num
    
    while temp > 0:
        digit = temp % 10  # Get the last digit
        sum += digit ** order  # Raise it to the power of the number of digits and add to sum
        temp //= 10  # Remove the last digit
    
    # Check if the number is an Armstrong number
    if num == sum:
        print(num)  # Print the Armstrong number


