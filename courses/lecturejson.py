import json

# TP JSON

#1 lire le fichier JSON

with open('./data/users.json') as f:
    data = json.load(f)

#print(data['users'][0]['eyeColor'])
    
#print(data['users'])
    
total_users = len(data['users'])
#1
print(len(data['users']))

#2
print(data['users'][1]['company'])

#3
print(data['users'][1]['friends'][2]['name'])

#4
print(data['users'][0]['eyeColor'])

#5
for x in range(len(data['users'])) :
    print(data['users'][x-1]['address'])

#6
    
#totalusersfruits = 0
#for x in range(len(data['users'])) :
#    if data['users'][x-1]['favoriteFruit'] == "strawberry" :
#        totalusersfruits += 1
#print(totalusersfruits)
    
total_users_fruits = 0
for x in data['users']:
    if x['favoriteFruit'] == "strawberry":
        total_users_fruits += 1
print(total_users_fruits)

#7
for user in data['users']:
    if user['name'] == 'Brianna Huffman' :
        print(user['greeting'])

#8
total_users_male = 0
for user in data['users']:
    if user['gender'] == 'male' :
        total_users_male += 1
print((total_users_male/total_users)*100)

#9
total_female_age = 0
total_users_female = 0
for user in data['users']:
    if user['gender'] == 'female' :
        total_users_female += 1 
        total_female_age += user['age']

print(round(total_female_age/total_users_female))

#10
total_soldes_somme = 0
for user in data['users']:
    user_solde = user['balance']
    user_solde = user_solde.replace("$","").replace(",","")
    total_soldes_somme += float(user_solde)
total_soldes_somme = "{:,.2f}".format(float(total_soldes_somme))
total_soldes_somme = "$" + str(total_soldes_somme)
print(total_soldes_somme)

#11

for user in data['users']:
    if user['name'] == 'Zelma Sutton' :
        
        print(user['address'])