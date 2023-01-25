def merge_the_tools(string, k):
    y = 0
    x = int(len(string )/k)
    z = k
    print(len(string))
    print(x)
    for i in range(x):
        l = [string[y:k]]
        t = ""
        for i in l[0]:
            if i in t:
                pass
            else:
                t += i
        print(t)
        y = k
        print(y)
        k +=z
        print(k)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    