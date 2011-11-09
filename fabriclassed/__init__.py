from fabric import api as fab
from utils import add_class_methods_as_module_level_functions_for_fabric as initialize
from base import BaseFabric
from django import DjangoFabric
from virtualenv import VirtualenvFabric

__version__ = 0.2
__all__ = ['FabricBase', 'DjangoFabric', 'VirtualenvFabric', 'initialize', 'fab']