# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 09:17:02 2020

@author: f33
"""



if 0 :
    import numpy as np
    import matplotlib.pyplot as plt
    #일차방정식 풀기
    
    x = np.arange(-6,6,1)
    
    exec('y=3*x + 12')
    plt.plot(x,y,marker='o')
    plt.plot(x,y*0,color = "blue")
    
    plt.show()

    ###################################################
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    x = np.arange(-6,6,1)
    exec('y=x*x -4')
    plt.plot(x,y,marker='o')
    plt.plot(x,y*0,color = "pink")
    plt.show()
    
    from sympy import Symbol, solve
    x = Symbol('x')
    print('x는',solve('x*x -4'))
    ###################################################
    
    
    from sympy import *
    x = Symbol('x')
    plot( x+1, x**2, xlim=(-2,2), ylim=(-1,3) )
    plot( x*x-1, (x,-2,2))
    plot(x*x*x-8, (x, -3, 3))
    
    
    from sympy import Symbol, solve, plot
    init_printing()
    Rational(1,2)
    x, y, z = symbols('x y z')
    expr = (x**2 + 2*x + 1)/(x**2 + x)
    expr
    Eq( 2*x, 1 )
    
    ###################################################    
    from sympy import *
    init_printing()
    
    ################################################### 
    
    from sympy import Symbol, sympify, simplify, pprint
    
    x = Symbol('x')
    
    #expr1 = input('Input first expression in variable x: ')
    #expr2 = input('Input second expression in variable x: ')
    expr1 = (x**2 + 2*x + 1)/(x**2 + x)
    
    p1 = sympify(expr1)
    #p2 = sympify(expr2)
    
    #result1 = simplify(p1+p2)
    #result2 = simplify(p1-p2)
    #result3 = simplify(p1*p2)
    #result4 = simplify(p1/p2)
    pprint(p1)
    result1 = simplify(p1)
    pprint(result1)
    #pprint(result2)
    #pprint(result3)
    #pprint(result4)    
        
    ################################################### 
    pprint((x**2 + 2*x + 1)/(x**2 + x))
    ################################################### 
    
if 0 :    
    from sympy import Symbol, solve, plot, pprint
    x = Symbol('x')
    plot(x*x*x-8, (x, -3, 3))
    print('x는', solve('x*x*x - 8'))
    pprint(solve('x*x*x - 8'))

#if 0:
#from sympy import *
#x = Symbol('x')
#y = Symbol('y')
#plot(-10*x+45)
#plot(-10*x+45,(x, -1, 5))
#plot(-10*x+45,(x, -1, 1))
#plot_implicit(-y-10*x+45,(x, -1, 5),(y,-5,50))
#    print(list(map(lambda x : -10*x+45, [1,2,3,4])))
#list(map(f, range(1,5)))

if 0:
    from sympy import Symbol, plot, solve
    x = Symbol('x')
    plot(-10*x+45)
    plot(-10*x+45,(x, -1, 6)) # x의 범위를 좁혀보면
    
    def f(x):
        a = -10*x+45
        return a
    print('x가', solve('-10*x+45'),'일때 f(x)는 0')
    x값 = [1,2,3,4]
    print('x가', x값,'일때 f(x)값은', list(map(f, x값)))
    
#simplify( -x -x +4)
#Out[14]: -2*x + 4

if 0:
    from sympy import Symbol, plot, solve
    x = Symbol('x')
    plot(-x+2)
    plot(-x+2,(x, -3, 3)) # x의 범위를 좁혀보면
    
    def f(x):
        a = -x+2
        return a
    print('x가', solve('-x+2'),'일때 f(x)는 0')
    x값 = list(range(-4,3))
    print('x가', x값,'일때 f(x)값은', list(map(f, x값)))
    [print(x,'→',f(x)) for x in x값]


from sympy import Symbol, plot, solve
x = Symbol('x')
plot(3*x + 12)
plot(3*x + 12,(x, -5, 1)) # x의 범위를 좁혀보면


def f(x):
    y = 3*x + 12
    return y
print('x가', solve('3*x + 12'),'일때 f(x)는 0')
x값 = list(range(-5,2))
print('x가', x값,'일때 f(x)값은', list(map(f, x값)))
print('x → f(x)')
[print(x,'→',f(x)) for x in x값]

 
# https://www.reddit.com/r/learnpython/comments/7etgpb/intersection_point_of_2_graphs/
#Saiboo
#2 points
#·
#3 years ago
#If you set your two functions equal, i.e.
#
#f1(x) == f2(x)
#
#you can manipulate it to
#
#f1(x) - f2(x) == 0
#
#You can interpret the left hand side as a new function g(x) , so you get
#
#g(x) := f1(x) - f2(x) == 0
#
#This means you are searching for the roots of g(x).
#
#There is a function in SciPy using Brent's method which does exactly that.
#from sympy import *
#x = symbols('x')
#'''y = 3.5*x + 90와 y = 7*x의 접점'''
#solve(3.5*x + 90 - 7*x, x) #right hand side is 0 and we solve for x

from sympy import symbols
x = symbols('x')
plot(3-6*x,15-3*x,(x, -10, 10))


 