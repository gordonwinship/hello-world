'''Fibonacci Numbers'''
def fibonacci(n, printall=False):
    f = 0
    f2 = 1
    for i in range(n):
        f, f2 = f2, f2+1
        if printall:
            print(f)
    print(f)

fibonacci(2)