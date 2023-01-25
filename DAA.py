from datetime import time,date
#BUbble Sort

# Date = date(2022,8,16)
# Time = time(15,22,5)
# def bubble_sort(n):
#     for i in range(len(n)-1):
#         for j in range(len(n)-1):
#             if n[j] > n[j+1]:
#                 n[j],n[j+1] = n[j+1],n[j]
#     return n
# n = [23,1,5,34,6,90,37,56]
# print("Sorted array is:")
# print(bubble_sort(n))
# print("\t\t\tName:Rohit Gupta")
# print(f"\t\t\tDate:{Date}")
# print(f"\t\t\tTime:{Time}")

#Merge Sort


# Date = date(2022,8,16)
# Time = time(16,25,21)
# def Merge_sort(array):
#     if len(array) > 1:
#         m = len(array)//2
#         l = array[:m]
#         r = array[m:]

#         Merge_sort(l)
#         Merge_sort(r)

#         i = j = k =0
        
#         while i < len(l) and j < len(r):
#             if l[i] < r[j]:
#                 array[k] = l[i]
#                 i += 1
#             else:
#                 array[k] = r[j]
#                 j+=1
#             k+=1
        
#         while i < len(l):
#             array[k] = l[i]
#             k += 1
#             i +=1

#         while j < len(r):
#             array[k] = r[j]
#             k+=1
#             j+=1

# def print_list(arr):
#     for i in range(len(arr)):
#         print(arr[i],end = " ")
#     print()

# n = [23,1,5,34,6,90,37,56]
# Merge_sort(n)
# print("Sorted array is:")
# print_list(n)
# print("\t\t\tName:Rohit Gupta")
# print(f"\t\t\tDate:{Date}")
# print(f"\t\t\tTime:{Time}")
       
#selection Sort

# Date = date(2022,8, 2)
# Time = time(16,11,50)
# def select_sort(arr):
#     for i in range(len(arr)):
#         min = i

#         for j in range(i+1,len(arr)):
#             if arr[j] < arr[min]:
#                 min = j
#         arr[i] , arr[min] = arr[min], arr[i]

# n = [23,1,5,34,6,90,37,56]
# select_sort(n)
# print(n)
# print("\t\t\tName:Rohit Gupta")
# print(f"\t\t\tDate:{Date}")
# print(f"\t\t\tTime:{Time}")

#quick sort


# Date = date(2022,8, 16)
# Time = time(16,10,9)
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quicksort(left) + middle + quicksort(right)

# l = [4,9,2,1,5,3]
# print("Sorted array is:")
# print(quicksort(l))
# print("\t\t\tName:Rohit Gupta")
# print(f"\t\t\tDate:{Date}")
# print(f"\t\t\tTime:{Time}")

#insertion sort


# Date = date(2022,8, 2)
# Time = time(15,18,21)
# def insertionsort(array):

#     for i in range(1,len(array)):
#         key = array[i]
#         j = i-1
        
#         while j>=0 and key<array[j]:
#             array[j+1] = array[j]
#             j = j-1
        
#         array[j+1] = key

# l = [4,9,2,1,5,3]
# insertionsort(l)
# print("Sorted array is:")
# print(l)
# print("\t\t\tName:Rohit Gupta")
# print(f"\t\t\tDate:{Date}")
# print(f"\t\t\tTime:{Time}")

#bucket sort

# Date = date(2022,8,16)
# Time = time(16,40,15)
# def bucket_sort(arr):
#     bucket = []

#     for i in range(len(arr)):
#         bucket.append([])

#     for j in arr:
#         ind_b = int(10*j)
#         bucket[ind_b].append(j)

#     for i in range(len(arr)):
#         bucket[i] = sorted(bucket[i])

#     k = 0
#     for i in range(len(arr)):
#         for j in range(len(bucket[i])):
#             arr[k] = bucket[i][j]
#             k+=1
#     return arr    
    

# array = [.42, .32, .33, .52, .37, .47, .51]
# print("Sorted array is:")
# print(bucket_sort(array))
# print("\t\t\tName:Rohit Gupta")
# print(f"\t\t\tDate:{Date}")
# print(f"\t\t\tTime:{Time}")


#heap sort


# Date = date(2022,8,16)
# Time = time(16,56,45)
# def heapify(arr, n, i):
#     largest = i
#     l = 2*i +1
#     r = 2*i +2

