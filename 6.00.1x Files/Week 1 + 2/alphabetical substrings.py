s = 'azcbobobegghakl'

x=''
y=''
for char in s:
 if(y==''):
  y=char
 elif(y[-1]<=char):
  y+=char
 elif(y[-1]>char):
  if(len(x)<len(y)):
   x=y
   y=char
  else:
   y=char
if(len(y)>len(x)):
 x=y
print(x) 