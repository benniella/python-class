# AI Course admission checker
applicant_name = input('Enter the applicant name: ')
applicant_age = int(input('Enter the applicant age: '))
laptop_ownership = input('Does the applicant own a laptop? (yes/no): ').lower()
previous_experience = input('Does the applicant have previous experience in AI? (yes/no): ').lower()

if applicant_age >= 18 and laptop_ownership == 'yes'or'no' and previous_experience == 'yes' or 'no':
    print(f'\nCongratulations {applicant_name}! You are eligible to apply for the AI course.')
else:
    print(f'\nSorry {applicant_name}, you do not meet the eligibility criteria for the AI course .')
