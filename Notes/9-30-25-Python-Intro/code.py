# In-class programs
# Rykir Evans

#####################################################
### Program 1 - Print sum from 1 to input number ####
#####################################################
num = int(input("Please enter a number: "))
sum = 0

for i in range(1, num + 1):
    sum += i

print(sum)

########################################################
### Program 2 - Print positive/negative/0 for input ####
########################################################
num1 = int(input("Please enter an integer number: "))

if num1 < 0:
    print("Negative number")
elif num1 > 0:
    print("Positive number")
else:
    print("Number is 0")

########################################################
### Program 3 - Print 1 to num along with square    ####
########################################################
num2 = int(input("Please enter an integer number: "))

for i in range(1, num2 + 1):
    print(i, pow(i, 2))

########################################################
### Program 4 - First and last name question        ####
########################################################
fname = input("Please enter your first name: ")
lname = input("Please enter your last name: ")

if fname == lname:
    print("Wow, your first name is the same as your last name!")
else:
    print(f"Nice to meet you {fname} {lname}!")

########################################################
### Program 5 - Pizza Party Math                    ####
########################################################

people = int(input("Please enter the number of people coming to the party: "))
pizzas = int(input("Please enter the number of pizzas being ordered"))

slicespp = int((pizzas * 8)/people)
leftover = pizzas * 8 % people
print(f"Each person will get {slicespp} slices with {leftover} leftover!")