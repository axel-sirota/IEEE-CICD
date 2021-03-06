from setuptools import setup

setup(name='funniest_ieee',
      version='0.5',
      description='The funniest_ieee joke in the world',
      url='https://github.com/axel-sirota/IEEE-CICD',
      author='Axel Sirota',
      author_email='axel.sirota@example.com',
      license='MIT',
      KEYWORDS = ["class", "attribute", "boilerplate"],
      CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
    ],
      packages=['funniest_ieee'],
      install_requires=[
        'nose',
        'pylint',
        'coverage',
        'nosexcover',
        'flake8',
        'twine'
      ],
      test_suite='nose.collector',
      tests_require=['nose']
      )
