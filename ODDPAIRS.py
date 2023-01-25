for _ in range(int(input())):
    n = int(input())
    odd = n//2
    even = n//2

    if n%2 != 0:
        odd +=1
    
    print(2*odd*even)