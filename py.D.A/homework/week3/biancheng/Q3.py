def my_sum(*args,value=1):
    '''
    Add Value To Numbers
    '''
    lis=[li+value for li in [*args]]
    return lis


print(my_sum(9,9,8,2,4,4,3,5,3,value=10))
print(my_sum(9,9,8,2,4,4,3,5,3))