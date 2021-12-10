# 1) reverse the list list1 = [100, 200, 300, 400, 500]
# list1 = [100, 200, 300, 400, 500]
# for list in reversed(list1):
#     print(list)

# 2) concatinate two list index wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
#
# res = [i + j for i, j in zip(list1, list2)]
# print(res)

# 3)Exercise 3: Turn every item of a list into its square
# numbers = [1, 2, 3, 4, 5, 6, 7]
# for i in numbers:
#     print(i*i)

# 4)Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# res = [i + j for i, j in zip(list1, list2)]
# print(res)


# 5) Exercise 5: Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
empty_list = []
for i in list1:
    empty_list.append(i)
    for i in reversed(list2):
        empty_list.append(i)


print(empty_list)

