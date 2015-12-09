>>> a = 10
>>> def f(x):
      return x + a
>>> a = 3
>>> f(1)
 

int - correct

4 - correct
#Enviroments. Without a defined value inside the function, it just takes the global set value.


>>> x = 12
>>> def g(x):
      x = x + 1
      def h(y):
          return x + y
      return h(6)
>>> g(x)
 
#functions can go inside functions!



def foo(x):
   def bar(x):
      return x + 1
   return bar(x * 2)

foo(3)
 

7 - correct
#7 is correct, NOT 8. the final line keeps x as 3, as defined in its own function.


def foo (x):
   def bar (z):
      return z + x
   return bar(3)

foo(2)
 

5 - correct

