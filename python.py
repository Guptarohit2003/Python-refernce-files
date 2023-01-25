'''import numpy as np
values = np.arange(100,200,10)
values = values.reshape(5,2)
values = values.reshape(1,-1)
print(values)'''

'''
n = input()
for i in range(len(n)):
    if n[i] == "A" or n[i] == "a":
        print(".-",end = "")
    if n[i] == "B" or n[i] == "b":
        print("-...",end = "")
    if n[i] == "c" or n[i] == "C":
        print("-.-.",end = "")
    if n[i] == "d" or n[i] == "D":
        print("-..",end = "")
    if n[i] == "E" or n[i] == "e":
        print(".",end = "")
    if n[i] == "F" or n[i] == "f":
        print("..-.",end = "")
    if n[i] == "G" or n[i] == "g":
        print("--.",end = "")
    if n[i] == "H" or n[i] == "h":
        print("....",end = "")
    if n[i] == "I" or n[i] == "i":
        print("..",end = "")
    if n[i] == "J" or n[i] == "j":
        print(".---",end = "")
    if n[i] == "K" or n[i] == "k":
        print("-.-",end = "")
    if n[i] == "L" or n[i] == "l":
        print(".-..",end = "")
    if n[i] == "M" or n[i] == "m":
        print("--",end = "")
    if n[i] == "N" or n[i] == "n":
        print("-.",end = "")
    if n[i] == "O" or n[i] == "o":
        print("---",end = "")
    if n[i] == "P" or n[i] == "p":
        print(".--.",end = "")
    if n[i] == "Q" or n[i] == "q":
        print("--.-",end = "")
    if n[i] == "R" or n[i] == "r":
        print(".-.",end = "")
    if n[i] == "S" or n[i] == "s":
        print("...",end = "")
    if n[i] == "T" or n[i] == "t":
        print("-",end = "")
    if n[i] == "U" or n[i] == "u":
        print("..-",end = "")
    if n[i] == "V" or n[i] == "v":
        print("...-",end = "")
    if n[i] == "W" or n[i] == "w":
        print(".--",end = "")
    if n[i] == "X" or n[i] == "x":
        print("-..-",end = "")
    if n[i] == "Y" or n[i] == "y":
        print("-.--",end = "")
    if n[i] == "Z" or n[i] == "z":
        print("--..",end = "")'''
# A	.-	B	-...	C	-.-.	D	-..	E	.	F	..-.
# G	--.	H	....	I	..	J	.---	K	-.-	L	.-..
# M	--	N	-.	O	---	P	.--.	Q	--.-	R	.-.
# S	...	T	-	U	..-	V	...-	W	.--	X	-..-
# Y	-.--	Z	--..
'''class X:
    def __init__(self, value):
        self.a = value
    def setval(self, value):
        self.a = value
    def display(self):
        print(self.a)
class Y:
    def __init__(self, value):
        self.b = value
    def setval(self, value):
        self.b = value
    def display(self):
        print(self.b)
def exchange(c1, c2):
    temp = c1.a
    c1.a = c2.b
    c2.b = temp
c1 = X(3)
c1.display()
c2 = Y(1)
c2.display()
exchange(c1, c2)
c1.display()
c2.display()'''


'''for _ in range(int(input())):
    N = int(input())
    m = input()
    l = []
    count = 0
    l[:0] = m
    if l[0] == '1':
        count+=1
    if l[-1] == '0':
        count +=1
    for i in range(len(l[0:-1])):
        if l[i] == '0'and l[i+1] == '1':
            count+=1
    print(count)
'''


'''for _ in range(int(input())):
    R,G,B = map(int,input().split())
    K = int(input())
    if K-min(R,G,B) <= 1:
        c = 3*(K-1)+1
    else:
        if R<B<G:
            c = 3*R + 2*(B-R) + (K-B)
        elif R<G<B:
            c = 3*R + 2*(G-R) + (K-G)
        elif B<G<R:
            c = 3*B + 2*(G-B) + (K-G)
        elif B<R<G:
            c = 3*B + 2*(R-B) + (K-R)
        elif G<R<B:
            c = 3*G + 2*(R-G) + (K-R)
        elif G<B<R:
            c = 3*G + 2*(B-G) + (K-B)
    print(c)'''

