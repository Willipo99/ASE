# calculator.py

def sum(m, n):
    if(n > 0):
        for i in range(n):
            m += 1
    else:
        for i in range(abs(n)):
            m -= 1
    return m;

def divide(m, n):
    res = 0
    negativeRes = m > 0 and n < 0 or m < 0 and n > 0
    n = abs(n)
    m = abs(m)

    while(m - n >= 0):
        m -= n
        res += 1

    res = -res if negativeRes else res

    return res


print(sum(2,-3))
print(divide(-8, 2))