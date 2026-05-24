# 30 minutes practice. Simple student grade calculator
student_name = input('Enter the student name: ')
first_subject = input('Enter the name of the first subject: ')
second_subject = input('Enter the name of the second subject: ')
third_subject = input('Enter the name of the third subject: ')

# Get the marks for each subject
first_subject_marks = float(input(f'\nEnter the marks obtained in {first_subject}: '))
second_subject_marks = float(input(f'Enter the marks obtained in {second_subject}: '))
third_subject_marks = float(input(f'Enter the marks obtained in {third_subject}: '))

# calculate total marks
total_marks = first_subject_marks + second_subject_marks + third_subject_marks
print(f'\nTotal marks obtained by {student_name} is: {total_marks}')

# calculate average marks
average_marks = total_marks / 3
print(f'\nAverage marks obtained by {student_name} is: {average_marks}')