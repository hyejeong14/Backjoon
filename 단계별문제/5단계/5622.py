S=list(input())
count=0
for i in S:
    if ord('A')<=ord(i)<=ord('C'):
        count+=3
    elif ord('D')<=ord(i)<=ord('F'):
        count+=4
    elif ord('G')<=ord(i)<=ord('I'):
        count+=5
    elif ord('J')<=ord(i)<=ord('L'):
        count+=6
    elif ord('M')<=ord(i)<=ord('O'):
        count+=7
    elif ord('P')<=ord(i)<=ord('S'):
        count+=8
    elif ord('T')<=ord(i)<=ord('V'):
        count+=9
    elif ord('W')<=ord(i)<=ord('Z'):
        count+=10
    
print(count)

'''다이얼 알파벳
Number=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word=input()
time=0
for num in Number:
  for x in word:
    if(x in num):
      time+=Number.index(num)+3
print(time)'''