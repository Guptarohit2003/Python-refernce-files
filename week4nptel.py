'''def frequency(l):
    m = [0]
    k = [0]
    n = [100]
    o = [0]
    s = set(l)
    for i in s:
        freq = 0
        for j in l:
            if j == i:
                freq +=1
        if m[-1] < freq:
            m[-1] = freq
            k[-1] = i
        elif m[-1] == freq:
            m.append(freq)
            k.append(i)
        if n[-1] > freq:
            n[-1] = freq
            o[-1] = i
        elif n[-1] == freq:
            n.append(freq)
            o.append(i)
    if len(set(m)) != 1:
        for i in range(len(m)-1,0,-1):
            if m[i-1] < m[i]:
                m.pop(i-1)
                k.pop(i-1)
    if len(set(n)) != 1:
        for i in range(len(n)-1,0,-1):
            if n[i-1] > n[i]:
                n.pop(i-1)
                o.pop(i-1)
    return (o,k)'''


def frequency(l):
    s = set(l)
    x = list(s)
    n = []
    for i in x:
        n.append(l.count(i))
    mi = min(n)
    ma = max(n)
    z = []
    y = []
    for j in range(len(n)):
        if n[j]==mi:
            z.append(x[j])
        if n[j] == ma:
            y.append(x[j])
    return (sorted(z),(sorted(y)))


def onehop(l):
    x = []
    l = sorted(l)
    for i in l:
        for j in l:
            if i !=j:
                if i[1] == j[0] and i[0] != j[1]:
                    z = (i[0],j[1])
                    if z not in x:
                        x.append(z)
    return sorted(x)




print(frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7]))