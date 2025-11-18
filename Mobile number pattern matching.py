import re

# Q: What do \d{2} and \d{10} represent?
regExp = re.compile(r'(\d{2})-(\d{10})')
mo = regExp.search('mobile number is 91-9394746581')

print(mo.groups())
print(mo.group(1))  # country code
print(mo.group(2))  # number

countryCode, uniqueCustNum = mo.groups()
print("customer mobile number is " + uniqueCustNum)
