num = int(input('Enter a number: '))
p_value = float(input('Enter a percentage value: '))

# Calculate the percentage value
result = (p_value / 100) * num
print(f'{p_value}% of {num} is: {result}')