'''t= int(input())
for i in range(t):
    r,g,b=map(int,input().split())
    k= int(input())
    print(min(r,k-1)+min(g,k-1)+min(b,k-1)+1)'''

'''t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    i = 1
    while A != B and A < B:
        if i % 2 != 0:
            A = A+1
            i+=1
        else:
            A += 2
            i+=1
    if A == B:
        print("YES")
    else:
        print("NO")'''

'''def gcd(a,b):
    if b>a:
        return gcd(b,a)
    elif b==0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    x = gcd(a,b)
    n = a*b//x
    return n
for i in range(int(input())):
    X,R = map(int,input().split())
    if 2<= X <= 10**16 and 2<= R <= 10**16:
        i = 0
        for A in range(1,R+1):
            for B in range(A+1,R+1):
                if B == A+1:
                    LCM = lcm(A,B)
                else:
                    LCM = lcm(LCM,B)
                if LCM ==X:
                    i +=1
        print(i)'''

'''print("Enter the operation you want to perform: ")
print("1. To Add")
print("2. To Subtract")
print("3. To Multiply")
print("4. To Divide")
# 1. The user is asked to enter the choice of operation to be performed.
# 2. The user is asked to enter the two numbers.
# 3. The condition checks whether the numbers are 56 or 9 and 9 or 56.
# 4. If the condition is true, the print statement is executed and the result is printed.
# 5. If the condition is false, the print statement is not executed and the result is printed.
op = int(input("Enter your choice : "))
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
if op == 1:
    if num1 == 56 or 9 and num2 == 9 or 56:
        print(77)
    else:
        print(num1+num2)
if op == 2:
    print(num1-num2)
if op == 3:
    if num1 == 45 or 3 and num2 == 45 or 3:
        print(555)
    else:
        print(num1*num2)
if op == 4:
    if num1 == 56 or 6 and num2 == 6 or 56:
        print(4)
    else:
        print(56/4)'''

# average number
'''for _ in range(int(input())):
    n,k,v = map(int, input().split())
    x = list(map(int,input().split()))
    b = v*(n+k)
    a = b - sum(x)
    if a <= 0:
        print(-1)
    elif a%k == 0:
        print(int(a/k))
    else:
        print(-1)'''

'''from collections import Counter
t = int(input())
for _ in range(t):
    flag = False
    n = int(input())
    arr = [int(i) for i in input().split()]
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            if arr[i-1] in arr[i:]:
                flag = True
                break
    if flag:
        print('NO')
    else:
        dic = Counter(arr)
        l = list(dic.values())
        print(l)
        print(set(l))
        if len(l) != len(set(l)):
            print('NO')
        else:
            print('YES')'''

# depchef
'''for _ in range(int(input())):
    N = int(input())
    a = [ int(i) for i in input().split( )]
    d = [ int(i) for i in input().split( )]
    sum = -1
    for i in range(0,N):
        if a[i-1] + a[(i+1)%N] < d[i]:
            sum = max(sum, d[i])
    print(sum)'''


'''for _ in range(int(input())):
    N = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    if len(set(a)) == 1:
        print(a[0])
    else:
        l = [a.count(a[i]) for i in range(len(a))]
        print(l)
        l.sort()
        print(l)
        j = l
        l = set(l)
        print(l)
        print(j)
    for i in range(len(a)):
        if a.count(a[i]) == max(l):
            print(a[i])
        '''


# Time Complexity: O(n^2)
'''for i in range(1, 10):
    print("i =", i, ":", end=" ")
    for j in range(1, 10):
        print("{:2d}".format(i * j), end=" ")
    print()'''

