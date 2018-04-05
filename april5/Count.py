new = input('enter')
d = l= 0
for c in new:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l = l+1
    else :
        pass
print('Letters', l)
print('Digits', d)