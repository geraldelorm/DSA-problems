# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# Clearifying Questions:
# Are the characters ASCII (128), extended ASCII (256) or Unicode (149,186 in v15.0)?

def isUnique(s):
    if len(s) > 128: return False #assuming is ASCII you cannot have all uqiue cahraters more that 128

    seen = set() #will only ever hold 128 character in the case of ASCII
    for char in s:
        if char in seen:
            return False
        seen.add(char)

    return True

# Time = O(n)
# Space = O(1) max_size  = 128

assert(isUnique("boy") == True)
assert(isUnique("uhstgdbjansutegsghabdsd") == False)

# To not use any more space - I would just sort the string/array in place 


def isUnique2(s):
    if len(s) < 2: return True
    if len(s) > 128: return False  # assuming is ASCII you cannot have all uqiue cahraters more that 128

    s = sorted(s)
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return False

    return True
# Time = o(nlogn) - for the sorting
# Space = O(1) - if sorting is done in-place

assert(isUnique2("boy") == True)
assert(isUnique2("uhstgdbjansutegsghabdsd") == False)
