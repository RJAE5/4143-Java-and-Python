def has_duplicates(l):
    copy = list(l)
    copy.sort()

    for i in range(1, len(copy)):
            if copy[i - 1] == copy[i]:
                return True
    return False
               

item = [1, 2, 3, 4, 5, 7]

print(has_duplicates(item))


def has_duplicates2(l):
    testDict = {}
    testDict[0] = l[0]

    for i in range(len(l)):
         for j in range(len(testDict.values())):
              if l[i] == testDict.Values()[j]:
                   return True
              else:
                   return False


# print(item)