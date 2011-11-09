import inspect
import sys

def add_class_methods_as_module_level_functions_for_fabric(instance, module_name):
    '''
    Utility to take the methods of the instance of a class, instance,
    and add them as functions to a module, module_name, so that Fabric
    can find and call them. Call this at the bottom of a module after
    the class definition. Returns a list of method for __all__ variable,
    otherwise command 'fab -l' will show extra commands.
    '''
    # get the module as an object
    module_obj = sys.modules[module_name]

    # Iterate over the methods of the class and dynamically create a function
    # for each method that calls the method and add it to the current module
    for method in inspect.getmembers(instance, predicate=inspect.ismethod):
        method_name, method_obj = method

        if not method_name.startswith('_'):
            # get the bound method
            func = getattr(instance, method_name)

            # add the function to the current module
            setattr(module_obj, method_name, func)

    return [name for name in dir(instance) if name[0] != '_' and callable(getattr(instance, name))]