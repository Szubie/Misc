from __future__ import print_function
#XOR GATES. Exclusive OR gates. False if the two numbers are the same, else true.

#s="00000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000"
s="1101010"


#It feels like this KINDA works, but it isn't perfect...What could be wrong?


print (s)
#This prints it all on one line.

#However, it adds an extra space after everything, which makes the results much wider. An alternative would be to use sys.stdout.write (after importing sys). Alternatively, could try to import print 


#How to make the traingles have a pointy top of only 1 x?
for y in range(len(s)):         # """Remember, range doesn't use the max value. Therefore, you don't need len(s)-1, otherwise you skip the last value""".
    if s[y]=="0":
        print (" ", end="")   #Remember to use commas if you want to print all on the same line!
    if s[y]=="1":
        print ("x", end="")

print ("")


def calc(s):
    next_line="0"
    next_line2=""
    next_line3="0"
    
    
    #Ok, insert a bit of code to deal with the first input. Then we can safely fix the range problem below.
    
    if s[1]==next_line3:   # len(next_line)-2 ? Rather than -1. We want to compare the value second from the back.
        next_line+="0"
        print (" ", end="")
    else:
        next_line+="1"
        print ("x", end="")      
        
    for num in range(1, len(s)-1): #len(s)-1 seems more accurate then len(s)-2. It completed the bottom section of the bottom-right triforce.  Start counting from range 1, since we have inserted a 0? HOLY SHIT, it broke everything.
        if s[num-1]==s[num+1]:      #So, the above actually compares the first value of the string to the last?    OH, and this line was comparing to "next_line", not s, big mistake.
            next_line+="0"
            print (" ", end="")
        else:
            next_line+="1"
            print ("x", end="")
    if s[len(s)-2]==next_line3:   # len(next_line)-2 ? Rather than -1. We want to compare the value second from the back.
        next_line+="0"
        print (" ", end="")
    else:
        next_line+="1"
        print ("x", end="")
      
    next_line+="0"   #Whoops, .append is for lists. += for strings.

    
    print ("")
    for n in range(1, len(next_line)-1):
        next_line2+=next_line[n]
    return next_line2       #Ooops, now the string gets bigger every time, instead of shrinking every time!
        
        

        
#Ok, sort of works for first run. Need to reproduce this 25 times!

#Well, apparently this is a bit wrong. We only return 5 characters out of a 7 character string every time: instead, we should imagine there is a "0" character on either side of the string at all times. 
#The result of this is that the string SHRINKS every time the function is called.

#The other person creates arrays of True or False and then iterates through, changing the values as required. Additionally, his version of output doesn't print everything on a different line.

#sys.stdout.write('Installing XXX... ') and sys.stdout.write('Done')

next_line=calc(s)



for x in range(25):
#    calc(next_line)           #THIS was why every line was doubled!!! This is why my images were a bit off. They're still strangely large though...
    next_line=calc(next_line)
#    print next_line
    
    
#Ok, let's be honest, this code is a realy mess. Hacked together. 





"""Output from when the strings continued to get bigger! Pretty cool (maybe I should've gotten rid of the printing of the numbers?) What the heck, it looks awesome.

1101010
x x          
x x x x          
x x x x          
01111000000
x x     x x          
x x     x x          
0110011000000
x x x x x x x x          
x x x x x x x x          
011111111000000
x x             x x          
x x             x x          
01100000011000000
x x x x         x x x x          
x x x x         x x x x          
0111100001111000000
x x     x x     x x     x x          
x x     x x     x x     x x          
011001100110011000000
x x x x x x x x x x x x x x x x          
x x x x x x x x x x x x x x x x          
01111111111111111000000
x x                             x x          
x x                             x x          
0110000000000000011000000
x x x x                         x x x x          
x x x x                         x x x x          
011110000000000001111000000
x x     x x                     x x     x x          
x x     x x                     x x     x x          
01100110000000000110011000000
x x x x x x x x                 x x x x x x x x          
x x x x x x x x                 x x x x x x x x          
0111111110000000011111111000000
x x             x x             x x             x x          
x x             x x             x x             x x          
011000000110000001100000011000000
x x x x         x x x x         x x x x         x x x x          
x x x x         x x x x         x x x x         x x x x          
01111000011110000111100001111000000
x x     x x     x x     x x     x x     x x     x x     x x          
x x     x x     x x     x x     x x     x x     x x     x x          
0110011001100110011001100110011000000
x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x          
x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x          
011111111111111111111111111111111000000
x x                                                             x x          
x x                                                             x x          
01100000000000000000000000000000011000000
x x x x                                                         x x x x          
x x x x                                                         x x x x          
0111100000000000000000000000000001111000000
x x     x x                                                     x x     x x          
x x     x x                                                     x x     x x          
011001100000000000000000000000000110011000000
x x x x x x x x                                                 x x x x x x x x          
x x x x x x x x                                                 x x x x x x x x          
01111111100000000000000000000000011111111000000
x x             x x                                             x x             x x          
x x             x x                                             x x             x x          
0110000001100000000000000000000001100000011000000
x x x x         x x x x                                         x x x x         x x x x          
x x x x         x x x x                                         x x x x         x x x x          
011110000111100000000000000000000111100001111000000
x x     x x     x x     x x                                     x x     x x     x x     x x          
x x     x x     x x     x x                                     x x     x x     x x     x x          
01100110011001100000000000000000011001100110011000000
x x x x x x x x x x x x x x x x                                 x x x x x x x x x x x x x x x x          
x x x x x x x x x x x x x x x x                                 x x x x x x x x x x x x x x x x          
0111111111111111100000000000000001111111111111111000000
x x                             x x                             x x                             x x          
x x                             x x                             x x                             x x          
011000000000000001100000000000000110000000000000011000000

"""

