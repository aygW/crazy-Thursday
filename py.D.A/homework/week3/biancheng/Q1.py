import random

def my_random(keys,weights):
    length=len(keys)
    collect=[]
    for i in range(length):
        for j in range(weights[i]):
            collect.append(keys[i])
    summ=sum(weights)-1
    ind=random.randint(0,summ)
    return collect[ind]

for i in range(10):
    print(my_random(keys=['a','b','c'],weights=[1,2,2]))