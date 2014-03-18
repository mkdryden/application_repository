from distutils.core import setup

import version


setup(name='application_repository',
      version=version.getVersion(),
      description='A Django site for serving versioned application and '
      'plug-in downloads.',
      keywords='application distribute plugin download django',
      author='Christian Fobel',
      url='http://github.com/cfobel/application_repository.git',
      license='GPL',
      packages=['application_repository',
                'application_repository.application',
                'application_repository.application.scripts',
                'application_repository.plugins',
                'application_repository.plugins.scripts',
                'application_repository.repository'],
      package_data={'application_repository': ['settings.py.skeleton',
                                               'app_data/.empty_file',
                                               'config/apache/*',
                                               'config/postgresql/*',
                                               'plugin_data/.empty_file'],
                    'application_repository.plugins': ['*.skeleton']})
