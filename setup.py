#from distutils.core import setup
from setuptools import setup
setup(
  name = 'empath',
  packages = ['empath'], # this must be the same as the name above
  version = '0.084',
  description = 'A tool for text analysis',
  author = 'Ethan Fast',
  author_email = 'ejhfast@gmail.com',
  url = 'https://github.com/Ejhfast/empath-client', # use the URL to the github repo
  download_url = 'https://github.com/Ejhfast/meta/empath-client/0.35',
  keywords = ['social science', 'lexicon', 'text analysis'], # arbitrary keywords
  package_data= { 'empath': ['data/categories.tsv', "data/user/blank"]},
  classifiers = [],
  install_requires=[
          'requests'
  ]
)
