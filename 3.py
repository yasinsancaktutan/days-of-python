# create a dict of key : value pairs for numbers from 1 to n where key is the number and value is the square of that number

print('enter in a number:')
n = int(input())
d = dict()
for i in range(1, n+1):
    d[i] = i*i
print(d)