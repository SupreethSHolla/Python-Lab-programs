import re

# Q: What does ^a and z$ enforce?
s = input("Enter the string: ")
pat = re.compile(r'^a[a-zA-Z]{3}z$')
matched = pat.search(s)

if matched:
    print("Search is successful")
else:
    print("Search is unsuccessful")
