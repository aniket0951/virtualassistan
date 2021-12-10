list = [0,1,2,43,4,5,6,'Aniket','krishan']

# for items in list:
#     for subitems in items.split():
#         if(subitems.isDigit()):
#             print(subitems)

# a = ['1 2 3', '4 5 6', 'invalid']
numbers = []
for item in list:
    if str(item).isnumeric() and item < 6:
        print(item)



