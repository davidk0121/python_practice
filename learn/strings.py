# string are similar to arrays
s = "abc"
print(s[0:2]) # output: "ab"

# So this creates a new string
s += "def"
print(s) # output: "abcdef"

# String --> Integer
print(int("123") + int("123")) # output: 246
# Integer --> String
print(str(123) + str(123)) # output: "123123"

# ASCII values
print(ord("a")) # output: 97
print(ord("b")) # output: 98

# Combine a list of strings (with an empty string delimiter)
string = ["ab", "cd", "ef"]
print(" ".join(string)) # output: "abcdef"