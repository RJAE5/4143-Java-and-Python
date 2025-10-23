
# `with` automatically opens and closes files
wordSum = 0
digitSum = 0
with open("Frankenstein.txt", encoding="utf-8") as fin:
    for line in fin:
        s = line.strip()
        wordSum += len(s.split())

    print(wordSum)


with open("Frankenstein.txt", encoding="utf-8") as fin:
    for line2 in fin:
        s = line2.strip()
        temp = s.split()
        for i in range(len(temp)):
            if temp[i].isdigit():
              digitSum += int(temp[i])

    print(digitSum)

my_list = [4,5,6]
your_list = ['a','b','c']

our_list = my_list + your_list
print(our_list)

his_list = my_list * 2
print(his_list)

a_list = my_list
x = a_list.pop(2)
print(x)
print(a_list)
print(my_list)

the_list = your_list + []
the_list.extend(['q','r','s'])
print(the_list[4:])

her_list = my_list.append(7)
print(my_list)
print(her_list)