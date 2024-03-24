n = int(input('Enter your number: '))

answer = input("Do you want to find the factorial of your number 'yes or no': ")

if answer == 'yes':
    
    def fact(n):
        if n==0 or n==1:
            return 1
        else:
            return n*fact(n-1)
    print(f'The factorial of {n} is:', fact(n))
else:
    print('Just as you like :)')
    
