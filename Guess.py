n = 9

while True:
    inpNumber = int(input("Enter your guess \n"))
    if inpNumber == 25:
        print("Congrats you are winner", "you are taking only", n, "Guess")
        break
    elif n == 0:
        print("Game Over ")
        break
    else:
        n = n - 1
        print(n, "You have only guess left")
        continue
