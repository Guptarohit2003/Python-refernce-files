'''for _ in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    ocount = []
    ecount = []
    for i in A:
        if i%2 == 0:
            ecount.append(i)
        else:
            ocount.append(i)
    if len(ecount) > len(ocount):
        print(int((len(ecount)-len(ocount))/2))
    elif len(ecount) < len(ocount):
        print(int((len(ocount)-len(ecount))/2))
    else:
        print(0)
'''

def odd_conversion_count(x):
    c=0
    while x%2==0:
        x//=2
        c+=1
    return c

for _ in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))[:(2*N)]
    ocount = []
    ecount = []
    for i in A:
        if i%2 == 0:
            ecount.append(i)
        else:
            ocount.append(i)
    if len(ecount) < len(ocount):
        print((len(ocount)-len(ecount))//2)
    elif len(ecount) == len(ocount):
        print(0)     
    else:
        len(ecount) < len(ocount)
        need_alt=(len(ecount)-len(ocount))//2
        for i in range(len(ecount)):
            ecount[i]=odd_conversion_count(ecount[i])
        ecount.sort()
        ans=0
        for i in range(need_alt):
            ans+=ecount[i]
        print(ans)