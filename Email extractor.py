import re

# Q: What does VERBOSE mode allow in regex?
s = re.compile('''[a-zA-Z0-9._-]+@ [a-zA-Z0-9]+ .[a-zA-Z]{2,4}''', re.VERBOSE)
print(s.findall("Contact : suma_12@gmail.com  jG_1234@yahoo.com"))
