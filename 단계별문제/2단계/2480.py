num1,num2,num3=map(int,input().split())
prize=0
if num1==num2==num3:
    prize=10000+num1*1000
elif num1==num2 or num1==num3 or num2==num3:
    if num1==num2 or num1==num3:
        prize=1000+num1*100
    if num2==num3:
        prize=1000+num2*100
else:
    prize=max(num1,num2,num3)*100

print(prize)