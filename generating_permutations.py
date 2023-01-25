#d c h b a e g l k o n m j i
# f j a d b i h g e c
def first_min(str):
    for i in range(len(str)-1,0,-1):
        if str[i] > str[i-1]:
            global x
            x = i-1
            print(str[x])
            print(x)
            return x

def func2(str):
    global x
    for i in range(x+1,len(str)):
        print(str[i])
        if str[x]>str[i]:
            print(str[x])
            k = str[x]
            str[x] = str[i-1]
            str[i-1] = k
            return str
        else:
            k = str[x]
            str[x] = str[-1]
            str[-1] = k
            return str

str = input().split()
x = 0
first_min(str)
func2(str)
s = str[x+1:]
s = s[::-1]
l = str[:x+1] + s
print(*l)



