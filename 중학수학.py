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
    
    
    from sympy import Symbol, solve, plot
    x = Symbol('x')
    plot( x+1, x**2, xlim=(-2,2), ylim=(-1,3) )
    plot( x*x-1, (x,-2,2))
    plot(x*x*x-8, (x, -3, 3))
    
    
    from sympy import *
    init_printing()
    Rational(1,2)
    x, y, z = symbols('x y z')
    expr = (x**2 + 2*x + 1)/(x**2 + x)
    expr
    Eq( 2*x, 1 )
    
    ###################################################    

from sympy import Symbol, solve, plot
x = Symbol('x')
plot(x*x*x-8, (x, -3, 3))
print('x는', solve('x*x*x - 8'))
