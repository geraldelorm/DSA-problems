#Brute Force
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    answer[i] = j - i
                    break

        return answer

        # TC: O(n^2)
        # SC: O(n)

#Optimal - Iterating backwards and keeping track of hottestday
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        hottest_day = len(temperatures) - 1

        for curr_day in range(len(temperatures) - 1, -1, -1):
            if temperatures[curr_day] >= temperatures[hottest_day]:
                hottest_day = curr_day
                continue
            
            warmer_day = 1

            while temperatures[curr_day + warmer_day] <= temperatures[curr_day]:
                #user save answer to get stored locations of next warmer_day 
                warmer_day += answer[curr_day + warmer_day]

            answer[curr_day] = warmer_day

        return answer

        # TC: O(n)
        # SC: O(n)
