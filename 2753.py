year=int(input())
while 1<=year<=4000:
    if (year%4==0)&(year%100!=0):
        print("1")
    elif year%400==0:
        print("1")
    else:
        print("0")
    break