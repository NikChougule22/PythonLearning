from Vid46_spec_var_name import *

print ("Name is used as " +  __name__ )

if __name__ =="__main__":
               first()

# if you are using name in a module1 then when you want to print __name__ it will give output as "__main__"
# but if you import the first module, module1 in another module say module2, then when you try to print the __name__
# from module1 in module2 it will give the module name instead of saying "__main__"