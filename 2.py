# compute the factorial of a given number, result printed in csv single line


def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)


print('Enter an integer...')
num = int(input())
print(factorial(num))