#     if l < n and arr[i] < arr[l]:
#         largest = l

#     if r<n and arr[largest] <arr[r]:
#         largest = r

#     if largest != i:
#         arr[i],arr[largest] = arr[largest],arr[i]
#         heapify(arr, n, largest)

# def heapsort(arr):
#     n = len(arr)

#     for i in range(n//2,-1,-1):
#         heapify(arr,n,i)
    
#     for i in range(n-1,0,-1):
#         arr[i],arr[0] = arr[0],arr[i]

#         heapify(arr,i,0)

# arr = [4,3,12,7,18,15,1]
# heapsort(arr)
# print('sorted array is:')
# for i in range(len(arr)):
#     print("%d" % arr[i],end=' ')
# print("\n")
# print("\t\t\tName:Rohit Gupta")
# print(f"\t\t\tDate:{Date}")
# print(f"\t\t\tTime:{Time}")


#2. WAP to implement Linear and Binary Search and analyze its time complexity

#linear search

# Date = date(2022,8,23)
# Time = time(15,49,27)
# def linear(array, n, x):
#     for i in range(0,n):
#         if array[i] == x:
#             return i
#     return -1


# array = [24, 41, 31, 11, 9, 10 ,5]
# x = 10
# n = len(array)
# result = linear(array, n, x)
# if(result == -1):
#     print("Element not found")
# else:
#     print(f"Element is Present at {result+1} Position ")
# print("\t\t\tName:Rohit Gupta")
# print(f"\t\t\tDate:{Date}")
# print(f"\t\t\tTime:{Time}")



#binary search

# Date = date(2022,8,23)
# Time = time(16,47,53)
# def binary(array, x, low, high):
#     while low<=high:r
#         mid = low + (high-low)//2

#         if array[mid] == x:
#             return mid
        
#         elif array[mid] < x:
#             low = mid +1

#         else:
#             high = mid-1

#     return -1

# array = [2,4,5,7,12,15,19,35]
# x = 2
# n = len(array)
# result = binary(array, x , 0, n-1)
# if(result == -1):
#     print("Element not found")
# else:
#     print(f"Element is Present at {result+1} Position ")
# print("\t\t\tName:Rohit Gupta")
# print(f"\t\t\tDate:{Date}")
# print(f"\t\t\tTime:{Time}")


#3 WAP to implement Strassen’s Matrix Multiplicatio


# import numpy as np

# Date = date(2022,8,30)
# Time = time(15,53,46) 
# def split(matrix):
#     row, col = matrix.shape
#     row2, col2 = row//2, col//2
#     return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]
  
# def strassen(x, y):
  
#     if len(x) == 1:
#         return x * y
  
#     a, b, c, d = split(x)
#     e, f, g, h = split(y)
  
#     p1 = strassen(a, f - h)  
#     p2 = strassen(a + b, h)        
#     p3 = strassen(c + d, e)        
#     p4 = strassen(d, g - e)        
#     p5 = strassen(a + d, e + h)        
#     p6 = strassen(b - d, g + h)  
#     p7 = strassen(a - c, e + f)  

#     c11 = p5 + p4 - p2 + p6  
#     c12 = p1 + p2           
#     c21 = p3 + p4            
#     c22 = p1 + p5 - p3 - p7  
  
#     c = np.vstack((np.hstack((c11, c12)), np.hstack((c21,c22)))) 
  
#     return c

# x = np.array([[2,2,3,1], [1,4,1,2], [2,3,1,1],[1,3,1,2]])
# y = np.array([[2,1,2,1], [3,1,2,1], [3,2,1,1],[1,4,3,2]])
# print(strassen(x,y))
# print("\t\t\tName:Rohit Gupta")
# print(f"\t\t\tDate:{Date}")
# print(f"\t\t\tTime:{Time}")


#4 WAP to implement Matrix Chain Multiplication and analyze its time complexity. 

# import sys

# Date = date(2022,9,27)
# Time = time(16,35,56) 
# def MatrixChain(p,i,j):
#     if i == j:
#         return 0
 
#     _min = sys.maxsize
     
#     for k in range(i, j):
     
#         count = (MatrixChain(p, i, k)
#              + MatrixChain(p, k + 1, j)
#                    + p[i-1] * p[k] * p[j])