""" Another error input. Appears to still be a fractal.

1101010
x x          
x x x        
x x x        
x   x x      
x   x x      
    x x x    
    x x x    
  x x   x x  
  x x   x x  
x x x   x x  
x x x   x x  
x   x   x x  
x   x   x x  
        x x  
        x x  
      x x x  
      x x x  
    x x   x  
    x x   x  
  x x x      
  x x x      
x x   x x    
x x   x x    
x x   x x x  
x x   x x x  
x x   x   x  
x x   x   x  
x x          
x x          
x x x        
x x x        
x   x x      
x   x x      
    x x x    
    x x x    
  x x   x x  
  x x   x x  
x x x   x x  
x x x   x x  
x   x   x x  
x   x   x x  
        x x  
        x x  
      x x x  
      x x x  
    x x   x  
    x x   x  
  x x x      
  x x x      
"""


""" Definitely not perfect, very imprecise. However, it's kinda cool, sort of works (even if very rough). Doesn't work at all for the other problem presented though (why?).

                                                                                                  x                                                                                              
                                                                                                x   x                                                                                              
                                                                                              x       x                                                                                            
                                                                                              x       x                                                                                            
                                                                                            x   x   x   x                                                                                          
                                                                                            x   x   x   x                                                                                          
                                                                                          x               x                                                                                        
                                                                                          x               x                                                                                        
                                                                                        x   x           x   x                                                                                      
                                                                                        x   x           x   x                                                                                      
                                                                                      x       x       x       x                                                                                    
                                                                                      x       x       x       x                                                                                    
                                                                                    x   x   x   x   x   x   x   x                                                                                  
                                                                                    x   x   x   x   x   x   x   x                                                                                  
                                                                                  x                               x                                                                                
                                                                                  x                               x                                                                                
                                                                                x   x                           x   x                                                                              
                                                                                x   x                           x   x                                                                              
                                                                              x       x                       x       x                                                                            
                                                                              x       x                       x       x                                                                            
                                                                            x   x   x   x                   x   x   x   x                                                                          
                                                                            x   x   x   x                   x   x   x   x                                                                          
                                                                          x               x               x               x                                                                        
                                                                          x               x               x               x                                                                        
                                                                        x   x           x   x           x   x           x   x                                                                      
                                                                        x   x           x   x           x   x           x   x                                                                      
                                                                      x       x       x       x       x       x       x       x                                                                    
                                                                      x       x       x       x       x       x       x       x                                                                    
                                                                    x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x                                                                  
                                                                    x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x                                                                  
                                                                  x                                                               x                                                                
                                                                  x                                                               x                                                                
                                                                x   x                                                           x   x                                                              
                                                                x   x                                                           x   x                                                              
                                                              x       x                                                       x       x                                                            
                                                              x       x                                                       x       x                                                            
                                                            x   x   x   x                                                   x   x   x   x                                                          
                                                            x   x   x   x                                                   x   x   x   x                                                          
                                                          x               x                                               x               x                                                        
                                                          x               x                                               x               x                                                        
                                                        x   x           x   x                                           x   x           x   x                                                      
                                                        x   x           x   x                                           x   x           x   x                                                      
                                                      x       x       x       x                                       x       x       x       x                                                    
                                                      x       x       x       x                                       x       x       x       x                                                    
                                                    x   x   x   x   x   x   x   x                                   x   x   x   x   x   x   x   x                                                  
                                                    x   x   x   x   x   x   x   x                                   x   x   x   x   x   x   x   x                                                  
                                                  x                               x                               x                               x                                                
                                                  x                               x                               x                               x                                                
                                                x   x                           x   x                           x   x                           x   x                                              
                                                x   x                           x   x                           x   x                           x   x                                              
                                              x       x                       x       x                       x       x                       x       x                                            
                                              x       x                       x       x                       x       x                       x       x                                            
"""




