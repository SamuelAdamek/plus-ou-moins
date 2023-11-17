numbers = [8, 7, 11, 7, 2, 10, 5, 8]

compteur = 0 
result = []

for num in numbers:
    if num not in result:
        result.append(num)

print(f'Tableau original :{numbers}\n')
print(f'Tableau modifier :{result}\n')