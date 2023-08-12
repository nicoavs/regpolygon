import turtle

n = input("Enter the number of sides your regular polygon: ")

if len(n.split()) == 1 and n.isdigit() and int(n) > 2:
    n = int(n)

else:
    print("Wrong input: must give a number greater than 2")
    quit()

angle = 360/n

wn = turtle.Screen()

regPol = turtle.Turtle()

for _ in range(n):
    regPol.forward(50)
    regPol.left(angle)

wn.exitonclick()