# RECNDNOS
'''from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            arr[i] = 0
    print(arr)
    dic = Counter(arr)
    print(dic)
    l = list(dic.items())
    print(l)
    l.sort(key = lambda x : (-x[1],x[0]))
    print(l)
    if l[0][0] == 0:
        print(l[1][0])
    else:
        print(l[0][0])'''

'''class phone:
    def __init__(self,number):
        self.number = number

    def turn_on(self):
        return print("mobile phone {} is turned on".format(self.number))

    def turn_off(self):
        return print("mobile phone is turned off")

    def call(self,number):
        return print("calling {} ".format(number))

p1 = phone(934324324)
p2 = phone(453594305)
p1.turn_on()
p2.turn_on()
p1.call(32432443534)
p1.turn_off()
p2.turn_off()'''


'''class Demo:
    class_var = 'shared variable'

d1 = Demo()
d2 = Demo()

print(Demo.class_var)
print(d1.class_var)
print(d2.class_var)

print('contents of d1:', d2.__dict__)'''

'''class Phone:
    counter = 0

    def __init__(self, number):
        self.number = number
        Phone.counter += 1

    def call(self, number):
        message = 'Calling {} using own number {}'.format(number, self.number)
        return message


class FixedPhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        FixedPhone.last_SN += 1
        self.SN = 'FP-{}'.format(FixedPhone.last_SN)


class MobilePhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        MobilePhone.last_SN += 1
        self.SN = 'MP-{}'.format(MobilePhone.last_SN)


print('Total number of phone devices created:', Phone.counter)
print('Creating 2 devices')
fphone = FixedPhone('555-2368')
mphone = MobilePhone('01632-960004')

print('Total number of phone devices created:', Phone.counter)
print('Total number of mobile phones created:', MobilePhone.last_SN)

print(fphone.call('01632-960004'))
print('Fixed phone received "{}" serial number'.format(fphone.SN))
print('Mobile phone received "{}" serial number'.format(mphone.SN))'''

'''import random


class Apple:
    counter = 0
    total_weight = 0

    def __init__(self,weight):
        self.weight = weight
        Apple.total_weight += weight
        Apple.counter +=1

while Apple.total_weight<300 and Apple.counter<1000:
    apple = Apple(random.uniform(0.2,0.5))


print('A limit has been reached. The order details:')
print('# of apples:', Apple.counter)
print('total weight:', round(Apple.total_weight, 2))'''


'''def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]

        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))

    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)'''


'''for _ in range(int(input())):
    X, Y, N, R = map(int, input().split())
    if X * N > R:
        print(-1)
    elif Y * N <= R:
        print("0", N)
    else:
        y = (R - N*X) // (Y-X)
        x = N-y
        print(x, y)'''

'''def f(n):
    s=0
    for i in range(1,n+1):
        if n//i == i and n%i == 0:
           s = 1
    return(s%2 == 1)

print(f(4))'''


'''#User function Template for python3
class Solution:
    def solve(self, N, K, A):
        a = set(A)
        a = list(a)
        l = [i for i in range(10**5)]
        for i in range(len(a)):
            l.remove(a[i])
        return l[k-1]
        # if l[k] not in A:
        #     return(l[k])
        # elif N == 1 and k ==1:
        #     return(l[0])
        # else:
        #     return(l[k+1])


# {
#  Driver Code Starts
# Initial Template for Python 3

for _ in range (int(input())):
    n,k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    sol = Solution()
    print(sol.solve(n,k,a))
# } Driver Code Ends'''

# x = 20
# b = [5,10,15,20,25]
# for i in range(len(b)):
#     z = int(bin(x)[2:])
#     y =  int(bin(b[i])[2:])
#     print(y)
#     print(z)
#     print(x^b[i])
#     print(y^z)


# for _ in range(int(input())):
#     n,m = map(int,input().split())
#     if n == m:
#         print("Tonya")
#     elif m == n+1 or n == m+1:
#         print("Burenka")
#     else:
#         print("Burenka")

