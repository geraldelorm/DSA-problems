# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
#                        perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"

def urlify(string, length):
    replacement = "%20"
    newString = ""

    for i in range(length):
        if string[i] == " ":
            newString += replacement
        else:
            newString += string[i]

    return newString

    # Time = O(n)
    # Space = O(n)

assert(urlify("Hello World  ", 11) == "Hello%20World")


def urlify2(string, t_length): #say string is passed in as an array
    string = [c for c in string]
    space_count = 0

    for i in range(t_length):
        if string[i] == " ":
            space_count += 1

    end_index = t_length + (space_count * 2)

    for i in range(t_length - 1, 0, -1):
        if string[i] == " ":
            string[end_index - 1] = "0"
            string[end_index - 2] = "2"
            string[end_index - 3] = "%"
            end_index -= 3
        else:
            string[end_index - 1] = string[i]
            end_index -= 1
    
    return "".join(string)


    # Time = O(n)
    # Space = O(1)
    
assert(urlify2("Hello World  ", 11) == "Hello%20World")
