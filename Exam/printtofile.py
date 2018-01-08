with open('printtext.txt', 'w') as f:
    print('printed by print function', file=f)
with open('printtext.txt') as f:
    print(f.read())