def get_my_counter():
    def inner(a=[]):
        a.append(0)
        return len(a)-1
    return inner

my_counter=get_my_counter()
print(my_counter())
print(my_counter())
print(my_counter())