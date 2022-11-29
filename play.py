def count(teamA, teamB):
    res = []
    teamA.sort()

    for score in teamB:
        # do binary search on teamA
        l, r = 0, len(teamA)
        while l < r:
            mid = (r + l) // 2
            if teamA[mid] > score:
                r = mid - 1
            else:
                l = mid + 1

        res.append(l)

    return res


print(count([1, 2, 3], [2, 4]))


def moves(arr1, arr2):
    L, moves = len(arr1), 0

    for i in range(L):
        if arr1[i] != arr2[i]:
            l = len(str(arr1[i]))
            for j in range(l):
                diff = abs(int(str(arr1[i])[j]) - int(str(arr2[i])[j]))
                moves += diff

    return moves


print(moves([123, 543], [321, 279]))
