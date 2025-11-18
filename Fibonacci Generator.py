# Q: What do 'first' and 'second' represent here?
def fib(n):
    first = 0
    second = 1

    if n >= 1:
        print(first, end=" ")
    if n >= 2:
        print(second, end=" ")

    i = 3
    while i <= n:
        third = first + second
        print(third, end=" ")
        first = second
        second = third
        i += 1

n = int(input("How many Fibonacci numbers to generate: "))
fib(n)
