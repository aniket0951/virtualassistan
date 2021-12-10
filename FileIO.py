f = open("AniketFile")


# myFile = f.read()


# print(myFile)


# to read a file line by line
# def readFileLineByLine():
#     for line in f:
#         print(line, end="")
#
#
# f.close()


def toReadFileFromSpecificPoint():
    m = open("AniketFile")
    m.seek(11)
    print(m.readline())
    m.close()


print(toReadFileFromSpecificPoint())
