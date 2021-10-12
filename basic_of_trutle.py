import turtle

shreyas = turtle.Turtle()

#draw a line 

#shreyas.forward(200)

#dram a rectangle 
'''
shreyas.forward(200)
shreyas.right(90)
shreyas.forward(200)
shreyas.right(90)
shreyas.forward(200)
shreyas.right(90)
shreyas.forward(200)'''


#filling clolor in rectangle
'''
shreyas.begin_fill()
shreyas.color("black","skyblue")
shreyas.forward(200)
shreyas.right(90)
shreyas.forward(200)
shreyas.right(90)
shreyas.forward(200)
shreyas.right(90)
shreyas.forward(200)
shreyas.end_fill()
'''

#drawing polygon using for loop
'''
for i in range(20):
    shreyas.forward(100)
    shreyas.left(45)
   
    shreyas.forward(10)
'''
#creating sun 
'''
for i in range(75):
    shreyas.begin_fill()
    
    shreyas.color("blue","yellow")
    shreyas.forward(100)
    shreyas.right(170)
    shreyas.forward(100)
    
    shreyas.end_fill()

'''
#draw start pattern
'''
for i in range(20):
    shreyas.forward(100)
    shreyas.left(180)
    shreyas.forward(100)
    shreyas.right(150)
'''

turtle.done()