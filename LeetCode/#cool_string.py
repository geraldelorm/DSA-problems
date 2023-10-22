'''
A cool string is defined as a string where all characters have the same frequency. Given a string, can you make it cool with 0 or 1 deletions?

"" -> True
"a" -> True
"aabb" -> True
"aaabb" -> True
"aabbcccddd" -> False
"aaabbbcc" -> False

'''
import collections

def cool_str(str_):
    if not len(str_): return True
    counts = collections.Counter(str_)

    unique_freq_map = {}
    for char, count_of_char  in counts.items():
        unique_freq_map[count_of_char] = unique_freq_map.get(count_of_char, 0) + 1

    if len(unique_freq_map) == 1: return True
    elif len(unique_freq_map) == 2: 
        min_freq, max_freq = min(unique_freq_map.keys()), max(unique_freq_map.keys())

        if max_freq - min_freq == 1 and unique_freq_map[max_freq] == 1:
            return True
        return False
        
    else: return False
    
assert(cool_str("") == True) 
assert(cool_str("a") == True) 
assert(cool_str("aabb") == True)
assert(cool_str("aabbcccddd") == False)
assert(cool_str("aaabbbcc") == False)
assert(cool_str("aaabb") == True) 
assert(cool_str("aaaabb") == False) 

print("ALL PASSED")