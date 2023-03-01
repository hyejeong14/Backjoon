A,B=map(int,input().split())
C=int(input())

H=A+((B+C)//60)
M=(B+C)%60

while (0<=A<=23)and(0<=B<=59)and(0<=C<=1000):
    if H>=24:
        H=H-24
    if M>=60:
        M=M-60
    break
print(H,M)