#         if count < _min:
#             _min = count

#     return _min
 

# arr = [10, 20, 30, 40, 30]
# n = len(arr)
 
# print("Minimum number of multiplications is ",
#                 MatrixChain(arr, 1, n-1))
# print("\t\t\tName:Rohit Gupta")
# print(f"\t\t\tDate:{Date}")
# print(f"\t\t\tTime:{Time}")

#5 WAP to implement Longest Common Subsequence Problem and analyze its time complexity


'''Date = date(2022,10,11)
Time = time(16,39,9) 
def LCS(x,y):
    m = len(x)
    n = len(y)
    c = [[None]*(n+1) for items in range(m+1)]
    b = [[None]*(n+1) for items in range(m+1)]
    z = ''
    for i in range(m+1):
        c[i][0] = 0
    for j in range(n+1):
        c[0][j] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "↖"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "↑"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "←"
    t = m
    u = n
    for i in range(m,0,-1):
        for j in range(n,0,-1):
            if c[t][u] == 0 or b[t][u] == None:
                return z[::-1]
            elif b[t][u] == "↑":
                t -= 1
            elif b[t][u] == "←":
                u -= 1
            else:
                z += x[t-1]
                t-=1
                u-=1
    

print("Longest common subsequence is: ",end = " ")
print(LCS("10010101","010110110"))
print("\t\t\tName:Rohit Gupta")
print(f"\t\t\tDate:{Date}")
print(f"\t\t\tTime:{Time}")'''


#6 WAP to implement Optimal Binary Search Tree Problem and analyze its time complexity. 

'''
Date = date(2022,10,18)
Time = time(16,29,44) 
def optcost(freq, i, j):
    #i starting point 
    #j ending point
    if j<i:
        return 0
    if j == i:
        return freq[i]
    
    fsum = Sum(freq,i,j)

    Min = 999999999999
    for r in range(i, j+1):
        cost = optcost(freq, i,r-1) + optcost(freq , r+1, j)
        if cost < Min:
            Min = cost

    return Min +fsum

def optimalsearchtree(keys,freq,n):
    sorting_keys(keys,freq,n)
    return optcost(freq,0,n-1)

def Sum(freq, i, j):
    s = 0
    for k in range(i,j+1):
        s += freq[k]
    return s


def sorting_keys(keys,freq,n):
    d = {}
    for i in range(n):
        d[keys[i]] = freq[i]
    dict1 = dict(sorted(d.items()))
    keys = list(dict1.keys())
    freq = list(dict1.values())

keys = [20,10, 12]
freq = [50,34,8]
n = len(keys)
print("Cost of Optimal BST is", optimalsearchtree(keys,freq,n))
print("\t\t\tName:Rohit Gupta")
print(f"\t\t\tDate:{Date}")
print(f"\t\t\tTime:{Time}")'''


#7 WAP to implement 0/1 knapsack using dynamic programming.


'''
Date = date(2022,11,1)
Time = time(16,14,23) 
def knapsack(w,p,n,M):
    
    if M == 0:
        return 0
    
    
    if n == 0:
        return 0

    if w[n-1] > M:
        return knapsack(w,p,n-1,M)

    return max(knapsack(w,p,n-1,M),p[n-1]+knapsack(w,p,n-1,M-w[n-1]))


p = [60,100,120]
w = [10,20,30]
M =50
n = 3
print("Solurion using 0/1 Knapsack is: ",knapsack(w,p,n,M))
print("\t\t\tName:Rohit Gupta")
print(f"\t\t\tDate:{Date}")
print(f"\t\t\tTime:{Time}")'''

#8 WAP to implement Dijkstra’s Algorithm and analyze its time complexity


'''Date = date(2022,9,20)
Time = time(15,59,56) 
Max = 9999999999
class Graph():

    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for c in range(vertices)]
        for r in range(vertices)]

    def printsol(self,dist):
        print("Vertex \tDistance from source")
        for i in range(self.V):
            print(i, "\t",dist[i])

    def mindistance(self, dist, sptset):
        min = Max

        for u in range(self.V):
            if dist[u] < min and sptset[u] == False:
                min = dist[u]
                min_index = u
        return min_index

    def dijkstra(self,src):

        dist = [Max]*self.V
        dist[src] = 0
        sptset = [False]*self.V

        for c in range(self.V):
            x = self.mindistance(dist,sptset)

            sptset[x] = True

            for y in range(self.V):
                if self.graph[x][y] > 0 and sptset[y] == False and \
                    dist[y] > dist[x] +self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        
        self.printsol(dist)

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)
print("\t\t\tName:Rohit Gupta")
print(f"\t\t\tDate:{Date}")
print(f"\t\t\tTime:{Time}")'''

