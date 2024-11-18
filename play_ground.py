#script to rename files in /leeetcode directory
#these directory contains other folders e.g "8. Add Two"
#these folders contain files named solution.py
#Rename solution.py to the parent folder name e.g 8_Add_Two.py


import os

def main():
   
    folder = "Leetcode"
    for filename in os.listdir(folder):
        path = folder + "/" + filename
        if os.path.isdir(path):  
            print("\nIt is a directory")  
            
            newName = "Leetcode" + "/" + filename.replace(".", "").replace(" ", "_") + ".py"
            print(filename, newName)
            rename_and_move_file(path, newName)
 
def rename_and_move_file(path, newPath):
    file = os.listdir(path)[0]
    src = f"{path}/{file}"
    dst = newPath

    print(src, dst)
    os.rename(src, dst)
    os.rmdir(path)

# Driver Code
if __name__ == '__main__':
     
    main()





num_terms = 10
fibonacci = [0, 1]

while len(fibonacci) < num_terms:
  next_term = fibonacci[-1] + fibonacci[-2]
  fibonacci.append(next_term)

print(fibonacci)

pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
pairs.sort(key= lambda pair : pair[1], reverse=True)
        
nums.sort(key=cmp_to_key(self.comparator))
    def comparator(self, num1, num2):
        if num1 + num2 > num2 + num1:
            return -1
        elif num1 + num2 < num2 + num1:
            return 1
        else:
            return 0
            
 from bisect import bisect_left          
idx_to_insert = bisect_left(longest_sub, curr_num)


#Backtracking 
def backtrack(i, currStr):
    if len(currStr) == len(digits):
        res.append(currStr)
        return

    for c in char_map[digits[i]]:
        backtrack(i + 1, currStr + c)

    if digits:
        backtrack(0, "")


# Distinct Component - island



# Topo sort DFS - detect cycles
import collections
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        for course, prepreq in prerequisites:
            graph[course].append(prepreq)

        visited = set()
        visiting = set() #to detect cycle as we can recieve a cyclic graph
        ordering = []

        def dfs(curr_course):
            visited.add(curr_course)
            visiting.add(curr_course)

            for pre_req in graph[curr_course]:
                if pre_req in visiting:
                    return False
                if pre_req not in visited:
                    if not dfs(pre_req): return False

            visiting.remove(curr_course)
            ordering.append(curr_course)
            return True

        for course in range(numCourses):
            if course not in visited:
                if not dfs(course): return []

        return ordering


# Kahn's Algo topo sort - BFS
# Function to detect cycle in a directed graph.
import collections 
from typing import List

def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
    indegree = collections.defaultdict(set)
    
    for node, edges in enumerate(adj):
        for edge in edges:
            indegree[edge].add(node)
            
    queue = collections.deque()
    
    for node in range(V):
        if not indegree[node]:
            queue.append(node)
            
    topo_order = []
    
    while queue:
        curr_node = queue.popleft()
        topo_order.append(curr_node)
        
        for edge in adj[curr_node]:
            indegree[edge].remove(curr_node)
            
            if not indegree[edge]:
                queue.append(edge)
                
    if len(topo_order) == V:
        return 0
    else:
        return 1
        
        
        
        
# Shortest distace from source to all nodes - Weighted DAG
# We can use topo sort + relaxed weight to calc distence - cos there are no
# cyles

