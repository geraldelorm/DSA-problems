# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit ( or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

# Clearifying Questions
# input always going to be a string? not null or empty?

def one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    i, j, edits = 0, 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            edits += 1
            if len(s1) > len(s2):
                i += 1
            elif len(s2) > len(s1):
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1

    return edits <= 1


# Time = O(n)
# Space = O(1)
assert(one_away("pale", "ple") == True)
assert(one_away("pales", "pale") == True)
assert(one_away("pale", "bale") == True)
assert(one_away("pale", "bake") == False)
