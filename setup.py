import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='haystack-static-pages',
    version='0.2.0alpha',
    description="Static pages for Haystack",
    long_description=read('README'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Framework :: Django',
    ],
    author='David Sauve',
    author_email='dsauve@trapeze.com',
    url='http://github.com/trapeze/haystack-static-pages/',
    license='BSD',
    py_modules=['xapian_backend'],
)
