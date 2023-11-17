email = 'jane.stewart@yahoo.fr'

#votre programme
destroyedemail = email.split('.')


#Output : 
first_name = destroyedemail[0]
last_name = destroyedemail[1].split('@')[0]

print (first_name,'\n',last_name)