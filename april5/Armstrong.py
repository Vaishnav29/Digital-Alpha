for i in range(1, 1001):
    b = len(str(i))
    res = 0
    org = i
    while org > 0:
        rem = (org % 10)
        res += rem**b
        org //= 10
    if i == res:
        print(i)
