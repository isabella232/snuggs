from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='parsnip',
      version='0.0.1',
      description=u"Parsnip parses and evaluates lisp-like Numpy expressions",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Sean Gillies",
      author_email='sean@mapbox.com',
      url='https://github.com/sgillies/parsnip',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'numpy',
          'pyparsing'
      ],
      extras_require={
          'test': ['pytest'],
      })