#9 WAP to implement Bellman Ford Algorithm and analyze its time complexity. 


'''Date = date(2022,9,20)
Time = time(16,56,12) 
class Graph():

    def __init__(self,Vertices):
        self.v = Vertices
        self.graph = []

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    
    def printsol(self,dist):
        print("Vertex Distance from Source")
        for i in range(self.v):
            print(i , "\t\t", dist[i])
    
    def BellmanFord(self,src):
        dist = [float("Inf")] * self.v
        dist[src] = 0


        for _ in range(self.v -1):
            for u,v,w in self.graph:
                if dist[u] != float("Inf") and dist[u] +w <dist[v]:
                    dist[v] = dist[u] +w
    
        for u,v,w in self.graph:
            if dist[u] != float("Inf") and dist[u] +w <dist[v]:
                print("Graph contain negative weight cycle")
                return
        
        self.printsol(dist)

g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
 
g.BellmanFord(0)
print("\t\t\tName:Rohit Gupta")
print(f"\t\t\tDate:{Date}")
print(f"\t\t\tTime:{Time}")'''

#10 WAP to implement DFS and BFS and analyze their time complexities. 

'''from collections import deque

Date = date(2022,9,6)
Time = time(16,41,18) 

def BFS(graph,root):

    visited, queue = set() , deque([root])
    visited.add(root)

    while queue:

        vertex = queue.popleft()
        print(str(vertex)+ ' ',end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

graph = {0: [1,2], 1: [2], 2:[3],3: [1,2]}
print("Following is Breadth First Traversal: ",end = ' ')
BFS(graph,0)
print("\n")

def DFS(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start,end=' ')

    for next in graph[start] - visited:
        DFS(graph, next, visited)
    return visited

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

print("Following is Depth First Traversal: ",end = ' ')
DFS(graph, '0')
print("\n")
print("\t\t\tName:Rohit Gupta")
print(f"\t\t\tDate:{Date}")
print(f"\t\t\tTime:{Time}")
'''
#11 WAP to implement Travelling Salesman Problem using backtracking

'''
Date = date(2022,11,8)
Time = time(15,45,51) 
n = 4
answer = []
v = [False for i in range(n)]
v[0] = True

def TSP(graph, v, currpos, n, count, cost):

    if (count == n and graph[currpos][0]):
        answer.append(cost + graph[currpos][0])
        return

    for i in range(n):
        if v[i] == False and graph[currpos][i]:
            v[i] = True
            TSP(graph, v, i, n, count + 1,cost + graph[currpos][i])

            v[i] = False
    return min(answer)

graph= [[ 0, 10, 15, 20 ],
            [ 10, 0, 35, 25 ],
            [ 15, 35, 0, 30 ],
            [ 20, 25, 30, 0 ]]

x = TSP(graph,v, 0, n, 1, 0)
print("The cost of most effective tour : ",end = "")
print(x)
print("\t\t\tName:Rohit Gupta")
print(f"\t\t\tDate:{Date}")
print(f"\t\t\tTime:{Time}")'''


#12 WAP to implement Topological sort algorithm and analyze their time complexities


'''from collections import defaultdict

Date = date(2022,11,8)
Time = time(16,53,27) 
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topologicalsortUTIL(self, v, visited, stack):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalsortUTIL(i,visited,stack)

        stack.append(v)
    
    def topologicalsort(self): 
        visited = [False]*self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topologicalsortUTIL(i, visited, stack)

        print(*stack[::-1])

g = Graph(6)
g.add_edge(5,2)
g.add_edge(5,0)
g.add_edge(4,0)
g.add_edge(4,1)
g.add_edge(2,3)
g.add_edge(3,1)

print("Following is a Topological Sort of given graph")
g.topologicalsort()
print("\t\t\tName:Rohit Gupta")
print(f"\t\t\tDate:{Date}")
print(f"\t\t\tTime:{Time}")'''
















