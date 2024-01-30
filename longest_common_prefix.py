# Find the longest common prefix in a list of Strings.
# Input: 
# 	strs = ["flower","flow","flight"] 
# Output: 
# 	"fl" 

strings = input().split(',')
min_str = strings[0]
for i in strings:
    if len(i) < len(min_str):
        min_str = i

for i in strings:
    j = 0
    while j < len(min_str):
        if i[j] == min_str[j]:
            j += 1
        else:
            min_str = min_str[:j]

print(min_str)
