import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='haystack-static-pages',
    version='0.2.1alpha',
    description="Static pages for Haystack",
    long_description=read('README.rst'),
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
    packages=[
        'haystack_static_pages',
        'haystack_static_pages.management',
        'haystack_static_pages.management.commands',
    ],
    package_data={
        'haystack_static_pages': ['templates/*']
    }
)
