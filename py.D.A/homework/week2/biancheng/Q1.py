students=eval(input())
student_sorted=sorted(students,key=lambda x:x[-1],reverse=True)
for tu in student_sorted:
    print(tu[0],tu[1],tu[2])