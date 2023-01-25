for _ in range(int(input())):
    s = input()
    t = {}
    total = 0
    for i in s:
        if i.isalpha():
            if i in t:
                t[i] +=1
            else:
                t[i] = 1
    values = t.values()
    for i in values:
        if i %2 == 0:
            total += i/2
        else:
            total += (i+1)/2
    print(total)


# for _ in range(int(input())):
#     s = input()
#     st = set(s)
#     total = 0
#     for i in st:
#         if i.isalpha():
#             c = s.count(i)
#             if c%2 == 0:
#                 total += c//2
#             else:
#                 total += (c+1)//2
#     print(total)