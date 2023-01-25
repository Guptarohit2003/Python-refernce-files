'''for _ in range(int(input())):
    l,n = map(int,input().split())
    x = []
    y = []
    for i in range(n):
        d,c = input().split()
        x.append(int(d))
        y.append(c)
    count = 0
    z = []
    s = 0
    for i in range(len(x)):
        if y[i] == 'C':
            s+=x[i]
        else:
            s-=x[i]
        print(s)
        if abs(x[i]//l) > 1:
            if (y[i-1] == "A" and y[i] == "C") or (y[i-1] == "C" and y[i] == "A"):
                count-=1
            print("1",abs(x[i]//l))
            count+=abs(x[i]//l)
        if s - s%l not in z:
            if s -s%l !=0:
                z.append(s-s%l)
                print("2",s-s%l)
                count+=1
    print(f"Case #{_+1}: {count}")'''
'''for _ in range(int(input())):
    l,n = map(int,input().split())
    x = []
    y = []
    for i in range(n):
        d,c = input().split()
        x.append(int(d))
        y.append(c)
    count = 0
    z = []
    s = 0
    for i in range(len(x)):
        if y[i] == 'C':
            s+=x[i]
        else:
            s-=x[i]
        if abs(x[i]//l) > 1:
            count+=abs(x[i]//l)
        if s - s%l not in z:
            if s -s%l !=0:
                z.append(s-s%l)
                count+=1
    print(count)'''


for _ in range(int(input())):
    n = int(input())
    count = 14
    if n <= 13:
        print(n)
    elif 14<n<=20:
        if n == 14 or n == 15:
            print(13)
        elif n == 16 or n == 18:
            print(14)
        else:
            print(15)
    else:
        n = n-20
        k = 0
        for i in range(n+1):
            count += 1
            k += 1
            if k == 2:
                k = 0
                count -=1
        print(count)