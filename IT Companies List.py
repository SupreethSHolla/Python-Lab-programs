IT_Companies = ["Facebook", "Google", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]
print(IT_Companies)

# Q: How does sort() arrange strings?
IT_Companies.sort()
print(IT_Companies)

# Q: What does reverse() do after sorting?
IT_Companies.reverse()
print(IT_Companies)

# First 3 companies
print(IT_Companies[0:3])

# Last 3 companies
print(IT_Companies[-3:])

# Finding middle company
mid = len(IT_Companies) // 2

# Q: Why check if mid is odd or even?
if mid % 2 != 0:
    print(IT_Companies[mid])
else:
    print(IT_Companies[mid:mid+1])

# Remove first company
del IT_Companies[0]
print(IT_Companies)

# Remove middle company
del IT_Companies[mid]
print(IT_Companies)

# Remove last company
del IT_Companies[-1]
print(IT_Companies)
