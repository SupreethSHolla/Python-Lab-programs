# Q: What does the function return based on month numbers?
def check_season(month):
    if month == 2 or month == 3:
        return "Spring"
    elif month in (4, 5, 6):
        return "Summer"
    elif month in (7, 8, 9, 10):
        return "Autumn"
    elif month in (11, 12, 1):
        return "Winter"
    else:
        return "Invalid month"


month = int(input("Enter the month (as a number): "))
print("Season:", check_season(month))
