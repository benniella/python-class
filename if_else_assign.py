# Calculator

f_num = int(input('Enter first number: '))
s_num = int(input('Enter second number: '))

#operation

print('\nPlease choose operator by number; (1,2,3,4)\n\n')
print('1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n\n')

operator = input('')

if operator == '1':
    result = f_num + s_num
    print(f'\nThe sum of {f_num} and {s_num} is: {result}')

elif operator == '2':
    result = f_num - s_num
    print(f'\nThe difference of {f_num} and {s_num} is: {result}')

elif operator == '3':
    result = f_num * s_num
    print(f'\nThe product of {f_num} and {s_num} is: {result}')

elif operator == '4':
    result = f_num / s_num
    print(f'\nThe quotient of {f_num} and {s_num} is: {result}')

else:
    print('\ninvalid operator! choose from the options (1,2,3,4)')