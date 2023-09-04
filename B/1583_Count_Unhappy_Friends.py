class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:

        def getPreferencedFriendsOverCurrentMatch(friend, pair):
            pref = set()
            for i, v in enumerate(preferences[friend]):
                if v == pair:
                    return pref
                pref.add(v)

        prefered_friends = collections.defaultdict(set)

        for [friend, pair] in pairs:
            prefered_friends[friend] = getPreferencedFriendsOverCurrentMatch(friend, pair)
            prefered_friends[pair] = getPreferencedFriendsOverCurrentMatch(pair, friend)

        print(prefered_friends)
        unhappy = 0
        for friend, preferences in prefered_friends.items():
            for pref in preferences:
                if friend in prefered_friends[pref]: 
                    unhappy += 1
                    break

        return unhappy

        # TC: O(n^2)
        # SC: O(n^2)
        