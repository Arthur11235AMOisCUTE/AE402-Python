import turtle

John = turtle.Turtle()

canvas = turtle.Screen()

canvas.title('Turtle Canvas')

canvas.bgcolor('#5286b4')

John.speed(0)
               

John.penup()
John.goto(-25,320)
John.pendown()



a = 3
for i in range (38):
    print(a)
    for i in range(a):
    
            John.forward(50)
    
            John.right(360/a)
    a += 1
'''        
for i in range(12):

        John.forward(50)

        John.right(150)
'''
turtle.done()
turtle.bye()