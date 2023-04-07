# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other. 

# Clearifying Questions:
# is the permutation case sensitive? they cannot be permutations if thier lenghts are not the same right?

def perm(s1, s2):
    if len(s1) != len(s2): return False

    s1 = sorted(s1)
    s2 = sorted(s2)

    return s1 == s2

    # Time = O(NlogN)
    # Space = O(1) - if sorting is done in place

assert(perm("dog", "god") == True)
assert(perm("dog", "God") == False)

# We can reduce time complexity without sorting


def perm2(s1, s2):
    if len(s1) != len(s2):
        return False

    s1_table, s2_table = {}, {}

    for i in range(len(s1)):
        s1_table[s1[i]] = s1_table.get(s1[i], 0) + 1
        s2_table[s2[i]] = s2_table.get(s2[i], 0) + 1

    for key in s1_table:
        if key not in s2_table:
            return False
        if s1_table[key] != s2_table[key]:
            return False

    return True

    # Time = O(n) n + m
    # Space = O(n) n + m

assert(perm2("dog", "god") == True)
assert(perm2("dog", "God") == False)
assert(perm2("qaxszw", "zxsawq") == True)
assert(perm2("qaxsazw", "zxstawq") == False)
assert(perm2("qaxskazw", "zxstaawq") == False)
