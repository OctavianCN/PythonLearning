import os.path
import types
import sys

module_name = 'module1'
module_file = 'module1_source.py'
module_path = '.'

module_rel_file_path = os.path.join(module_path, module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)

# read source code from file
with open(module_rel_file_path, 'r') as code_file:
    source_code = code_file.read()

# create a module object
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path

# set a ref in sys modules
sys.modules[module_name] = mod

# compile source code
code = compile(source_code, filename=module_abs_file_path, mode='exec')

#execute compiled source code
exec(code, mod.__dict__) # where globals goes in mod.__dict__


mod.hello()

# if everything above is commented it will not work because module1_source is not module1
# but with everything above module1 is added to the cache and it is loaded
import module1

module1.hello()