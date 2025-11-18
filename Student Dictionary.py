# Q: What data type is used to store skills?
person = {
    'first_name': 'Ambika',
    'last_name': 'S',
    'age': 25,
    'country': 'Bengaluru',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {'street': 'K R Road', 'zipcode': '5600008'}
}

print(len(person))  # Q: What does len() return for dictionaries?

print(person['skills'])
print(type(person['skills']))

# Add new skill
person['skills'].append('c++')
print(person)

# Get keys and values
print(list(person.keys()))
print(list(person.values()))

# Convert dictionary to list of tuples
print(list(person.items()))

# Delete a key
del person['is_married']

# Clear entire dictionary
person.clear()
print(person)
