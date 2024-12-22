marks ={
    'Hindi':60,
    'English':70,
    'Maths':39
    } # key:value 

print(type(marks))
print(marks)
print(marks['Hindi'])# to get output of that particular data
print(marks.get('Science'))# error not display by usinf 'get'

marks['Science']=20
print(marks) 

del marks['Hindi']
print(marks)