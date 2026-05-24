# student grade checker
student_name = input('Enter the student name: ')
score = float(input('Enter the score: '))

if score >= 70:
    grade = 'Distinction'
elif score >= 60:
    grade = 'Merit'
elif score >= 50:
    grade = 'Pass'
else:
    grade = 'Fail'

print(f'\n{student_name} scored {score} and received grade {grade}.')