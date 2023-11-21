digit = tuple(input().split())

for i in set(digit):
    print(f'Символ {i}: {digit.count(i)}')