# Dijkstra is needed if cycles are posible - cos there is no topo sort of cyclic
# graphs
class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
                         
        #create graph
        graph = collections.defaultdict(list)

        for fro, to, dist in edges:
            graph[fro].append([to, dist])

        #create topo ordering
        visited = set() #just this cos there are no cycles
        topo_order_stack = []
        
        def dfs(curr_v): #simple cos there are not cycles to check for
            visited.add(curr_v)
            
            for next_v, dist in graph[curr_v]:
                if next_v not in visited:
                    dfs(next_v)
                
            topo_order_stack.append(curr_v)

        for v in range(V):
            if v not in visited:
                dfs(v)
                
        # Pop from topo stacck and relax edges - distance update
        distance = [float("inf")] * V
        distance[0] = 0 #mark distance to source

        while topo_order_stack:
            curr_v = topo_order_stack.pop()
            curr_dist = distance[curr_v]
            
            for next_v, next_dist in graph[curr_v]:
                if curr_dist + next_dist < distance[next_v]:
                    distance[next_v] = curr_dist + next_dist

        for i, d in enumerate(distance):
            if d == float("inf"):
                distance[i] = -1
                
        return distance


# Shortest distance in Undirected graph with unit weight

class Solution:
    def shortestPath(self, edges, n, m, src):
        graph = collections.defaultdict(set)
        
        for fro, to in edges:
            graph[fro].add(to)
            graph[to].add(fro)
            
            
        queue = collections.deque()
        queue.append([src, 0])
        distance = [float("inf")] * n
        visited = set()
        visited.add(src)
        
        while queue:
            curr_v, dist = queue.popleft()
            distance[curr_v] = dist
            
            for next_v in graph[curr_v]:
                if next_v not in visited:
                    visited.add(next_v)
                    queue.append([next_v, dist + 1])
                    
        for i, d in enumerate(distance):
            if d == float("inf"):
                distance[i] = -1
                
        return distance
        
        
        
# Word ladder
class Solution:
    def findSequences(self, beginWord, endWord, wordList):
        word_list = set(wordList)
        queue = collections.deque()
        queue.append([[beginWord], 1])
        visited = set([beginWord])

        answer = []
        target_dist = float("inf")

        while queue:
            curr_word_path, dist = queue.popleft()
            curr_word = curr_word_path[-1]

            if dist > target_dist:
                break

            visited.add(curr_word)

            if curr_word == endWord:
                answer.append(curr_word_path)
                target_dist = dist

            for i in range(len(curr_word)):
                curr_word_list = list(curr_word)
                for new_c in "abcdefghijklmnopqrstuvwxyz":
                    curr_word_list[i] = new_c
                    new_word = "".join(curr_word_list)

                    if new_word in word_list and new_word not in visited:
                        queue.append([curr_word_path + [new_word], dist + 1])

        return answer
        
        
        
        
    #Dijkstra's Algo - With Priority Queue - O(ElogV)
    #Undirectlted weighted graph
    
    class Solution:
        def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
            graph = collections.defaultdict(list)
            
            for node in range(len(adj)):
                for next_node, cost in adj[node]:
                    graph[node].append([next_node, cost])
            
            distance = [float("inf")] * len(adj)
            distance[src] = 0
            
            p_queue = []
            
            heapq.heappush(p_queue, [0, src])
            
            while p_queue:
                curr_dist, curr_node = heapq.heappop(p_queue)
                
                for next_node, next_dist in graph[curr_node]:
                    if curr_dist + next_dist < distance[next_node]:
                        distance[next_node] = curr_dist + next_dist
                        heapq.heappush(p_queue, [curr_dist + next_dist, next_node])
                        
            return distance
            
    
    #Dijkstra's Path - Track parents etc
    class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        graph = collections.defaultdict(list)

        for node, next_node, cost in edges:
            graph[node].append([next_node, cost])
            graph[next_node].append([node, cost])

        distance = [float("inf")] * (n + 1)
        parent = [-1] * (n + 1)

        p_queue = []
        heapq.heappush(p_queue, (0, 1, -1))

        while p_queue:
            curr_dist, curr_node, parent_node = heapq.heappop(p_queue)

            if curr_dist > distance[curr_node]:
                continue

            distance[curr_node] = curr_dist
            parent[curr_node] = parent_node

            for next_node, next_dist in graph[curr_node]:
                if curr_dist + next_dist < distance[next_node]:
                    distance[next_node] = curr_dist + next_dist
                    heapq.heappush(p_queue, (curr_dist + next_dist, next_node, curr_node))

        if distance[n] == float("inf"): return [-1]

        path = []
        node = n

        while node != -1:
            path.append(node)
            node = parent[node]

        path.append(distance[n])
        path.reverse()
        return path
    
    
    
    
