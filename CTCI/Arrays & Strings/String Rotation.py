# String Rotation: Assumeyou have a method isSubstringwhich checks if oneword is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring(e.g., "waterbottle" is a rotation of"erbottlewat").


def isRotated(s1, s2):
    if len(s1) != len(s2) and len(s2) < 0:
        return False
    return isSubString(s1 + s1, s2)

# Time = O(n) isSubString => O(n)
# Space = O(1)


def isSubString(s1, s2):
    l, r = 0, len(s2)

    while r < len(s1):
        if s1[l: r] == s2:
            return True

        l += 1
        r += 1

    return False


assert(isRotated("waterbottle", "erbottlewat") == True)
assert(isRotated("rudhdgethdy", "erbottlewat") == False)
