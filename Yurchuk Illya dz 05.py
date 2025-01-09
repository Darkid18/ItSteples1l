import colorama

import inspect



print("Is module:   ",inspect.ismodule(colorama))
print("Is class:    ",inspect.isclass(colorama))
print("Addres:      ",inspect.getmodule(colorama))
print("Is code:     ",inspect.iscode(colorama))