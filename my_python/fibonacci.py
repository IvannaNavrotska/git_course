def fibonacci (f):
    if f == 0 or f == 1:
        return 1
    else:
        return fibonacci(f-1) + fibonacci(f-2)
    
print(fibonacci(5))
print('i just need to change something')
