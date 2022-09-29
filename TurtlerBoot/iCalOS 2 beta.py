#Thank you for adding Turtler boot video to your code if you want more sub packages go to
# https://github.com/SlideShowGames/SlideShowGames and also check out my youtube https://www.youtube.com/channel/UCECRYbDpMr5aMyxhnS3ESGg
UserName = input("make a name")
def OSmenu():
    print("Welcome To iCal OS 2 vBeta 0.2",UserName)
    MainMenu = input("What Would You Like To Do? "
                 "[1].Calculator "
                 "[2].usb.pyVideo "
                 "[3].pickup.pyVideo" 
                 " [4].exit"
                 " [5].how to install new files")
    if MainMenu == "1" :
        calculator()
    if MainMenu == "2" :
        Usbvideo()
        OSmenu()
    if MainMenu == "3" :
        PickupVideo()
        OSmenu()
    if MainMenu == "4" :
        exit()
    if MainMenu == "5" :
        print("to install new files you must..."
"1. import a defined word for copy and paste or writing it."
"2. on the menu put a extra number then a if command that uses your word."
"3. test it.")
        print("__________________________________________________________________")
        OSmenu()
import os
import turtle
def Usbvideo():
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
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.bgpic("python-powered Turtler.gif")
    turtle.exitonclick()

def PickupVideo():
    turtle.bgcolor("black")
    turtle.color("white")
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(65)
    turtle.backward
    turtle.circle(55)
    turtle.forward(100)
    turtle.color("black")
    turtle.forward(100)
    turtle.color("red")
    turtle.circle(40)
    turtle.bgpic("python-powered Turtler.gif")
    turtle.exitonclick()




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
    print("mode now multiplication ")
    number7 = input("enter first number")
    number8 = input("enter second number")
    vsum4 = float(number7) * float(number8)
    OSmenu()

OSmenu()
#Thank you for the calculator to your code if you want more sub packages go to
# https://github.com/SlideShowGames/SlideShowGames and also check out my YouTube https://www.youtube.com/channel/UCECRYbDpMr5aMyxhnS3ESGg
turtle.mainloop()