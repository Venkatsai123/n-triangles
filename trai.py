l=[]
r=int(input("enter the range upto how many trangles to be performed:"))
print("enter the sides of triangle:")
for i in range(0,3):
    l.append(int(input()))
l.sort()
n=input("enter which operation to be perform:")
print("the given triangle:",l)
for i in range(1,r+1):
    c=l[0]
    if(n=="+"):
        l[0]=l[0]+l[1]
        l[1]=l[1]+l[2]
        l[2]=l[2]+c
        print("the triangle ",i," sides:",l)
    elif(n=="*"):
        l[0]=l[0]*l[1]
        l[1]=l[1]*l[2]
        l[2]=l[2]*c
        print("the triangle ",i," sides:",l)
    elif(n=="-"):
        l.sort(reverse=True)
        c=l[0]
        l[0]=l[0]-l[1]
        l[1]=l[1]-l[2]
        l[2]=l[2]-c
        if(min(l)==0 or min(l)<0):
            break
        else:
            print("the triangle ",i," sides:",l)
    else:
        l.sort(reverse=True)
        c=l[0]
        l[0]=l[0]/l[1]
        l[1]=l[1]/l[2]
        l[2]=l[2]/c
        if(min(l)==0):
            break
        else:
             print("the triangle ",i," sides:",l)
