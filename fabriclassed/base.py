from fabric import api as fab

class FabricBase(object):
    name = ''
    local_file = ''
    remote_file = ''

    def base_task1(self):
        '''base task 1'''
        fab.run('svn export /path/to/{self.name}'.format(self=self))

    def base_task2(self):
        '''base task 2'''
        fab.put(self.local_file, self.remote_file)