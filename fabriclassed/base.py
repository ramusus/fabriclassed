from fabric import api as fab
from os.path import exists, join
from contrib.django import DjangoFabric
from contrib.virtualenv import VirtualenvFabric

__all__ = ['BaseFabric', 'DjangoFabric', 'VirtualenvFabric']

class BaseFabric(object):

    hosts = []
    remote_project_path = ''
    local_project_path = ''

    search_dirs = []
    search_exclude_patterns = [".pyc", ".tmp_"]
    search_exclude_dir_patterns = [".svn", "migrations", ".git", "*.egg-info"]

    def __init__(self):
        fab.env.hosts = self.hosts

    def is_remote(self):
        '''
        Returns true if we run fabfile remotely.
        Script check existing local_project_path directory
        '''
        return not exists(self.local_project_path)

    @property
    def project_path(self):
        '''
        Returns project path (dep or dev) depends on current directory sctructure
        '''
        return self.remote_project_path if self.is_remote() else self.local_project_path

    def project_path_join(self, *args):
        '''
        Regular os.path.join() with prepended project_path
        '''
        return join(self.project_path, *args)

    def fab_search(self, string=''):
        '''
        Search string amoung source code inside directories from `search_dirs` property
        '''
        fab.local('grep -R "%(string)s" %(dirs)s %(exclude)s' % {
            'string': string,
            'dirs': ' '.join(self.search_dirs),
            'exclude': ' '.join(['--exclude "%s"' % pattern for pattern in self.search_exclude_patterns] \
                + ['--exclude-dir "%s"' % pattern for pattern in self.search_exclude_dir_patterns]),
        }, capture=False)

    def fab_del_pyc(self):
        '''
        Remove all .pyc files inside in fabfile and child directories
        '''
        fab.local('find -name \*.pyc -delete')