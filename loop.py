# Looping through a list of numbers and printing those greater than 10
number = [2, 5, 6, 10, 50, 60]
for num in range(len(number)):
   # print(f'index {num} is: {number[num]}')
   pass


#printing number greater than 10
for num in number:
    if num > 10:
       # print(num)
        pass


# number 2
for num in range(1,51):
    if num % 4==0: 
        #print(f'number divisible by 4: \n{num}')
        pass

for num in range(1,51):
    if num % 8!=0:
    #    print(f'numbers that are not divisibe by 8: \n{num}')
        pass

# number 3
colors = ['blue', 'green', 'yellow']
objects = ['car', 'house', 'shirts']
for color in colors:
    if color == 'green':
        continue
    for obj in objects:
        #print(f'{color} {obj}')
        pass

# number 4
for i in range(5):
    for j in range(5):

        if i == j:
        #    print("*", end=" ")

       # else:
     #       print(" ", end=" ")

    #print()
    
            pass



        
# number 5
scores1 = [10, 20, 30]
scores2 = [5, 15, 25]

# Print sum of each pair
for num1 in scores1:
    for num2 in scores2:

        total = num1 + num2
        print(f"{num1} + {num2} = {total}")

# Print only sums greater than 30
print("\nSums greater than 30:")

for num1 in scores1:
    for num2 in scores2:

        total = num1 + num2

        if total > 30:
            print(total)        