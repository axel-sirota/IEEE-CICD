from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      url='https://github.com/axel-sirota/IEEE-CICD',
      author='Axel Sirota',
      author_email='axel.sirota@example.com',
      license='MIT',
      packages=['funniest'],
      test_suite='nose.collector',
      tests_require=['nose']
      )
