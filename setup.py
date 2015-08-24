from setuptools import setup, find_packages
import os

version = '1.0.0.dev0'

tests_require = [
]


setup(name='ftw.autofeature',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" + open(
          os.path.join("docs", "HISTORY.txt")).read(),

      classifiers=[
          "Environment :: Web Environment",
          'Framework :: Plone',
          'Framework :: Plone :: 4.3',
          "Intended Audience :: Developers",
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],

      keywords='ftw autofeature',
      author='4teamwork AG',
      author_email='mailto:info@4teamwork.ch',
      url='https://github.com/4teamwork/ftw.autofeature',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'path.py',
          'setuptools',
      ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """)
