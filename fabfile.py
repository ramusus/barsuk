from fabriclassed import initialize
from fabriclassed.base import BaseFabric, DjangoFabric, VirtualenvFabric
from fabric.api import cd, lcd, local, run, sudo
from os.path import join, dirname
from time import strftime

class Fabric(BaseFabric, DjangoFabric, VirtualenvFabric):
    search_dirs = ['project/templates', 'project/media/js']

    test_default_app = 'barsuk'
    test_settings = 'settings_test'
    shell_plus = True

    hosts = ['ram@kworx.ru']
    remote_project_path = '/var/www/barsuk'
    local_project_path = '/home/ramusus/workspace/barsuk'
    diff_dir = 'diffs'
    applications_dir = 'project/apps'
    patched_applications = (
    )
    media_css_dirs = (
        'project/media/html',
        'project/media/css',
        'project/media/i',
    )
    dump_file = 'data/dump/data.sql.gz'
    fixtures_dir = 'project/fixtures'
    fixtures_map = (
    )

    def fab_deploy(self, migrate=False, upgrade=None):
        '''
        Deploy project to the remote host
            `migrate` boolean argument if neccesary to run syncdb and migrate (south) management commands
            `upgrade` list of applications separated by commas need to upgrade using pip
        '''
        local('git push')
        with cd(self.remote_project_path):
            run('git pull')
#            if migrate:
#                self.run_manage('syncdb')
#                self.run_manage('migrate')
#            if upgrade:
#                self.run_pip('install --upgrade %s' % upgrade.replace(',', ' '))
            sudo('./server restart')
#        sudo('/etc/init.d/celerycam restart')
#        sudo('/etc/init.d/celeryd restart')
#
#    def fab_sync_data(self):
#        '''
#        Synchronize content data (dump + images) from remote host to local
#        '''
#        local('rsync -vr --stats %s:/var/www/movister/%s data/dump' % (self.hosts[0], self.dump_file), capture=False)
#        local('rsync -vr --stats %s:/var/www/movister/data/images/avatars /media/data/work/movister' % self.hosts[0], capture=False)
#        local('rsync -vr --stats %s:/var/www/movister/data/images/images /media/data/work/movister' % self.hosts[0], capture=False)
#        local('cp %s /media/data/work/movister/dump/data_%s.sql.gz' % (self.dump_file, strftime('%Y%m%d')), capture=False)
#
#    def fab_restore_data(self):
#        '''
#        Load content data from dump file to the DB
#        '''
#        local('gunzip %s' % self.dump_file)
#        local('psql -U movister -d movister < %s' % self.dump_file)
#
#    def fab_update_css(self):
#        '''
#        Put remote dirs with css files to the repository and get them on development
#        '''
#        with cd(self.remote_project_path):
#            run('git add %s' % ' '.join(self.media_css_dirs))
#            run('git commit -nm "updated css"')
#            run('git push')
#        local('git pull', capture=False)
#
#    def i18n(self):
#        '''
#        Make i18n files and compile them after finishing translating
#        '''
#        langs = ['ru','en']
#        for lang in langs:
#            local('./manage.py makemessages -sl %s --ignore=*/magnolia/* --ignore=*/django/contrib/flatpages/forms.py --ignore=*/debug_toolbar/js/* --traceback' % lang, capture=False)
#            local('./manage.py makemessages -l %s -d djangojs --ignore=*js/all.r* --traceback' % lang, capture=False)
#        if confirm(u'Are messages ready for compiling?'):
#            local('./manage.py compilemessages', capture=False)

__all__ = initialize(Fabric(), __name__)