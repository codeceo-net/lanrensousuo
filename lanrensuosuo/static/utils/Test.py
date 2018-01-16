#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from functools import wraps

#
# def dec2( func ):
#
#     def inner( *args, **kwargs ):
#         print( "dec2" )
#         print(args)
#         print(kwargs)
#         return func( *args, **kwargs  )
#     return inner
# def dec1( func ):
#
#     def inner( *args, **kwargs ):
#         print( "dec1" )
#         print(args)
#         print( kwargs )
#         return func( *args, **kwargs  )
#     return inner
#
# @dec2
# @dec1
# def func(arg1, arg2):
#     print("11111111111111111111111111111111")
#     pass


#func = dec2(dec1(func))
#func(1,2)

def checkLogin(func):
    @wraps(func)
    def wrappers(*args, **kwargs):
        """Docs"""
        if True:
            print("111111111111")
            return func(*args, **kwargs)
        else:
            return print("00000000")
    return wrappers
@checkLogin
def fun(arg1, arg2):
    print("==========================")
    """Docstring"""
    pass
fun(1,2)

print(fun.__name__, fun.__doc__)

a = True if 10<20 else False

print( a )

def a (a,v,**args):
    print(a)
    print(v)
    print( args )
a(1,1,x=2,y=3)

# def decomaker( func ):
#     def inner( *args, **kwargs ):
#         print( "decomaker" )
#         print(args)
#         print(kwargs)
#         return func( *args, **kwargs  )
#     return inner
#
# @decomaker("/nihao")
# def func(arg1, arg2):
#     pass
#
# func(1,2)