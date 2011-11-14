from utils import add_class_methods_as_module_level_functions_for_fabric as initialize
from base import BaseFabric
from django import DjangoFabric
from virtualenv import VirtualenvFabric

VERSION = (0, 3, 2)
__version__ = '.'.join(map(str, VERSION))
__all__ = ['FabricBase', 'DjangoFabric', 'VirtualenvFabric', 'initialize']