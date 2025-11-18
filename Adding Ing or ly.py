# Q: Why check string length before modification?
def add_string(str1):
    length = len(str1)
    if length > 2:
        if str1.endswith('ing'):
            str1 += 'ly'
        else:
            str1 += 'ing'
    return str1


s1 = input('Enter the string: ')
print(add_string(s1))
