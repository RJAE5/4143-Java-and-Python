# In-class programs
# Rykir Evans

###################################################################
### Program 1 - Print if n is perfect, abundant, or deficient  ####
###################################################################
inNum = int(input("Please enter a positive integer: "))

def perf(num):
    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum += i
            # print(f"adding {i} to sum")
            # print(f"sum = {sum}")

    if sum > num:
        print("That number is an abundant number!")
    elif sum < num:
        print("That number is a deficient number!")
    else:
        print("That is a perfect number!")

perf(inNum)

###################################################################
### Program 2 -  Version of above but returns a char to print  ####
###################################################################
def charOut(n):
    cSum = 0
    for i in range(1, n):
        if n % i == 0:
            cSum += i
            # print(f"adding {i} to sum")
            # print(f"sum = {sum}")

    if cSum > n:
        return 'a'
    elif cSum < n:
        return 'd'
    else:
        return 'p'

print(f"The charOut version is {charOut(inNum)}!")

###################################################################
### Program 3 -  Recursion function that prints sum up to num  ####
###################################################################

def recsum(number):
    if number <= 0:
        return 0
    else:
        return number + recsum(number - 1)

num_test = int(input("Enter a number: "))

print(f"Total number: {recsum(num_test)}")


    