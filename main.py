from decimal import *
num = abs(Decimal(input()))
print(max(num.as_tuple().digits) if num < 1 else min(num.as_tuple().digits) + max(num.as_tuple().digits))
print('Hello, Nikita')
print('Sup, Max!')