""" Error: got this:
x x   x   x
x x                          #Error here, should be 3 x's.
x x x                        #Additionally, there are more spaces than required? Why?
x x x        
x   x x      
x   x x      
    x x x    
    x x x    
  x x   x x x
  x x   x x x
  x x   x    
  x x   x    
x x x     x x
x x x     x x
    x x x x x
    x x x x x
x x x        
x x x        
x   x x      
x   x x      
    x x x    
    x x x    
  x x   x x x
  x x   x x x
  x x   x    
  x x   x    
x x x     x x
x x x     x x
    x x x x x
    x x x x x
x x x        
x x x        
x   x x      
x   x x      
    x x x    
    x x x    
  x x   x x x
  x x   x x x
  x x   x    
  x x   x    
x x x     x x
x x x     x x
    x x x x x
    x x x x x
x x x        
x x x        
x   x x      
x   x x      
    x x x    
    x x x    
  x x   x x x
  x x   x x x
"""

"""Expected result:  

xx x x
xx    x
xxx  x
x xxx x
  x x
 x   x
 
 """
 
 
""" This is actually not that bad. But it's bigger in general. Slightly different too. 
x x   x   x  
x x         x
x x x     x  
x x x     x  
x   x x x   x
x   x x x   x
    x   x    
    x   x    
  x       x  
  x       x  
x   x   x   x
x   x   x   x


...lots of white space underneath.
"""

"""  SHORTER GUY! Lines are no longer doubled. However, he's still quite...wide...

x x   x   x  
x x         x
x x x     x  
x   x x x   x
    x   x    
  x       x  
x   x   x   x

"""

"""
                                                                                                  x                                                                                                
                                                                                                x   x                                                                                              
                                                                                              x       x                                                                                            
                                                                                            x   x   x   x                                                                                          
                                                                                          x               x                                                                                        
                                                                                        x   x           x   x                                                                                      
                                                                                      x       x       x       x                                                                                    
                                                                                    x   x   x   x   x   x   x   x                                                                                  
                                                                                  x                               x                                                                                
                                                                                x   x                           x   x                                                                              
                                                                              x       x                       x       x                                                                            
                                                                            x   x   x   x                   x   x   x   x                                                                          
                                                                          x               x               x               x                                                                        
                                                                        x   x           x   x           x   x           x   x                                                                      
                                                                      x       x       x       x       x       x       x       x                                                                    
                                                                    x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x                                                                  
                                                                  x                                                               x                                                                
                                                                x   x                                                           x   x                                                              
                                                              x       x                                                       x       x                                                            
                                                            x   x   x   x                                                   x   x   x   x                                                          
                                                          x               x                                               x               x                                                        
                                                        x   x           x   x                                           x   x           x   x                                                      
                                                      x       x       x       x                                       x       x       x       x                                                    
                                                    x   x   x   x   x   x   x   x                                   x   x   x   x   x   x   x   x                                                  
                                                  x                               x                               x                               x                                                
                                                x   x                           x   x                           x   x                           x   x                            
"""

