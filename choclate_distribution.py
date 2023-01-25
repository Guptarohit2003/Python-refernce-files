n = list(map(int,input().split()))
m = int(input())
n.sort()
l = []
for i in range(len(n)-(m-1)):
    l.append(n[i:m+i])
p = []
a = 0
while a < len(l):
    p.append(max(l[a])-min(l[a]))
    a+=1
p, l = zip(*sorted(zip(p, l)))
print("Selected  packets of chocolates:",l[0])
print("Mininmum Distance:",p[0])
