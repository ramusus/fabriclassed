import inspect
import sys

def add_class_methods_as_module_level_functions_for_fabric(instance, module_name):
    '''
    Utility to take the methods with prefix 'fab_' of the class instance `instance`,
    and add them as functions to a module `module_name`, so that Fabric
    can find and call them. Call this at the bottom of a module after
    the class definition. Returns a list of method for __all__ variable,
    otherwise command 'fab -l' will show extra commands.
    '''
    # get the module as an object
    module_obj = sys.modules[module_name]
    method_names_list = []

    # Iterate over the methods of the class and dynamically create a function
    # for each method that calls the method and add it to the current module
    for method in inspect.getmembers(instance, predicate=inspect.ismethod):
        method_name = method[0]

        if method_name.startswith('fab_'):
            # get the bound method
            func = getattr(instance, method_name)

            method_name = method_name.replace('fab_', '')

            # add the function to the current module
            setattr(module_obj, method_name, func)
            method_names_list += [method_name]

    return method_names_list