# from itertools import product
# for _ in range(int(input())):
#     n,k = map(int,input().split())
#     s = []
#     x = [i for i in range(1,n+1)]
#     l = list(product(x,repeat=2))
#     for i in range(len(l)-1):
#         for j in range(2):
#             print(l[i][j])
#             if l[i][j] in s:
#                 l.pop(i)
#             else:
#                 s.append(l[i][j])


#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

'''def checkMagazine(magazine, note):

    for i in range(len(note)):
        if note[i] in magazine:
            magazine.remove(note[i])
        else:
            return False
    return True
    # Write your code here

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    if len(magazine) == len(note):
        if len(set(magazine)) == len(set(note)):
            print("Yes")
        else:
            print("No")
    else:
        x = checkMagazine(magazine, note)
        if (x):
            print("Yes")
        else:
            print("No")'''


'''class Evenstream(object):
    def __init__(self):
        self.x  = 0

    def get_next(self):
        y = self.x
        self.x += 2
        return y
class Oddstream(object):
    def __init__(self):
        self.x = 1

    def get_next(self):
        y =self.x
        self.x += 2
        return y

def print_from_stream(n, stream = None):
    if stream is None:
        stream = Evenstream()

    for _ in range(n):
        print(stream.get_next())

for _ in range(int(input())):
    a,b = input().split()
    b = int(b)
    if a == "even":
        print_from_stream(b)
    else:
        print_from_stream(b, Oddstream())'''

from dbm import ndbm
import math
from operator import xor
import os
import random
import re
import sys
from collections import Counter, OrderedDict, deque
import cmath
import math
from tkinter import N

'''b = ('blue','red','green','yellow','silver')
for i,col in enumerate(b):
    print(i,col)'''

'''x = int(input())
l = Counter(list(map(int,input().split())))
n = int(input())
sum = 0
for i in range(n):
    a,b = map(int,input().split())
    if l[a]:
        sum += b
        l[a]-=1
print(sum)'''

'''x = complex(input())
print(abs(complex(x.real,x.imag)))'''

'''for _ in range(int(input())):
    l = list(map(int,input().split()))
    flag = 1
    if int((l[0] + l[1])/2) < 35 or int((l[0] + l[2])/2) < 35  or int((l[2] + l[1])/2) < 35 :
        print("Fail")
    else:
        print("Pass")'''

'''for _ in range(int(input())):
    x,y = map(int,input().split())
    if x == y:
        print("Yes")
    elif (max(x,y) - min(x,y))%2 == 0:
        print("Yes")
    else:
        print("No") '''


'''from collections import Counter
for _ in range(int(input())):
    n = int(input())
    z = list(map(int,input().split()))
    x = Counter(z).most_common(1)[0][1]
    if x > int(len(z)/2)+1:
        print("No")
    else:
        print("Yes")'''

    
'''def sum(a,b):
    return a+b

l = []
for _ in range(int(input())):
    a,b = map(int,input().split())
    c = sum(a,b)
    l.append(c)
print(l)'''

'''for tc in range(int(input())):
    ans = 0
    n = int(input())
    for i in range(n):
        s = int(input(),36)
        ans = ans ^ s
    print(str(bin(ans)).count("1"))'''


# for _ in range(int(input())):
#     n = int(input())
#     l = list(map(int,input().split()))
#     l = l.sort()
#     c = 0
#     for i in range(1,n):
#         if l[i] == l[i-1]:
#             c+=1
#     if c == 0 and n%2 !=0:
#         print("NO")
#     else:
#         print("YES")

'''N = int(input())
lst = []
i = 1
for i in range(N):
    command = input()
    if command == "print":
        print(lst)
    elif command == "sort":
        lst.sort()
    elif command == "pop":
        lst.pop()
    elif command == "reverse":
        lst.reverse()
    elif command[0:6] == "append":
        lst.append(int(command[7]))
    elif command[0:6] == "remove":
        lst.remove(int(command[7]))
    elif command[0:6] == "insert":
        ind = int(command[7])
        val = int(command[9:999])
        lst.insert(ind,val)'''


