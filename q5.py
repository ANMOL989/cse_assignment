#question 5: 
#(a)print a list and then remove 4th element from the list and let it print the new list
#(b)remove 'Black' and 'Pink' from the list and replace it with 'Purple'

my_list=['Red','Green','White','Black','Pink','Yellow']
#(a) part
print('(a)')
print(my_list)
my_list.remove('Black')
print(my_list)


my_list=['Red','Green','White','Black','Pink','Yellow']
#(b) part
print('(b)')
print(my_list)
my_list[3]='Purple'
my_list[4]='Purple'
print(my_list)
