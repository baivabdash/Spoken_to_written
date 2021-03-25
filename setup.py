import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
	name = 'speech_to_text',
      packages = ['speech_to_text'],
      version='0.1',
      description='Reusable library to convert spoken english text to written',
      author='Baivab Dash',
      author_email='dbaivab@gmail.com',
      url='https://github.com/cyberdhiman/Spoken-To-Written-English',
      classifiers = ['Intended Audience :: Developers',
      					'Programming Language :: Python'],

     )
