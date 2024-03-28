def fibonacci (f):
    if f == 0 or f == 1:
        return 1
    else:
        return fibonacci(f-1) + fibonacci(f-2)
    
print('this is for master')
print(fibonacci(5))


