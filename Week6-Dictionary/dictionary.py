# Create a Dictionary using dict() or {}
city = dict()
print(city)

city["Singair"] = 1820
city["Manikganj"] = 1819
print(city)
print(len(city))


########## Another way ##########
# Determining if a Dictionary Is Empty or not
if city:
  print('not empty')
else:
  print('empty')
  
  
########## Iterate a dictionary ##########
for area, code in city.items():
  print(f'{area}’s area code is {code}')
  
  
########## Dictionary operations 
# Accessing a value 
city["Cantonment"]
# Update a value
city['Cantonment'] = 1202
print(city)


# updating/insert both key-value respectively
city.update({'Mohammadpur':1207})
print(city)
city.update({'Mohammadpur Housing':	1207})
print(city)
city.update({'Mohammadpur': 1208})
print(city)


# Adding a new key-value pair
city['Mirpur'] = 1212
print(city)


# remove a key-value pair
del city['Cantonment']
print(city)

