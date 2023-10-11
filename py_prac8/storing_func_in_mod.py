# storing your functions in modules 
    # one advantage of functions is the way they seperate blocks of code from your main program. 
    # you can store seperate func in different files called modules, and then import them into your main program
    # an import statment tells py to make the code in a module avaliable in the currently running program file
    # helps focus on higher level logic
    # helps allow you to reuse functions in many different programs
    # when you store your functions in differe files, you can share those to othr programmers.


# importing an entire module
    # we need to create a module 
# see files in folder importing file
# import pizza in making_pizza.py copys all functions in pizza.py and imports them into making_pizza.py
# module_name.function_name()


# importing specific functions 
# from module_name import function_name
# from module_name import function_1, function_2, function_3


# using as to give a function an alias
    # if the name of the func youre importing is the same as a function alreaing existing
    # or too long, 
    # you can make an alias
# from pizza import make_pizza as mp
# from module_name import function_name as fn


# using as to give a module an alias 
    # you can also provide an alias for a module name
# import pizza as p
# p.make_pizza(16, 'pepperoni')


# importing all functions in a module 
    # from pizza import *
    # from module_name import *
    
   
# styling functions 
    # functions should have descriptive names 
    
    # def function_name(parameter_0, parameter_1, parameter_2='deafult value')
    
    # def function_name(parameter_0, parameter_1, parameter_2, 
    #                   parameter_3, parameter_4, parameter_5):
    #       function body...


