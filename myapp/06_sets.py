# sets do not add duplicate value only unique values taken
my_sets=('MON','TUE','WED','THU') 
print(type(my_sets))
print(my_sets)

my_sets.__add__('FRI')
print(my_sets)

my_list=('mon','tue','wed','mon','wed')
days_set=set(my_list)
print(days_set)