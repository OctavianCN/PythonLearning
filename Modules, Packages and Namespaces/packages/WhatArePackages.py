"""
Packages are modules ( but modules are not necessarly packages)

They contain:
    - modules
    - packages (called sub_packages)

If a module is a package, it must have a value set for __path__

Packages and File Systems
    Modules do not have to be entities in a file system
    By the same token, packages do not have to be entities in thhe file system
    Typically they are - just as typically modules are file system entities

Packages represents a hierarchy of modules / packages:
    pack1.mod1
    pack1.pack1_1.mod1_1

Importing nested Packages

If you have a statement in your top-level program such as:
import pack1.pack1_1.module1

The import system will perform these steps:
    - imports pack1
    - imports pack1.pack1_1
    - imports pack1.pack1_1.module1
The sys.modules cache will contain entries for:
                - pack1
                - pack1.pack1_1
                - pack1.pack1_1.module1
The namespace where the import was run contains: pack1

Although modules and packages can be far more generic than file system based entities, it gets complicated! ( for more info PEP302)

File Based Packages:
    - package paths are created by using file system directories and files
    - the directory name becomes package name
    - since the package is a module the code for the package is in __init__.py

import pack1

the code for pack1 is in __init__.py, that code is loaded, executed and cached in sys.modules
the symbol pack1 is added to our namespace referencing the same object ( just like a module)
__path__ property -> file system directory path (absolute)
__file__ property -> file system path to __init__.py (absolute)


For modules inside the package:
__file__ property - location of the module code in file system
__package__ - is the package the module code is located in (empty string if the module is located in the application root)
If the module is also a package:
__path__ - the location of the package in file system

To import for example module1 from a package use

import pack1.module1

If __init__.py - contains imports in the code the modules will be also imported when the package will be imported
"""