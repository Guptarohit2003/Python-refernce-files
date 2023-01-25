for _ in range(int(input())):
    stu = []
    for l in range(int(input())):
        stu.append(list(map(int,input().split()))[1:])
    x = False
    for s in stu:
        for d in stu:
            if s!=d:
                if {1,2,3,4,5}.issubset(s+d):
                    x = True
                    break
        
        if x:
            break
    if x:
        print("YES")
    else:
        print("NO")