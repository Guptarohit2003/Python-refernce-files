'''for _ in range(int(input())):
    N = int(input())
    H = list(map(int,input().split()))
    s = set(H)
    x = [H.count(i) for i in s]
    s1 = set(x)
    if len(s1) == 1 and x[0] > 1:
        print("0")
    elif len(H) == len(s):
        if len(H) %2 != 0:
            print((len(H)+1)//2 )
        else:
            print(len(H)//2)
    else:
        if x.count(1) == 1:
            print("1")
        else:
            print(x.count(1)-1)'''


'''from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    x = list(Counter(arr).keys())
    y = list(Counter(arr).values())
    count = 0
    c2 = 0
    f=len(y)
    flag=0
    w = 0
    for i in range(f):
        if y[i]==1:
            count+=1
            w=i
        if y[i]==2:
            c2+=1
    if count == 1:
        if int(x[w])==max(arr) and c2==f-1:
            print("2")
            flag = flag + 1
    if flag==0:
        print((count+1)//2)'''

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
 
List = [2, 1, 2, 2, 1, 3,1,1]
print(most_frequent(List))