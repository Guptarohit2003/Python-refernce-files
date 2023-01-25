def solve():
    n = int(input())
    s0 = 0
    s1 = 0
    s = 0
    l = list(map(int,input().split()))
    for i in range(n-1):
        if l[i] == 0:
            s0 += l[i]
        else:
            s1 += l[i]
    for i in range(1,n):
        if i ==1:
            s += l[1] == l[n]
        else:
            s+=l[i] == l[i-1]
    
    s -= abs(s0-s1)
    print("Bob" if s%4==0 else "Alice")

for _ in range(int(input())):
    solve()
        
    

