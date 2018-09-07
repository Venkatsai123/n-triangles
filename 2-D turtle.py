import turtle
myPen = turtle.Turtle()
myPen.shape("arrow")
myPen.color("red")
def drawPolygon(numberOfsides,l):
  exteriorAngle=360/numberOfsides
  length=600/numberOfsides
  myPen.penup()
  myPen.goto(-length/2,-length/2)
  myPen.pendown()
  for i in range(0,numberOfsides):
      myPen.forward(length)
      myPen.write(l[i])
      myPen.left(exteriorAngle)
  myPen.hideturtle()
l=[]
r=int(input("enter the range upto how many 2-D shapes to be performed:"))
s=int(input("enter the no.of sides:"))
print("enter the sides of 2-D shape:")
for i in range(0,s):
    l.append(int(input()))
l.sort()

n=input("enter which operation to be perform:")
print("the given 2-D shape:",l)
for j in range(1,r+1):
    l2=[]
    l2=l.copy()
    c=l2[0]
    del l2[0]
    l2.append(c)
    for i in range(0,s):
        if(n=="+"):
            l[i]=l[i]+l2[i]
        elif(n=="*"):
            l[i]=l[i]*l2[i]
        elif(n=="-"):
            l.sort(reverse=True)
            l2=l.copy()
            c=l2[0]
            del l2[0]
            l2.append(c)
            l[i]=l[i]-l2[i]
        elif(n=="/"):
            l.sort(reverse=True)
            l2=l.copy()
            c=l2[0]
            del l2[0]
            l2.append(c)
            l[i]=l[i]/l2[i]
    print("the 2-D shape with ",s," sides:",l)
    drawPolygon(s,l)

     
