import turtle
k = turtle.Screen()
me=turtle.Turtle()

#movements
dist = 0
ang = 120
me.left(60)
for i in range(10):
    
    
    me.speed(10)
    dist +=10
    
    
    me.right(ang)
    me.forward(dist)
    me.right(ang)
    me.forward(dist)
       

me.fillcolor("red")
me.begin_fill("red")
        
k.exitonclick()
