
with open('token') as f:
    lines = f.readlines()
print ("i'am here")
print(lines)
# Iterate over the string
i = 0
newstr = ""
for element in lines[0]:
    asc=(ord(element) - i)
    if (asc > 0):
        newstr = newstr + chr(asc)
   
    i = i+1
print(newstr + "\n")