#### Introduction

This is a hack to enable the definition of Fabric tasks as methods in a class instead of just as module level functions. This class-based approach provides the benefits of inheritance and method overriding.

We had several Fabric scripts which violated DRY. Class-based Fabric script can solve this issue.

#### Example usage:

```python
from fabriclassed import FabricBase, initialize, fab
    
class Fabric(FabricBase):
    name = 'website'
    local_file = '/local/path/to/my_website'
    remote_file = '/remote/path/to/my_website'
    
    def task(self):
        '''my website task'''
        fab.local('echo "Hello world"')
   
__all__ = initialize(Fabric(), __name__)
```

Running fab -l gives:

```
$ fab -l
Available commands:

    task  my website task
```

