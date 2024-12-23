enter=int(input('Enter the number :'))
my_list = []

for num in range ( 1, enter+1):
    result=""
    if num %3 ==0:
        result = result + 'Fizz'
        my_list.append(result)

print(my_list)
    

