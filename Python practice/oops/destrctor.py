#in python destructor is not as much as in c++ because python has its own garbage collector
class Employee:

    def __init__(self):
       print("employee is here")


    def __del__(self):
        print("destructor called.")
def Created_obj():
   print("making object..")
   obj = Employee()
   print("function end..")

   return obj

print("calling created_obj() function..")
obj = Created_obj()
print("program end")