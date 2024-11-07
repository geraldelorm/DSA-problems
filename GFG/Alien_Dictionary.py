#User function Template for python3

from typing import List
import collections

class Solution:
    def buildgraph(self, str1, str2):
        L = min(len(str1), len(str2))
        
        for i in range(L):
            if str1[i] != str2[i]:
                self.graph[str1[i]].add(str2[i])
                return
        
    def findOrder(self, dict: List[str], n: int, k: int) -> str:
        self.graph = collections.defaultdict(set)
        
        for i in range(len(dict) - 1):
            self.buildgraph(dict[i], dict[i + 1])
            
        topo_order = []
        visited = set()
        visiting = set()
        
        def dfs(char):
            visited.add(char)
            visiting.add(char)
            
            for next_char in self.graph[char]:
                if next_char in visiting:
                    return False
                
                if next_char not in visited:
                    if not dfs(next_char): return False
            
            visiting.remove(char)
            topo_order.append(char)
            return True
        
        for i in range(k):
            curr_char = chr(ord("a") + i)
            
            if curr_char not in visited:
                if not dfs(curr_char): return ""
                
                
        topo_order.reverse()
        return "".join(topo_order)
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class sort_by_order:

    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word

    def sort_this_list(self, lst):
        lst.sort(key=self.transform)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1])

        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob = Solution()
        order = ob.findOrder(alien_dict, n, k)
        s = ""
        for i in range(k):
            s += chr(97 + i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)

            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)

        print("~")

# } Driver Code Ends