#User function Template for python3
import collections

class Solution:
    def findSequences(self, beginWord, endWord, wordList):
        word_list = set(wordList)
        queue = collections.deque()
        queue.append([[beginWord], 1])
        visited = set([beginWord])

        answer = collections.defaultdict(list)

        while queue:
            curr_word_path, dist = queue.popleft()
            curr_word = curr_word_path[-1]

            visited.add(curr_word)

            if curr_word == endWord:
                answer[dist].append(curr_word_path)

            for i in range(len(curr_word)):
                curr_word_list = list(curr_word)
                for new_c in "abcdefghijklmnopqrstuvwxyz":
                    curr_word_list[i] = new_c
                    new_word = "".join(curr_word_list)

                    if new_word in word_list and new_word not in visited:
                        queue.append([curr_word_path + [new_word], dist + 1])

        if not answer:
            return []

        return answer[min(answer.keys())]