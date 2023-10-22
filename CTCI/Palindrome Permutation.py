# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

# Clearifying questions
# Can I ignore spaces and non alphabets in the string? 

def pal_perm(string):
    strings_map = {}

    for c in string:
        if c.isalpha():
            strings_map[c.lower()] = strings_map.get(c.lower(), 0) + 1

    found_odd = False
    for k in strings_map:
        if strings_map[k] % 2 != 0:
            if found_odd:
                return False
            found_odd = True

    return True

    # Time = O(n)
    # Space = O(n)

assert(pal_perm("Tact Coa") == True)


# we can improve this a little bit by avoiding the second iteration over the hashmap

def pal_perm2(string):
    strings_map = {}

    odd_count = 0
    for c in string:
        if c.isalpha():
            strings_map[c.lower()] = strings_map.get(c.lower(), 0) + 1

            if strings_map[c.lower()] % 2 != 0:
                odd_count += 1
            else:
                odd_count -= 1

    return odd_count <= 1

    # Time = O(n)
    # Space = O(n)


assert(pal_perm2("Tact Coa") == True)