# Time Complexity: O(n)

'''n = int(input())
arr = list(map(int,input().split()))
arr_2 = list(map(int,input().split()))

prev_state = 0
final = abs(arr[0]-arr_2[0]) #initial conditions
for i in range(1,n):
    vertical_place = final + abs(arr[i]-arr_2[i])
    print(vertical_place)   
    horizontal_place = prev_state + abs(arr[i] - arr[i-1]) + abs(arr_2[i] - arr_2[i-1])
    prev_state = final
    print(horizontal_place)
    final = max(vertical_place,horizontal_place)
    print(final)
    print("---------")'''


'''def max3bad(x,y,z):
  maximum = 0
  if x >= y:
    if x >= z:
      maximum = x
  elif y >= z:
    maximum = y
  else:
    maximum = z
  return(maximum)
print(max3bad(20,10,30))'''

'''def mergebad(l1,l2):

  (lmerged,i,j) = ([],0,0)

  while i+j < len(l1) + len(l2):
    if i == len(l1):
      lmerged.append(l2[j])
      j = j+1
    elif j == len(l2):
      lmerged.append(l1[i])
      i = i+1
    elif l1[i] < l2[j]:
      lmerged.append(l1[i])
      i = i+1
    elif l2[j] < l1[i]:
      lmerged.append(l2[j])
      j = j+1
    else:
      lmerged.append(l1[i])
      i = i+1
      j = j+1
    
  return(lmerged)    

def mergesortbad(l):
  if len(l) < 2:
    return(l)
  else:
    n = len(l)
    leftsorted = mergesortbad(l[:n//2])
    rightsorted = mergesortbad(l[n//2:])
    return(mergebad(leftsorted,rightsorted))

l = [1,1,1,1,1,1,1,1]
print(mergesortbad(l))'''

'''def max4(w,x,y,z):
    if w>=x and w>=y and w>=z:
        maximum = w
    elif x > w and x>y and x>z:
        maximum = x
    elif y > w and y>x and y>z:
        maximum = y
    else:
        maximum = z
    return(maximum)

print(max4(32,12,16,11))'''

'''def mypalindrome(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(l == l[::-1])


print(	
mypalindrome([13,14,13]))'''



'''def perfect(n):
    sum = 0
    for i in range(1,n//2+1):
        if n%i == 0:
            sum += i
    return(sum == n)

print(perfect(28))'''

'''x =1
while 1:
    n = input()
    if n == " ":
        break
    if x%3 == 0:
        print(n)
    x+=1'''


'''def repeated(l):
    s = set(l)
    n = 0
    for i in s:
        if l.count(i) > 1:
            n+=1
    
    return n

print(repeated(["the","higher","you","climb","the","further","you","fall"]))
'''



'''def f(n): 
    s=0
    for i in range(1,n+1):
        if n//i == i and n%i == 0:
           print(i)
           s = 1
    return(s%2 == 1)

print(f(16))'''


'''def leftrotate(m):
    size = len(m)
    rotated_m = []
    for i in range(size):
        rotated_m.append([])
    for c in range(size-1,-1,-1):
        for r in range(size):
            print(size-(c+1))
            rotated_m[size-(c+1)].append(m[r][c])
    return(rotated_m)


print(leftrotate([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]))'''

'''def uncommon(l1,l2):
    l = []
    s1 = set(l1)
    s2 = set(l2)
    for i in s1:
        if i not in l2:
            l.append(i)
    for i in s2:
        if i not in l1:
            l.append(i)
    l.sort()
    return(l)

print(uncommon([2,2,4],[1,3,3,4,5]))'''



'''l = []
while True:
    ip = input()
    if ip == "":
        break
    else:
        l.append(ip)
for i in range(len(l+1)):
    if i%2 == 0:
        print(l[i])
for i in range(len(l+1)):
    if i %2 != 0:
        print(l[i])'''




