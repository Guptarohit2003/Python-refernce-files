for _ in range(int(input())):
    n = int(input())
    count = 1
    ncount = 0
    bcount = 0
    while n !=0:
        if n <2:
            n = 0
        elif n < 10:
            ncount += count
            n = 0
            count-=count
        elif n < 26:
            bcount+=count
            n = 0
            count-=count
            #ncount-=1
        else:
            count =count*2
            #count -=1
            n-=26
    print(count,ncount,bcount,sep=" ")
