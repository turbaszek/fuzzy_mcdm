from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='fmcdm',
      version='0.1',
      description='Simple implementation of fuzzy preference structures and '
                  'tools for fuzzy multi-criteria decision making',
      long_description=readme(),
      classiffiers=[
            'Development Status :: 1 - Planning',
            'Topic :: Scientific/Engineering',
      ],
      keywords='fuzzy preference structures multi-criteria decision making logic decision modeling ',
      url='https://github.com/nuclearpinguin/fuzzy_mcdm.git',
      author='Tomasz Urbaszek',
      author_email='turbaszek@gmail.com',
      license='MIT',
      packages=['fmcdm'],
      install_requires=['numpy'],
      zip_safe=False)