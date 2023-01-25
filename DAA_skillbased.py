# Implement the Knapsack problem and 0/1 Knapsack problem

# Knapsack problem using greedy approach

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractionalKnapsack(W, arr):

    arr.sort(key=lambda x: (x.value/x.weight), reverse=True)   

    finalvalue = 0.0

    for item in arr:
 

        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value
 
        else:
            finalvalue += item.value * W / item.weight
            break
     
    # Returning final value
    return finalvalue


# 0/1 knapsack  (dynamic programming)
def Knapsackdynamic(W,weight,Value,n):
    mat = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                mat[i][w] = 0
            elif weight[i-1] <= W:
                mat[i][w] = max(Value[i-1]+mat[i-1][w-weight[i-1]],mat[i-1][w])
            else:
                mat[i][w] = mat[i-1][w]
    return mat[n][W]

val = [10,5,15, 7, 6, 18, 3]
wt = [2, 3, 5, 7, 1, 4, 1]
arr = [Item(10,2), Item(5,3), Item(15,5),Item(7,7),Item(6,1),Item(18,4),Item(3,1)]
W = 15
n = len(val)
print("\nRohit Gupta (0901AM211045)\n\n")
print("Maximum Total Value is By Knapsack with greedy approach is: ")
print(fractionalKnapsack(W,arr))
print("Maximum Total Value is By 0/1Knapsack is: ")
print(Knapsackdynamic(W, wt, val, n))


# Max = 9999999999
# class Graph():

#     def __init__(self,vertices):
#         self.V = vertices
#         self.graph = [[0 for c in range(vertices)]
#         for r in range(vertices)]

#     def printsol(self,dist):
#         print("Vertex \tDistance from source")
#         for i in range(self.V):
#             print(i, "\t",dist[i])

#     def mindistance(self, dist, sptset):
#         min = Max

#         for u in range(self.V):
#             if dist[u] < min and sptset[u] == False:
#                 min = dist[u]
#                 min_index = u
#         return min_index

#     def dijkstra(self,src):

#         dist = [Max]*self.V
#         dist[src] = 0
#         sptset = [False]*self.V

#         for c in range(self.V):
#             x = self.mindistance(dist,sptset)

#             sptset[x] = True

#             for y in range(self.V):
#                 if self.graph[x][y] > 0 and sptset[y] == False and \
#                     dist[y] > dist[x] +self.graph[x][y]:
#                     dist[y] = dist[x] + self.graph[x][y]
        
#         self.printsol(dist)

# g = Graph(9)
# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#            [4, 0, 8, 0, 0, 0, 0, 11, 0],
#            [0, 8, 0, 7, 0, 4, 0, 0, 2],
#            [0, 0, 7, 0, 9, 14, 0, 0, 0],
#            [0, 0, 0, 9, 0, 10, 0, 0, 0],
#            [0, 0, 4, 14, 10, 0, 2, 0, 0],
#            [0, 0, 0, 0, 0, 2, 0, 1, 6],
#            [8, 11, 0, 0, 0, 0, 1, 0, 7],
#            [0, 0, 2, 0, 0, 0, 6, 7, 0]
#            ]

# print("\nRohit Gupta (0901AM211045)\n\n")
# g.dijkstra(0)

