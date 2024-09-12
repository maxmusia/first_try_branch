from decimal import *
n = int(input())
num = abs(Decimal(n))
print(max(num.as_tuple().digits) if num < 1 else min(num.as_tuple().digits) + max(num.as_tuple().digits))
print('Hello, Nikita')
for i in range(n):
    for j in range(10):
        print('11', sep='_', end='')
    print()
