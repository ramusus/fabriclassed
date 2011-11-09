from fabric import api as fab
from base import FabricBase
from utils import add_class_methods_as_module_level_functions_for_fabric as initialize

__version__ = 0.1
__all__ = ['FabricBase', 'initialize', 'fab']