#creating list on demand and sorting
class Leaderboard:
    def __init__(self): #space O(n)
        self.leaderboard = {}    

    def addScore(self, playerId: int, score: int) -> None: #O(1)
        self.leaderboard[playerId] = self.leaderboard.get(playerId, 0) + score
        
    def top(self, K: int) -> int: #O(nlogn)
        scores = list(self.leaderboard.values())
        scores.sort(reverse = True)
        return sum(scores[:K])
        
    def reset(self, playerId: int) -> None: #O(1)
        del self.leaderboard[playerId]
        
#creating a heap on demand to avoid sorting
class Leaderboard:
    def __init__(self): #space O(n)
        self.leaderboard = {}    

    def addScore(self, playerId: int, score: int) -> None: #O(1)
        self.leaderboard[playerId] = self.leaderboard.get(playerId, 0) + score
        
    def top(self, K: int) -> int: #O(nlogk). space O(k)
        import heapq
        heap = []

        for v in self.leaderboard.values():
            heapq.heappush(heap, v)

            if len(heap) > K:
                heapq.heappop(heap)

        return sum(heap)
        
    def reset(self, playerId: int) -> None: #O(1)
        del self.leaderboard[playerId]


#using a sorted dictionary (TreeMap) ~ BST
import collections
from sortedcontainers import SortedDict
class Leaderboard:

    def __init__(self): #space O(n)
        self.leaderboard = defaultdict()
        self.sortedLeaderboard = SortedDict()

    def addScore(self, playerId: int, score: int) -> None: #O(logN)
        if playerId not in self.leaderboard:
            self.leaderboard[playerId] = score
            #updaying with negative value to get it sorted in inorder treversal
            self.sortedLeaderboard[-score] = self.sortedLeaderboard.get(-score, 0) + 1 #BTS Search
        else:
            prevScore = self.leaderboard[playerId]
            self.leaderboard[playerId] += score

            num_of_players_with_prevScore = self.sortedLeaderboard.get(-prevScore) #BTS Search

            if num_of_players_with_prevScore == 1:
                del self.sortedLeaderboard[-prevScore]
            else:
                self.sortedLeaderboard[-prevScore] -= 1

            newScore = prevScore + score;
            self.sortedLeaderboard[-newScore] = self.sortedLeaderboard.get(-newScore, 0) + 1
        
    def top(self, K: int) -> int: #O(k)
        count, total = 0, 0

        for key, val in self.sortedLeaderboard.items():
            for _ in range(val):
                total += -key
                count += 1;

                if count == K:
                    break

            if count == K:
                    break

        return total
        
    def reset(self, playerId: int) -> None: #O(logN)
        prevScore = self.leaderboard[playerId]
        num_of_players_with_prevScore = self.sortedLeaderboard.get(-prevScore) #BST search

        if num_of_players_with_prevScore == 1:
            del self.sortedLeaderboard[-prevScore]
        else:
            self.sortedLeaderboard[-prevScore] -= 1

        del self.leaderboard[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)