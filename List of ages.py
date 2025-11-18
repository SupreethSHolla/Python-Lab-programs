# Q: What does sort() do to the list?
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)

ages.sort()
print(ages)

min_age = ages[0]
max_age = ages[-1]

# Q: Why is the last element considered max?
print("minimum age in list is", min_age, "maximum age in list is", max_age)

add_min_max_age = min_age + max_age
print("addition of minimum and maximum ages is", add_min_max_age)

# Q: How is the median computed using index and ~index?
mid = len(ages) // 2
median = (ages[mid] + ages[~mid]) / 2
print("Median of list is:", median)

average = sum(ages) / len(ages)
print("Average age of list is:", average)
