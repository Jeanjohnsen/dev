def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


#Print 100 fibs
for index, x in enumerate(fib()):
    if index == 100:
        break
    print("{} ".format(x), end="")
