def printDuplicate(myList):
    # get a size of list first

    sizeOfList = len(myList)

    # here we store  new list
    getNewList = []

    for i in range(sizeOfList):
        a = i + 1
        for j in range(a, sizeOfList):
            if myList[i] == myList[j] and myList[i] not in getNewList:
                getNewList.append(myList[i])
    return getNewList


A = [1, 2, 3, 4, 3, 2, 1, 4]
print(printDuplicate(A))


def sortList(unsorted_list):
    sorted_list = []
    while unsorted_list:
        minimum = unsorted_list[0]
        for item in unsorted_list:
            if item < minimum:
                minimum = item
        sorted_list.append(minimum)
        unsorted_list.remove(minimum)
    return sorted_list


A = [110, 0, 8, 5, 7, 3, 2, 4, 1]
n = len(A)
print("sorted list", sortList(A))


def thirdSmallestNumberOfArray(myList, number):
    newList = []
    while myList:
        miniNum = myList[0]
        for i in myList:
            if i < miniNum:
                miniNum = i
        newList.append(miniNum)
        myList.remove(miniNum)
    thirdEle = newList[2]
    return thirdEle


A = [10, 20, 3, 2, 8]
number = len(A)
print("third smallest number of array", thirdSmallestNumberOfArray(A, number))


def findFrequency(myList):
    x = 8
    counter = 0
    for i in myList:
        if i == x:
            counter = counter + 1
    return counter


A = [1, 1, 1, 1, 1, 1, 3, 5, 8, 7, 0, 9]
print("frequency of array is", findFrequency(A))


def sortArrayInAscendingOrder(myList):
    empty_list = []

    while myList:
        minNum = myList[0]
        for i in myList:
            if i < minNum:
                minNum = i
            empty_list.append(minNum)
    return empty_list


A = [0, 2, 1, 2, 0]
print("Ascending order of array is", sortArrayInAscendingOrder(A))
