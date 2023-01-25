# list of programs
# 1 types of data types
'''a = 1
b = "string"
c = True
d = 2+3j
e = 6.9
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))'''

# 2 diffrent arithmetic operations
'''def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def floor_div(a,b):
    return a//b
def mod(a,b):
    return a%b
def sub(a,b):
    return max(a,b) - min(a,b)

a,b = map(int,input().split())
print("addition of a &b is :", add(a,b))
print("subtraction of a &b is :", sub(a,b))
print("multiplication of a &b is :", mul(a,b))
print("division of a &b is :", div(a,b))
print("floor division of a &b is :", floor_div(a,b))
print("modulus of a &b is :", mod(a,b))
print("exponential a of b is:", b**a)'''

#3 create concatenate print a string and access substrings

'''s = "Welcome to MITS "
p = "Python Lab"
x = s+p
print(x)
l = x.split()   
print(l)
y = x[11:15]
print(y)'''

#4 create append and remove from the list

'''l = [1,4,9,16,25,36,49,64]
l.append(81)
print(l)
l.pop(0)
print(l)
l.remove(49)
print(l)'''

#5 working with tuples

'''x = 3,2,5,6,1,4,1,1,2,1
y = (7,8,9,10,11,12)
print(type(x))
print(type(y))
print(len(x))
print(any(x))
print(sorted(x))
print(x.count(1))
print(x.index(6))
z = x + y
print(z)
print(type(z))'''

#6 working with dictionaries

'''d = {"one":1,2:"two","x":"y"}
print(len(d))
print(any(d))
#print(sorted(d))
print(list((d.keys())))                                                                                                                                  
print(d.values())
print(d.pop(2))
print(d.popitem())
s = {"new":7}
print(d.update(s))
print(d)'''

#7 factorial using recursion

'''def fact(n):
    if n == 1 or n ==0:
        return 1
    else:
        return n*fact(n-1)

a = int(input())
if a<0:
    print("No factorial of Negative number")
else:
    print("factorial is:",fact(a))
'''
#8 swapping  two numbers

'''a = int(input())
b = int(input())
print("Initial A:",a)
print("Initial B:",b)
a += b
b = a-b
a = a - b
print("Final A:",a)
print("Final B:",b)
'''
#9 read content of file and write into another file

with open('C:\PROFO\python\python practice/textfiles/file3.txt','r') as f1:
    with open('C:\PROFO\python\python practice/textfiles/file4.txt','w') as f2:
        count = 1
        for line in f1:
            print("line"+str(count)+" coppied successfully")
            count+=1
            f2.write(line)


#10 import self defined module and use its function 

'''import module1                                                                       
a = int(input())
b = int(input())
print(module1.add(a,b))
print(module1.func())'''



# Below part is not the part of python file


'''for _ in range(int(input("Enter number of elements"))):
    l = []
    index = -1
    a = int(input())
    for i in range(len(l)):
        if l[i] > a:
                index = i
                break
        l.insert(index, a)
print(l)

#mean
def mean(l):
    sum = 0
    for i in l:
        sum+=l
    return sum/len(l)

def mode(l):
    freq = 0
    num = l[0]
    for i in l:
        if l.count(i) > freq:
            freq = l.count(i)
            num = i
    return num
l = [10,10,10,20,30,40,20,20,20]
print(mode(l))'''



























