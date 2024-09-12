# Define a generator function to produce Fibonacci numbers indefinitely
def fib():
    # Initialize the first two Fibonacci numbers
    a, b = 1, 1
    # Infinite loop to keep generating Fibonacci numbers
    while True:
        # Yield the current Fibonacci number (starts with 'a')
        yield a
        # Update 'a' and 'b' to the next Fibonacci numbers in the sequence
        a, b = b, a + b

# Iterate through the generated Fibonacci numbers with an index
# 'enumerate(fib())' gives both the index and the Fibonacci number
for index, x in enumerate(fib()):
    # Stop the loop after 100 numbers (i.e., when index reaches 100)
    if index == 100:
        break
    # Print each Fibonacci number on the same line, followed by a space
    print("{} ".format(x), end="")
