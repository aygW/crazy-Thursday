n=int(input())
flag=0
song=dict()
for i in range(n):
    m=int(input())
    flag+=m
    for i in range(m):
        soname,comnum=input().split()
        song[soname]=int(comnum)
songg=sorted(song.items(),key=lambda x:x[-1],reverse=True)
for i in range(flag):
    print(songg[i][0],songg[i][1])