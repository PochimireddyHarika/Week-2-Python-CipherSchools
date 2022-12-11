# more about get, two same keys in dictionaries

user = {'name': 'Harika', 'age': 18, 'age': 20}
print(user)
print(user.get('name'))
print(user.get('names'))
print(user.get('fav', 'not found ! '))