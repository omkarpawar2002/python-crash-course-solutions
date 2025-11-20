'''
 8-16. Imports: Using a program you wrote that has one function in it, store that 
function in a separate file . Import the function into your main program file, and 
call the function using each of these approaches:

 import module_name
 from module_name import function_name
 from module_name import function_name as fn
 import module_name as mn
 from module_name import *
 '''


# ----------------

'''
import printing_functions
printing_functions.print_models(['samsung','apple'])
'''


'''
from printing_functions import print_models
print_models(['samsung','nord','vivo15'])
'''


'''
from printing_functions import print_models as p_m
p_m(['samsung','nord','vivo15'])
'''



'''
import printing_functions as p_f
p_f.print_models(['samsung','apple'])
'''



'''
from printing_functions import *
print_models(['apple','motorola'])
'''