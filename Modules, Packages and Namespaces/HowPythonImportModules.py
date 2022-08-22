# When we run a statement such as
import fractions
# what is Python doing:
#        - The first thing is that Python is doing the import at run time
#          while the code is actually running
#        - This is different between traditional compiled languages (Ex. C)
#          where the modules are compiled and linked at compile time
#    In both cases though, the system needs to know where those code file exist.
#    Python uses a relatively complex system of how to find and load modules
#   The sys module has a few proprieties that define where Python is going to look for modules
import sys
print(sys.prefix) # where is Python installed (this is a virtual env and all the Python libreries, etc are copied to this directory)
                  # and Python is not running from here it is rooted to this location.
print(sys.exec_prefix) # where are the C binaries located

print(sys.path) # where python looks for imports

# When python wants to import a module Python will search in sys.path
# If it does not find the module in one of those paths the import will fail
# If an import fails you should search in the path ( you can also append to sys.path)

# At a high level, this is how Python imports a module from file:
#    - Checks the sys.modules cache to see if the module was already imported - otherwise:
#    - creates a new module object ( types.ModuleType)
#    - loads the source code from file
#    - add an entry to sys.modules with name as key and the newly created module
#    - compiles and executes the source code
# When a module is imported - the module code gets executed


