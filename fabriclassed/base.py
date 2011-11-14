from fabric import api as fab
from os.path import exists

class BaseFabric(object):

    hosts = []
    remote_project_path = ''
    local_project_path = ''

    search_dirs = []
    search_exclude_patterns = [".pyc", ".svn", ".tmp_"]

    def __init__(self):
        fab.hosts = self.hosts

    def _remote(self):
        '''
        Returns true if we run fabfile remotely.
        Script check existing local_project_path directory
        '''
        return not exists(self.local_project_path)

    def search(self, string=''):
        '''
        Search string amoung source code inside directories from `search_dirs` property
        '''
        fab.local('grep -r %(string)s %(dirs)s %(exclude)s' % {
            'string': string,
            'dirs': ' '.join(self.search_dirs),
            'exclude': '| ' + ' | '.join(['grep -v "%s"' % pattern for pattern in self.search_exclude_patterns]) if len(self.search_exclude_patterns) else '',
        }, capture=False)