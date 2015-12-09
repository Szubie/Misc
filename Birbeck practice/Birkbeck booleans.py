x=5
y=20
s="Birkbeck"

s2=""

x==5 and y==10
#False, "and" requires both to be True.

x<0 or y>15
#True, "or" requires only one has to be True (y is True)

y%x==0 and len(s)==8
#s.length()==8 (groovy syntax)

#True, both are True.

for n in range(1,3):
    s2+=s[n]
    #s.substring(1,3) == "Bir"
s2=="Bir" or x/y>0
#False, both are False actually.


#Groovy seems to use "true" and "false", rather than the capitalised versions in Python "True" and "False". (Also, it seems to be similar to C in some ways: curly braces { } and declaring the type of a variable (int i = 0) (string s = "s"))