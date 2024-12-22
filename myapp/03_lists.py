users_list=['i','am','hifza']
print(users_list)
print(users_list[0])
print(users_list[1])

users_list.append('khan')#add data in a list
print(users_list)

users_list.remove('am') #remove data from list
print(users_list)

users_list[1]="Hifza" # to rewrite data
print(users_list)

users_list.insert(2,'hifza')# to add data on specific position
print(users_list)

del users_list[2]
print(users_list)

# No. of items in a list
print(len(users_list))

users_list.extend(['i','want','to','become','devops']) # to add multiple items
print(users_list)

#sorting of list

users_list.sort()
print(users_list)

#users_list(reversed=True)
users_list.sort()
print(users_list)

users_list.pop()
print(users_list)

remove = users_list.pop()
print (remove)

users_list[0:4]
print(users_list[0:4])
print(users_list[:4])
print(users_list[2:4])
print(users_list[-4:])


marks=(34,5.6,1,2,7,93,4.24,7,)
print(min(marks))
print(max(marks))
print(sum(marks))

mix_list=('hifza'23,46,74.6)
print(mix_list)