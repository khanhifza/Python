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

users_list.insert(2,'am')# to add data on specific position
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

users_list(reversed=True)
print(users_list)