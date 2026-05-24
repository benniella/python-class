# 1 hour practice simple bank app
#account_creation

account_name = input('Enter your account name: ')
age = int(input('Enter your age: '))
initial_deposit = float(input('Enter your initial deposit amount: '))

print(f'\nWelcome {account_name}! Your account has been created with an initial deposit of ${initial_deposit}. You are {age} years old.')

# Deposit calculator

current_balance = float(input('\nEnter your current balance: '))
deposit_amount = float(input('Enter the amount you want to deposit: '))

new_balance = current_balance + deposit_amount
print(f'\nour new balance after depositing ${deposit_amount} is: ${new_balance}')

# Withdrawal calculator
current_balance = float(input('\nEnter your current balance: '))
withdrawal_amount = float(input('Enter the amount you want to withdraw: '))

remaining_balance = current_balance - withdrawal_amount
print(f'\nYour remaining balance after withdrawing ${withdrawal_amount} is: ${remaining_balance}')

#interest calculator
principal = float(input('\nEnter the principal amount: '))
rate = float(input('Enter the annual interest rate (in percentage): '))
time = float(input('Enter the time in years: '))

interest = (principal * rate * time) / 100
print(f'\nThe interest earned on your deposit is: ${interest}')

#currency converter
amount_in_usd = float(input('\nEnter the amount in USD you want to convert: '))
exchange_rate = float(input('Enter the exchange rate (1 USD to your local currency): '))

amount_in_local_currency = amount_in_usd * exchange_rate
print(f'\n{amount_in_usd} USD is equivalent to {amount_in_local_currency} in your local currency.')

