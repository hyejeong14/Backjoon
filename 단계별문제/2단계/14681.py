x=int(input())
y=int(input())
while 1:
    if (x>0)&(y>0):
        print("1")
    elif (x<0)&(y>0):
        print("2")
    elif (x<0)&(y<0):
        print("3")
    elif (x>0)&(y<0):
        print("4")
    break
