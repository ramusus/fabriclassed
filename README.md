#### Introduction

We had several Fabric scripts which violated DRY. Class-based Fabric script can solve this issue.
This is a hack to enable the definition of Fabric tasks as methods in a class instead of just as module level functions.
This class-based approach provides the benefits of inheritance and method overriding.

#### Example usage:

```python
from fabriclassed import initialize
from fabriclassed.base import BaseFabric, DjangoFabric, VirtualenvFabric
from fabric import api as fab

class Fabric(BaseFabric):
    remote_project_path = '/local/path/to/my_project'
    local_project_path = '/remote/path/to/my_project'

    def fab_task(self):
        '''My website task'''
        fab.local('echo "Hello world"')

__all__ = initialize(Fabric(), __name__)
```

Every method with prefix 'fab_' will became a fabric command. Running fab -l gives:

```
$ fab -l
Available commands:

    del_pyc          Remove all .pyc files inside in fabfile and child direc...
    search           Search string amoung source code inside directories fro...
    task             My website task
```

Running fab task gives:

```
$ fab task
[localhost] local: echo "Hello world"
Hello world

Done.
```

#### Extended usage with Django under Virtualenv:

DjangoFabric and VirtualenvFabric classes contains various of tools to work with Django in Virtualenv environment. You can use both of these toos together or separately, as you like.

Example of Fabric class with a bunch of properies:

```python
from fabriclassed import initialize
from fabriclassed.base import BaseFabric, DjangoFabric, VirtualenvFabric
from fabric.api import lcd, local

class Fabric(BaseFabric, DjangoFabric, VirtualenvFabric):
    search_dirs = []

    hosts = ['website.com']
    remote_project_path = '/local/path/to/my_project'
    local_project_path = '/remote/path/to/my_project'

    # django settings
    managefile_path = './manage.py'
    test_default_app = 'name_of_my_main_django_application'
    test_settings = 'settings_test_special_file'
    shell_plus = True
    devserver_port = 8000

    # virtualenv settings
    use_virtualenv = True
    virtualenv_dir = 'env'
    patched_applications = [
        # list of virtualenv patched applications
    ]
    diff_dir = 'my_relative_to_project_diffs_dir'
    applications_dir = 'my_relative_to_project_apps_dir'

__all__ = initialize(Fabric(), __name__)
```

Running fab -l gives:

```
Available commands:

    del_pyc          Remove all .pyc files inside in fabfile and child direc...
    dev              Run Django's dev server
    diff_dump        Walk over map of patched applications and make diff fil...
    patch            Walk over 'diffs' directory and patch every application
    search           Search string amoung source code inside directories fro...
    sh               Run Django's standart shell or shell from django_extent...
    symlink          Create symlink from 'apps' dir to the site-packages or ...
    test             Run Django's tests. Argument can be application name, n...
```

#### Installation:

To install the latest version of fabriclassed, just use command:

```
pip install fabriclassed
```