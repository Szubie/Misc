bobs=0

for x in range(len(s)):
    if s[x:x+3] == "bob":
        bobs +=1
        
print bobs