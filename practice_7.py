# football match ticket category
age = int(input('Enter your age: '))
print('\n Are you a student? \n(yes/no)')

operator = input().lower()

if age < 16:
    print('\nYou are eligible for a child ticket ')
elif age >= 60:    
    print('\nYou are eligible for a senior ticket')    
elif age >=16 and age<=59 and operator == 'yes':    
    print('\nYou are eligible for a student ticket')
elif age >= 16 and age <= 59 and operator == 'no':
    print('\nYou are eligible for an Adult ticket')
else:
    print('\nInvalid input! Please enter a valid age and student status (yes/no)')