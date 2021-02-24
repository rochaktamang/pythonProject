N=int(input('enter the number of students: '))
K=int(input('enter the number of apples: '))
number_of_apples_each_students_get=K//N
numbers_of_apples_in_basket=K%N
print(f'the number of apples each students get is {number_of_apples_each_students_get}')
print('the number of apples in basket is', numbers_of_apples_in_basket)