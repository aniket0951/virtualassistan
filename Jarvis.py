import turtle
import phonenumbers
from phonenumbers import geocoder, carrier
import subprocess

# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor('black')
# t.speed(0)
#
# col = ['yellow','red','pink', 'cyan', 'green', 'blue']
#
# for i in range(120):
#     t.pencolor(col[i%6])
#     t.circle(190-i/2,90)
#     t.lt(90)
#     t.circle(190-i/3,90)
#     t.lt(60)

# s.exitonclick()


a_string = "nick tell me the service provider of 7038206592"

numbers = []
for word in a_string.split():
    if word.isdigit():
        numbers.append(int(word))


def findServiceProvider():
    phoneNumber = phonenumbers.parse("+918262861157")

    # Getting carrier of a phone number
    Carrier = carrier.name_for_number(phoneNumber, 'en')

    # Getting region information
    Region = geocoder.description_for_number(phoneNumber, 'en')

    # Printing the carrier and region of a phone number
    if Carrier and Region:
        print(Carrier)
        print(Region)
    else:
        print("Country code miss-matched")

#
#
#
#
#
#
#
