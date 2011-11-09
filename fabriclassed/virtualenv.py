from fabric.api import lcd, local
from fabric.context_managers import prefix, settings
from contextlib import contextmanager
from os.path import join, isdir
from os import listdir

class VirtualenvFabric(object):
    '''
    Fabric command file with base virtualenv commands
    '''
    use_virtualenv = True
    virtualenv_dir = 'env'
    patched_applications = [
        # list of applications in format below:
        # applications from repo in env/src/
        # ('django', 'snv'),
        # ('django-mptt-comments', 'git'),
        # applications from pypi in env/lib/python2.6/site-packages/ !!!! exactly app name, not 'django-pagination'
        # ('pagination', 'lib'),
    ]
    diff_dir = 'diffs'

    def _site_packages_path(self):
        return join(self.local_project_path, self.virtualenv_dir, 'lib', 'python2.6', 'site-packages')

    def _site_package_path(self, app_name):
        return join(self._site_packages_path(), app_name)

    def _source_package_path(self, app_name):
        return join(self.local_project_path, self.virtualenv_dir, 'src', app_name)

    @contextmanager
    def virtualenv(self):
        with prefix('source %s/bin/activate' % join(self.local_project_path, self.virtualenv_dir)):
            yield

    def patch(self):
        '''
        Walk over 'diffs' directory and patch every application
        '''
        vcs_commands = {
            'git': 'git checkout .',
            'svn': 'svn revert -R .',
        }
        for patch in listdir(join(self.local_project_path, self.diff_dir)):
            app_name, vcs = patch.split('.')[:-1]
            if vcs == 'lib':
                app_dir = self._site_packages_path()
                if isdir(self._site_package_path(app_name)) and isdir(self._site_package_path('%s.original' % app_name)):
                    # delete patched app and move original app to the normal place
                    with lcd(app_dir):
                        local('rm -R %(app)s && mv %(app)s.original %(app)s' % {'app': app_name}, capture=False)
                # copy app from normal to reserve place for keeping
                with lcd(app_dir):
                    local('cp -R %(app)s %(app)s.original' % {'app': app_name}, capture=False)
            else:
                app_dir = self._source_package_path(app_name)
                # revert files from repo
                with lcd(app_dir):
                    local(vcs_commands[vcs], capture=False)

            with lcd(app_dir):
                local('patch -p0 < %s' % join(self.local_project_path, self.diff_dir, patch), capture=False)

    def diff_dump(self):
        '''
        Walk over map with patched applications and make diff files in 'diffs' directory
        '''
        vcs_commands = {
            'git': 'git diff --no-prefix',
            'svn': 'svn diff',
        }
        for app_name, vcs in self.patched_applications:
            patch_path = join(self.local_project_path, self.diff_dir, '%s.%s.diff' % (app_name, vcs))
            if vcs == 'lib':
                app_dir = self._site_packages_path()
                with lcd(app_dir):
                    with settings(warn_only=True):
                        local('diff -rcx .pyc %s.original %s > %s' % (app_name, app_name, patch_path), capture=False)
            else:
                app_dir = self._source_package_path(app_name)
                with lcd(app_dir):
                    local('%s > %s' % (vcs_commands[vcs], patch_path), capture=False)