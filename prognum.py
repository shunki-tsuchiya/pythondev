
def fibonacci(i):
    if i < 3:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)