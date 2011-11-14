from fabric.api import local
import re

class DjangoFabric(object):
    '''
    Fabric command file with base django's manage.py commands
    '''
    managefile_path = './manage.py'
    test_default_app = None
    test_settings = None
    shell_plus = False
    devserver_port = 8000

    def _manage(self, command):
        '''
        Run manage.py command
        '''
        if getattr(self, 'use_virtualenv', False):
            # use virtualenv context manager
            with self.virtualenv():
                local('%(manage)s %(command)s' % {
                    'manage': self.managefile_path,
                    'command': command,
                }, capture=False)
        else:
            local('%(manage)s %(command)s' % {
                'manage': self.managefile_path,
                'command': command,
            }, capture=False)

    def dev(self):
        '''
        Run Django's dev server
        '''
        self._manage('runserver %(host)s:%(port)d' % {
            'host': self.hosts[0] if self._remote() else '127.0.0.1',
            'port': self.devserver_port,
        })

    def sh(self):
        '''
        Run Django's standart shell or shell from django_extentions application if `shell_plus=True`
        '''
        self._manage('shell_plus' if self.shell_plus else 'shell')

    def test(self, test_name=''):
        '''
        Run Django's tests. Argument can be application name, name of test class or method of test class
        '''
        if self.test_default_app:
            # without args => test default application
            if not test_name:
                test_name = self.test_default_app

            # arg is name of test class => add default application
            if re.search(r'^[^\.]+Test', test_name):
                test_name = '.'.join([self.test_default_app, test_name])

        self._manage('test %(name)s %(settings)s' % {
            'name': test_name,
            'settings': ('--settings=%s' % self.test_settings) if self.test_settings else '',
        })