# Dijkstra Path Effort:
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        start = [0, 0, 0]
        end = [ROWS - 1, COLS - 1]

        p_queue = []
        heappush(p_queue, start)

        efforts = [[float("inf") for _ in range(COLS)] for _ in range(ROWS)]
        efforts[0][0] = 0

        while p_queue:
            curr_min_effort, curr_row, curr_col = heappop(p_queue)

            if [curr_row, curr_col] == end:
                return curr_min_effort

            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

            for row_offset, col_offset in directions:
                new_row, new_col = curr_row + row_offset, curr_col + col_offset

                if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                    exsiting_effort = efforts[new_row][new_col]
                    next_effort = abs(heights[curr_row][curr_col] - heights[new_row][new_col])
                    path_effort = max(curr_min_effort, next_effort)

                    if exsiting_effort > path_effort:
                        efforts[new_row][new_col] = path_effort
                        heappush(p_queue, [path_effort, new_row, new_col])

        return -1
    
    
    
# Bellaman ford ALgo - O(V * E)
# Relax edges + check neg cycle- shortest ppath with neg weight
    def bellman_ford(self, src):

        # Step 1: fill the distance array and predecessor array
        dist = [float("Inf")] * self.V
        # Mark the source vertex
        dist[src] = 0

        # Step 2: relax edges |V| - 1 times
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        # No negative weight cycle found!
        # Print the distance and predecessor array
        self.print_solution(dist)
    
    
# Floyd Warshall - Algo Milti-source shortest path
# Algorithm implementation - Used Dynamic programming to compute
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    print_solution(distance)
    
    
# Minimum Spanning Tree
# A tree with N nodes and N - 1 edges where all nodes are reacchable from each
# The MST is the tree with the mininum sum of edge weights

# Prim's Algorithm - To get the sum or also the edges that form the MST
# Priority Queue + visted set
def prims_mst(adj: List[List[int]]):
    visited = set()
    mst = []
    mst_sum = 0
    p_queue = []
    
    heapq.heappush(p_queue, [0, 0, -1]) #weight node parent
    
    while p_queue:
        wei, node, parent = heapq.heappop(p_queue)
        
        if node in visited:
            continue
        
        visited.add(node)
        mst_sum += wei
        mst.append((parent, node))
        
        for nei, nei_wei in adj[node]:
            if nei not in visited:
                heapq.heappush([nei_wei, nei, node])
                
    return mst_sum
        
        
# Disjoint set -- ********* MST Kruskal's Algo
# Finding parent and union
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            #path compression 
            self.parent[cur] = self.parent[self.parent[cur]] 
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        #find grand parents 
        pu = self.find(u)
        pv = self.find(v)
        
        #already connected 
        if pu == pv:
            return False
            
        #get highest rank
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
            
        # set parent of smaller ranked node
        self.parent[pv] = pu
        
        #update rank for higher rank node
        self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res
        
        
        
#Kruskals algorithms - MST using disjointset
#Sort all edges with weight
#Create a DSU if the graph
#For every edges if the nodes no not belong to the same union add the to the MST
def spanningTree(self, V: int, adj: List[List[int]]) -> int:
    dsu = DSU(len(adj))
    mst = []
    mst_sum = 0
    
    adj_list = []
    
    for node, info in enumerate(adj):
        for nei, weight in info:
            adj_list.append([weight, node, nei])
        
    adj_list.sort(key = lambda x:x[0])
    
    for weight, fro, to in adj_list:
        if dsu.union(fro, to):
            mst.append([fro, to])
            mst_sum += weight
            
    return mst_sum