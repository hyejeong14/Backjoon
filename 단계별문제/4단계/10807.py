import sys
N=int(input())
n=list(map(int,sys.stdin.readline().split()))
while len(n)==N:
    try:
        v=int(sys.stdin.readline())
        count=0
        for i in n:
            if v==i:
                count+=1
        print(count)
        break
    except:
        print("error")