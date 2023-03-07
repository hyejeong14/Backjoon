A,B = map(list,input().split())
A.reverse()
B.reverse()
A_int=0
B_int=0
for i in range(len(A)):
    A_int+=int(A[i])*(10**(2-i))
    B_int+=int(B[i])*(10**(2-i))

print(max(A_int,B_int))


#print(max(input()[::-1].split()))