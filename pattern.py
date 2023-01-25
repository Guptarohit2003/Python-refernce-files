n = int(input())
m = (n+1)/2
i = 1
while i <= n:
    if i <= m:
        b = m-i
        s = 2*i-1
    else:
        b = i-m
        s = 2*(n-i)+1
    j = 1
    while j <= b:
        print(' ', end="")
        j += 1
    j = 1
    while j <= s:
        print('*', end="")
        j += 1
    print()
    i += 1
