#Thank you for adding Turtler boot video to your code if you want more sub packages go to
# https://github.com/SlideShowGames/SlideShowGames and also check out my youtube https://www.youtube.com/channel/UCECRYbDpMr5aMyxhnS3ESGg


import turtle
def OSbooter():
    turtle.TurtleScreen
    turtle.color("blue")
    turtle.bgcolor("Green")
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.color("white")
    turtle.left(90)
    turtle.left(90)
    turtle.forward(50)
    turtle.color("blue")
    turtle.circle(100)
    turtle.bgcolor("black")
    turtle.bgpic("python-powered Turtler.gif")
OSbooter()

def calculator():
    print("current mode addition")
    number1 = input("enter first number")


number2 = input("enter second number")
vsum = float(number1) + float(number2)
print(vsum)
print("mode now subtraction")
number3 = input("enter first number")
number4 = input("enter second number")
vsum2 = float(number3) - float(number4)
print(vsum2)
print("mode now division ")
number5 = input("enter first number")
number6 = input("enter second number")
vsum3 = float(number5) / float(number6)
print(vsum3)
print("mode now multiplication")
number7 = input("enter first number")
number8 = input("enter second number")
vsum4 = float(number7) * float(number8)
print(vsum4)



UserName = input("make a name")
def OSmenu():
    print('Welcome To iCal OS v2.1.0 {}'.format(UserName))
    MainMenu = input("""
                   What Would You Like To Do?
                   [1]. Exit os
                   """)

OSmenu()
if MainMenu == "2" :
 calculator()



#Thank you for the calculator to your code if you want more sub packages go to
# https://github.com/SlideShowGames/SlideShowGames and also check out my YouTube https://www.youtube.com/channel/UCECRYbDpMr5aMyxhnS3ESGg