'''def minbad(l):
  mymin = l[-len(l)]
  for i in range(-len(l),-1):
    if l[i] < mymin:
       mymin = l[i]
  return(mymin)

l = [2,3,4,0,1]
print(minbad(l))'''

'''def stablesortbad(l):
  for j in range(len(l)-1):
    for i in range(len(l)-1):
      if l[i][1] >= l[i+1][1]:
        (l[i],l[i+1]) =  (l[i+1],l[i])
  return(l)

l = [(45,2),(20,1),(13,4),(1,2)]
print(stablesortbad(l))
'''

'''def thirdmax(l):
    (mymax,mysecondmax,mythirdmax) = (0,0,0)
    for i in range(len(l)):
        l.sort()
        mythirdmax = l[2]
        break
    return(mythirdmax)'''

'''def squarefree(n):
    for i in range(2,n//2):
        if n%(i**2) == 0:
            return False
    else:
        return True

print(squarefree(48))'''

'''def disjointlist(l1,l2):
    s1 = set(l1)
    s2 = set(l2)
    flag = False
    for i in s1:
        if i in l2:
            flag = True
    for i in s2:
        if i in l1:
            flag = True
    if flag:
        return False
    else:
        return True

print(	
disjointlist([1,2,3,4],[2,2]))'''


'''l = []
while True:
    ip = input()
    if ip == "":
        break
    else:
        l.append(ip)
n = len(l)
for i in l[n//2:]:
    print(i)
for i in l[:n//2]:
    print(i)'''

'''def intreverse(n):
    n= str(n)
    x=" "
    for i in range(1, len(n)+1):
        x = x+n[-i]

    return x

print(intreverse(783))'''



'''wickets = {"Tests":{"Bumrah":[3,5,2,3],"Shami":[4,4,1,0],"Ashwin":[2,1,7,4]},"ODI":{"Bumrah":[2,0],"Shami":[1,2]}}

wickets["ODI"]["Ashwin"] = [4,4]
print(wickets)'''


# def fmin(l):
#     m = min(l)
#     for i in range(len(l)):
#         if l[i] == m:
#             temp = l[i]
#             l[i] = l[0]
#             l[0] = temp
#             return

# def isort(l):
#     if l == []:
#         return l
#     else:
#         fmin(l)
#         return (l[:1] + isort(l[1:]))

# l = [34,22,1,3,56,12,96,9,23,3,1,23,4,54,342]
# print(isort(l))


'''n = int(input())
arr = list(map(int,input().split()))
arr_2 = list(map(int,input().split()))

prev_state = 0
final = abs(arr[0]-arr_2[0]) #initial conditions
for i in range(1,n):
	vertical_place = final + abs(arr[i]-arr_2[i])
	horizontal_place = prev_state + abs(arr[i] - arr[i-1]) + abs(arr_2[i] - arr_2[i-1])
	prev_state = final 
	final = max(vertical_place,horizontal_place)
print(final)'''

'''def func(x,count=0):
    if x-25 < 0 and x%25==0:
        return count
    elif x-25 < 0 and x%25 !=0:
        return count+1
    else:
        x -= 25
        count +=1
        return(func(x,count))
    
print(func(1))
print(func(34))
print(func(150))
print(func(74))'''

'''
a = [1,3,2,1,2,2]
s = set(a)
max= 0
for i in s:
    if a.count(i) > max:
        max = a.count(i)
print(len(a)-max)'''
    
# from collections import Counter
# for _ in range(int(input())):
#     n = int(input())
#     l = list(map(int,input().split()))
#     if len(set(l)) == len(l):
#         print(0)
#     elif len(set(l)) == 1:
#         print(n-1)
#     else:
#         test_list = Counter(l)
#         print(test_list)
#         res = test_list.most_common(1)[0][0]
#         res2 = test_list.most_common(2)[0][1]
#         print(res)
#         print(res2)
#         print(l.count(res)-l.count(res2))



