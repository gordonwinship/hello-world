'''Fibonacci Numbers'''
def fibonacci(n, printall=False):
    print("-"*10)
    f = 0
    f2 = 1
    for i in range(n):
        f, f2 = f2, f2+1
        if printall:
            print(f)
    print("F_{} = {}".format(n,f))
    print("-"*10)

fibonacci(2)