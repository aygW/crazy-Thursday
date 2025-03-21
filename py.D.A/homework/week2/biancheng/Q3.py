n,m=map(int,input().split())
lis=list(map(str,input().split()))
s=set()
for i in range(0,m):
    s.update(map(str,input().split()))
num=n-len(s)
print(num)

'''for name in lis:
    if name in s:
        lis.remove(name)
num=len(s)'''
'''for i in range(0,m):
    liss=list(map(str,input().split()))
    for name in liss:
        if name in lis:
            lis.remove(name)
num=len(lis)
print(num)'''

'''lisss=[0]*n
flag=0
for i in range(0,m):
    liss=list(map(str,input().split()))
    for name in liss:
        if(name not in lisss):
            lisss[i]=name
            i+=1'''

'''liss=[0]*m
for i in range(0,m):
    liss[i]=list(map(str,input().split()))
lisss=[e for ele in liss for e in ele]
for i in range(0,n):
    if(lis[i] in lisss):
            lis[i]=0
num=n-lis.count(0)
print(num)'''