def intreverse(n):
    n = str(n)
    x = ""
    for i in range(1, 1 + len(n)):
        x += n[-i]
    return x


def matched(s):
    x = 0
    y = 0
    for i in range(len(s)):
        if y <= x:
            if s[i] == "(":
                x += 1
            elif s[i] == ")":
                y += 1
        else:
            return False
    if x == y:
        return True
    else:
        return False

def isprime(x):
    if x > 1:
        for i in range(2,x):
            if (x%i) == 0:
                return False
        else:
            return True
    else:
        return False

def sumprimes(l):
    sum = 0
    for i in l:
        if isprime(i):
            sum += i
    return sum
