from setuptools import setup

setup(name='nocps',
      version='0.1',
      description='API for NOC-PS provisioning system',
      url='https://github.com/noonedeadpunk/nocps/',
      author='Dmytro Rabotiahov',
      author_email='contact@nodead.net',
      license='MIT',
      packages=['nocps'],
      install_requires=[
          'xmlrpclib;python_version<"3"',
      ],
      python_requires='>=2.2',
      zip_safe=False) 
