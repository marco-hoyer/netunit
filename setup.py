from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='netunit',
      version='0.1',
      description='Network testing framework',
      long_description=long_description,
      author='Marco Hoyer',
      author_email='marco_hoyer@gmx.de',
      url='https://github.com/marco-hoyer/netunit',
      packages=['netunit'],
      )
