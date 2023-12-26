"""
Modules can be importend using:
        -> import statement
        -> importlib.import_module

When a module is imported:
    -> system cache is checked first sys.modules -> if in cache, just returns cached refference
    otherwise:
    -> module has to be located sommewhere ( by finders) some of the finders in sys.meta_path
    -> module code has to be retrived(loaded)   loaders returned by finder-> ModuleSpec
    -> empty module type object is created
    -> a referece to the module is added to the system cache in sys.modules
    -> module is compiled (optionally)
    -> module is executed -> sets up the module's namespace( module.__dict__ is module.globals())

Module finders:

sys.meta_path -> _frozen_importlib.BuiltinImporter  - finds built-ins, such as math
              -> _frozen_importlib.FrozenImporter   - finds frozen modules
              -> _frozen_importlib.external.PathFinder - file-based modules

PathFinder:
    - Finds file-based modules based on sys.path and package __path__
    sys.path -> ['/home/fmb/my-app', /usr/lib/python3.6 ...]

    collections.__path__ -> ['/usr/lib/python3.6/collections'] - look here to import for example named tuples

Module Properties:
    - built-in import math
    - type(math) -> module
    - math.__spec__ -> ModuleSpec(..)
    - math.__name__ -> math
    - math.__package__ -> ''
    - __file__ is not an attribute of math (built-ins only)

    -standard library import fractions
    -type(fractions) -> module
    -fractions.__spec__ -> ModuleSpec(name,loader,origin)
    -fractions.__name__ -> fractios
    -fractions.__package__ -> ''
    -fractions.__file__ -> /usr/lib/python3.6/fractions.py (found by PathFinder in one of the paths listed in sys.path)

    -custom module import module1
    -type(fractions) -> module
    -fractions.__spec__ -> ModuleSpec(name,loader,origin)
    -fractions.__name__ -> module1
    -fractions.__package__ -> ''
    -fractions.__file__ -> /home/fmb/my-app/fractions.py (found by PathFinder in one of the paths listed in sys.path)

    Python modules may reside:
        - built-ins
        - in files on disk
        - they can be pre-compiled, frozen or zip archives
        - anywhere else that can be accessed by a finder and a loader

    For file based modules(PathFinder):
            - They must exist in a path specified in sys.path
            - or in a path specified by <package>.__path__

Python docs, PEP 302 - to find more info
"""