# n,m = map(int,input().split())
# a = set(map(int,input().split()))
# b = set(map(int,input().split()))
# c = set(map(int,input().split()))
# score = 0
# for i in a:
#     if i in b:
#         score+=1
#     elif i in c:
#         score-=1
# # x = len(a.intersection(b))
# # y = len(a.intersection(c))
# # print(x)
# # print(y)
# # score = x-y
# pri9nt(score)


# def reverse(string):
#     s = string.split()
#     s = s[::-1]
#     return s
# s = "hello i m python"
# print(*reverse(s))


# for _ in range(int(input())):
#     a = input()
#     x = ["a","e","i","o","u"]
#     count = 0
#     for i in range(len(a)-1):
#         if a[i] in  x:
#             count += 1
#             if count >2:
#                 print("Happy")
#                 break
#         elif a[i] not in x:
#             count = 0
#     else:
#         print("Sad")

# count = 0
# for i in range(3):
#     for j in range(11):
#         for k in range(11):
#             print(i,j,k)
#             count+=1
# print(count)

# def changestate(curr_stage):
#     if curr_stage == "y":
#         curr_stage = "z"
#     else:
#         curr_stage = "y"
#     return curr_stage
# curr = "y"
# changestate(curr)
# print(curr)

# for _ in range(int(input())):
#     n = int(input())
#     s = input()
#     x = []
#     x.append(s[0])
#     for i in range(1,n):
#         if s[i] == '1':
#             break
#         else:
#             x.append(s[i])
#     print(len(x))
    
'''def power(b,n):
    s=1
    while(n):
        if n%2 == 1:
            s = s*b%998244353
        b = b*b%998244353
        n/=2
    return s

def count(i,j):
    return((i//(1<<(j+1)))<<j) + (max(0,i%(1<<(j+1))-(1<<j)+1))

for _ in range(int(input())):
    n,m = map(int,input().split())
    s=0
    for i in range(31):
        s = (s+(power(count(m,i),n)<<i)%998244353)%998244353
    print(s)'''

'''l = [12,10,20]
p = [8, 34, 50]
d = {}
for i in range(len(l)):
    d[l[i]] = p[i]
dict1 = dict(sorted(d.items()))
x = list(dict1.keys())
y = list(dict1.values())
print(x,y)'''


'''n,m = input().split()
n = int(n)
if m == "Clothing" and n>= 1000:
    print(n - n*0.1)
elif m == "Accessories" and n >= 1500:
    print(n-n*0.15)
elif m == "Home" and n >= 2000:
    print(n-n*0.2)
else:
    print(n - n*0.05)'''

'''n = list(map(str,input().split()))
for i in range(1,4):
    print(*n[0:6:i])'''
 
#red blue white green black grey


'''l = list(map(int,input().split()))
v = map(str, l)
x = []
char = "a"
k = ord(char[0])
for i in v:
    if int(i[::-1]) in l:
        x.append(str(int(i[0])+int(i[1]))+char)
        k+=1
        char = chr(k)
    else:
        x.append(int(i[0])+int(i[1]))
        k+=1
        char = chr(k)
print(*x)  '''  

'''for _ in range(int(input())):
    x,y = map(int,input().split())
    x = int(x)
    y = int(y)
    if x>y:
        print("YES")
    else:
        print("NO")'''

'''for _ in range(int(input())):
    a,b,x,y = map(int,input().split())
    temp = a-b
    if temp == 0:
        print("YES")
    elif temp<0:
        if abs(temp) <= x:
            print("YES")
        else:
            print("NO")
    else:
        if abs(temp)<= y:
            print("YES")
        else:
            print("NO")'''

'''for _ in range(int(input())):
    n = int(input())
    s = input()
    x = set(s)
    l = 1
    for i in x:
        if s.count(i)%2 != 0:
            l = 0
            break
    if l == 0:
        print("NO")
    else:
        print("YES")'''

'''def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n*factorial(n-1)

for _ in range(int(input())):
    mod = 7 + (10)**9
    n = int(input())
    x = list(map(int,input().split()))
    l = []
    s = set(x)
    sum = 0
    for i in s:
        sum += factorial(i)*(x.count(i))%mod
    print(sum%mod)'''

# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)

#     print(start)

#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited


# graph = {'0': set(['1', '2']),
#          '1': set(['0', '3', '4']),
#          '2': set(['0']),
#          '3': set(['1']),
#          '4': set(['2', '3'])}

# dfs(graph, '0')


# importing tkinter module
'''from tkinter import *
 
# creating Tk() variable
# required by Tkinter classes
master = Tk()
 
# Declaration of Tkinter variables
intvar = IntVar()
strvar = StringVar()
boolvar = BooleanVar()
doublevar = DoubleVar()
 
# Initialization of Tkinter variables
# using set() method
intvar.set(100)
strvar.set("GFG")
boolvar.set(False)
doublevar.set(10.36)
'''

# numbers = [2,3,4]
# target = 6
# # nums = list(set(numbers))
# # nums.sort()
# # for i in range(len(nums)):
# #     for j in range(i,len(nums)):
# #         if nums[i] + nums[j] == target and i!=j:
# #             x = i+1
# #             y = j+1
# #             temp = i
# #             break 
# # for i in range(temp):
# #     x+= numbers.count(nums[i])
# #     y+= numbers.count(nums[i])
# # print(x,y)                
#         for i in range(-10,target+1):
#             if i in numbers and target - i in numbers:
#                 return numbers.index(i)+1,numbers[numbers.index(i)+1:].index(target-i)+1+numbers.index(i)+1

'''s = ["h","e","l","l","o"]
x = len(s) -1
while x>=0:
    y = s.pop(x)
    s.append(y)
    x-=1
print(s)'''

'''s = "Let's take LeetCode contest"
l = s.split(" ")
for i in range(len(l)):
    l[i]= list(reversed(l[i]))
x = ''
count = 0
for i in l:
    if count != 0:
        x += " "
    for j in i:
        x += j
    count=1
print(x)
'''
'''prices = [7,6,4,3,1]
n = prices[0]
max_profit = 0
for i in prices:
    if i<n:
        n = i
    else:
        max_profit = max(max_profit,i-n)'''
'''mat = [[1,2],[3,4]] 
r =  1
c = 4
# vals =(val for row in mat for val in row)
# print([[next(vals) for col in range(c)] for row in range(r)])
vals =[val for row in mat for val in row]
ans = [[None for _ in range(c)] for _ in range(r)]
count = 0
for i in range(r):
    for j in range(c):
        ans[i][j] = vals[count]
        count+=1
print(ans)'''
'''def substrings(s,n):
    l = []
    for i in range(n):
        for j in range(i+1,n+1):
            l.append(s[i:j])
    return l

def filt(a):
    p = ''
    for i in a:
        if i not in p:
            p = p+i
    return p

def lengthOfLongestSubstring(s: str) -> int:
    a = substrings(s,len(s))
    # print(a)
    b = []
    for i in a:
        i = filt(i)
        if i not in b:
            b.append(i)
    b = sorted(b,key=len)
    return b   


s = 'pwwkew'
print(lengthOfLongestSubstring(s))'''
'''def generate(numrows):
    l = []
    if numrows == 1:
        return [[1]]
    else:
        for i in range(numrows+1):
            l.append([])
            for j in range(i):
                if j == 0:
                    l[i].append(1)
                elif j == i-1:
                    l[i].append(1)
                else:
                    z = l[i-1][j-1] + l[i-1][j]
                    l[i].append(z)
        l.pop(0)
        return l

print(generate(1))'''

s = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

# def is_valid(s):
#     for i,row in enumerate(s):
#         for j,c in enumerate(row):
#             if c!= ".":
#                 print(i,row,j,c)
# is_valid(s)



def isValidSudoku(board):
    seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
                for i, row in enumerate(board)
                for j, c in enumerate(row)
                if c != '.'), [])
    print(seen)
    return len(seen) == len(set(seen))


print(isValidSudoku(s))






















