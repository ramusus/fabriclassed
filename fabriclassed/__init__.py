from utils import add_class_methods_as_module_level_functions_for_fabric as initialize

VERSION = (0, 4, 1)
__version__ = '.'.join(map(str, VERSION))
__all__ = ['initialize']