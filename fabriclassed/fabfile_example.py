from fabriclassed import FabricBase, initialize, fab

class Fabric(FabricBase):
    name = 'website'
    local_file = '/local/path/to/my_website'
    remote_file = '/remote/path/to/my_website'

    def task(self):
        '''my website task'''
        fab.local('echo "Hello world"')

__all__ = initialize(Fabric(), __name__)