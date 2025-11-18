while True:
    point = float(input("Enter your scored point (0-100) for grading: "))

    if point > 100:
        print('Max. marks is 100!!!')
    elif point >= 93.33:
        print('A')
    elif point >= 90:
        print('A-')
    elif point >= 86.67:
        print('B+')
    elif point >= 83.33:
        print('B')
    elif point >= 80:
        print('B-')
    elif point >= 76.67:
        print('C+')
    elif point >= 73.33:
        print('C')
    elif point >= 70:
        print('C-')
    elif point >= 66.67:
        print('D+')
    elif point >= 63.33:
        print('D')
    elif point >= 60:
        print('D-')
    elif point >= 0:
        print('F')
    else:
        # Q: Why does negative input break the loop?
        print('Invalid input')
        break