"""
                                                 x                                                
                                                x x                                               
                                               x   x                                              
                                              x x x x                                             
                                             x       x                                            
                                            x x     x x                                           
                                           x   x   x   x                                          
                                          x x x x x x x x                                         
                                         x               x                                        
                                        x x             x x                                       
                                       x   x           x   x                                      
                                      x x x x         x x x x                                     
                                     x       x       x       x                                    
                                    x x     x x     x x     x x                                   
                                   x   x   x   x   x   x   x   x                                  
                                  x x x x x x x x x x x x x x x x                                 
                                 x                               x                                
                                x x                             x x                               
                               x   x                           x   x                              
                              x x x x                         x x x x                             
                             x       x                       x       x                            
                            x x     x x                     x x     x x                           
                           x   x   x   x                   x   x   x   x                          
                          x x x x x x x x                 x x x x x x x x                         
                         x               x               x               x                        
                        x x             x x             x x             x x                       
                       x   x           x   x           x   x           x   x                      
                      x x x x         x x x x         x x x x         x x x x                     
                     x       x       x       x       x       x       x       x                    
                    x x     x x     x x     x x     x x     x x     x x     x x                   
                   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x                  
                  x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x                 
                 x                                                               x                
                x x                                                             x x               
               x   x                                                           x   x              
              x x x x                                                         x x x x             
             x       x                                                       x       x            
            x x     x x                                                     x x     x x           
           x   x   x   x                                                   x   x   x   x          
          x x x x x x x x                                                 x x x x x x x x         
         x               x                                               x               x        
        x x             x x                                             x x             x x       
       x   x           x   x                                           x   x           x   x      
      x x x x         x x x x                                         x x x x         x x x x     
     x       x       x       x                                       x       x       x       x    
    x x     x x     x x     x x                                     x x     x x     x x     x x   
   x   x   x   x   x   x   x   x                                   x   x   x   x   x   x   x   x  
  x x x x x x x x x x x x x x x x                                 x x x x x x x x x x x x x x x x 
 x                               x                               x                               x
x x                             x x                             x x                             x 
   x                           x   x                           x   x                           x x
  x x                         x x x x                         x x x x                         x   
 x   x                       x       x                       x       x                       x x  
x x x x                     x x     x x                     x x     x x                     x   x 
       x                   x   x   x   x                   x   x   x   x                   x x x x
      x x                 x x x x x x x x                 x x x x x x x x                 x       
     x   x               x               x               x               x               x x      
    x x x x             x x             x x             x x             x x             x   x     
   x       x           x   x           x   x           x   x           x   x           x x x x    
  x x     x x         x x x x         x x x x         x x x x         x x x x         x       x   
 x   x   x   x       x       x       x       x       x       x       x       x       x x     x x  
x x x x x x x x     x x     x x     x x     x x     x x     x x     x x     x x     x   x   x   x 
               x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x x x x x x x x
              x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x               
             x                                                                     x              
            x x                                                                   x x             
           x   x                                                                 x   x            
          x x x x                                                               x x x x           
         x       x                                                             x       x          
        x x     x x                                                           x x     x x         
       x   x   x   x                                                         x   x   x   x        
      x x x x x x x x                                                       x x x x x x x x       
     x               x                                                     x               x      
    x x             x x                                                   x x             x x     
   x   x           x   x                                                 x   x           x   x    
  x x x x         x x x x                                               x x x x         x x x x   
 x       x       x       x                                             x       x       x       x  
x x     x x     x x     x x                                           x x     x x     x x     x x 
   x   x   x   x   x   x   x                                         x   x   x   x   x   x   x   x
  x x x x x x x x x x x x x x                                       x x x x x x x x x x x x x x x 
 x                           x                                     x                             x
x x                         x x                                   x x                           x 
   x                       x   x                                 x   x                         x x
  x x                     x x x x                               x x x x                       x   
 x   x                   x       x                             x       x                     x x  
x x x x                 x x     x x                           x x     x x                   x   x 
       x               x   x   x   x                         x   x   x   x                 x x x x
      x x             x x x x x x x x                       x x x x x x x x               x       
     x   x           x               x                     x               x             x x      
    x x x x         x x             x x                   x x             x x           x   x     
   x       x       x   x           x   x                 x   x           x   x         x x x x    
  x x     x x     x x x x         x x x x               x x x x         x x x x       x       x   
 x   x   x   x   x       x       x       x             x       x       x       x     x x     x x  
x x x x x x x x x x     x x     x x     x x           x x     x x     x x     x x   x   x   x   x 
                   x   x   x   x   x   x   x         x   x   x   x   x   x   x   x x x x x x x x x
                  x x x x x x x x x x x x x x       x x x x x x x x x x x x x x x                 
                 x                           x     x                             x                
                x x                         x x   x x                           x x               
               x   x                       x   x x   x                         x   x              
              x x x x                     x x x   x x x                       x x x x             
             x       x                   x     x x     x                     x       x            
            x x     x x                 x x   x   x   x x                   x x     x x           
"""