'''for _ in range(int(input())):
    n,m = map(int,input().split())
    a = sum(list(map(int,input().split())))
    x = a//m
    y = a - x*m
    print("Case #{0}: {1}".format(_+1,y))'''


'''def number_of_record_breaking_days(n, v):
    record_breaking_days = 0
    a_max = [0]
    a_max[0] = v[0]
    for i in range(1,len(v)):
        a = max(a_max[i-1],v[i])
        a_max.append(a)
    for j in range(1,n-1):
        if (v[j]>a_max[j-1] and v[j]>v[j+1]):
            record_breaking_days += 1
    if n == 1:
        record_breaking_days +=1
    if n> 1 and v[0] > v[1]:
        record_breaking_days += 1
    if n>=2 and v[n-1] > a_max[n-2]:
        record_breaking_days += 1
    return record_breaking_days

def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1, 1):
    number_of_days = int(input())
    vistors = list(map(int, input().split()))

    ans = number_of_record_breaking_days(number_of_days, vistors)

    print("Case #{}: {}".format(test_case, ans))

if __name__ == "__main__":
  main()'''


'''def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1):
        N, R, C, Sr, Sc = map(int, input().split())
        instructions = input()

        final_r, final_c = end_position(N, R, C, Sr, Sc, instructions)
        print(f'Case #{test_case}: {final_r} {final_c}')


def end_position(N, R, C, Sr, Sc, ns):
    l=[[Sr,Sc]]
    for i in range(N):
        if ns[i] == "S":
            Sr += 1
            while[Sr,Sc] in l:
                Sr += 1
        elif ns[i] == "N":
            Sr -= 1
            while[Sr,Sc] in l:
                Sr -= 1
        elif ns[i] == "E":
            Sc += 1
            while[Sr,Sc] in l:
                Sc += 1
        elif ns[i] == "W":
            Sc -= 1
            while[Sr,Sc] in l:
                Sc -= 1
        l.append([Sr, Sc])
    
    final_r, final_c = l[-1][0],l[-1][1]

    return final_r, final_c


if __name__ == '__main__':
    main()'''

'''def get_neighbor(r, c, i, neighbors):
    if (r, c, i) in neighbors:
        return neighbors[(r, c, i)]

    if i == 'N':
        return (r - 1, c)
    elif i == 'S':
        return (r + 1, c)
    elif i == 'E':
        return (r, c + 1)
    else:  # 'W'
        return (r, c - 1)


def link_neighbors(r, c, neighbors):
    north = get_neighbor(r, c, 'N', neighbors)
    south = get_neighbor(r, c, 'S', neighbors)
    east = get_neighbor(r, c, 'E', neighbors)
    west = get_neighbor(r, c, 'W', neighbors)

    neighbors[(*north, 'S')] = south
    neighbors[(*south, 'N')] = north
    neighbors[(*east, 'W')] = west
    neighbors[(*west, 'E')] = east


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N, R, C, r, c = map(int, input().split())
        instructions = input()  # string of N, S, E or W
        neighbors = {}

        for i in instructions:
            link_neighbors(r, c, neighbors)
            print(neighbors)
            r, c = get_neighbor(r, c, i, neighbors)  # new position
            print(r,c)

        print('Case #{}: {} {}'.format(case, r, c))


main()'''


'''z = 0
for _ in range(int(input())):
    if z >= 1:
        y = input()
    N = int(input())
    x = list(map(int,input().split()))
    P = int(input())
    l = []
    for i in range(P):
        count = 0
        c = int(input())
        for i in range(0,(2*N)-1,2):
            if c in range(x[i],x[i+1]+1):
                count += 1
        l.append(count)
    print('Case #{}: {}'.format(_+1,' '.join(map(str,l))))
    z += 1'''

    
# for _ in range(int(input())):
#     a,b,n,k = map(int,input().split())
#     l = [(i,j)for i in range(1,n+1) for j in range(1,n+1) if (i**a+j**b)%k == 0 and i != j]
#     x = len(l)%(10**9 + 7)
#     )
    

for _ in range(int(input())):
    c = []
    d = []
    u = []
    n = int(input())
    for p in range(n):
        l = [i for i in input().split(" ")]
        c.append(l[0])
        d.append(l[1])
        u.append(l[2])
    l1 = u[:]
    l2 = u[:]
    for i in range(len(c)-1):
        if c[i] > c[i+1]:
            temp = l1[i]
            l1[i] = l1[i+1]
            l1[i+1] = temp
    for i in range(len(d)-1):
        if d[i] > d[i+1]:
            temp = l2[i]
            l2[i] = l2[i+1]
            l2[i+1] = temp
    print(l1)
    print(l2)
    x = 0
    for i in range(len(u)):
        if l1[i] == l2[i]:
            x+=1   
    print('Case #{}: {}'.format(_+1, x))
        