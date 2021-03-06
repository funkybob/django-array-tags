from setuptools import setup, find_packages

with open('README.md') as fin:
    long_description = fin.read()

setup(
    name='django-array-tags',
    version='0.2.2',
    description='Simple Tagging for Django using PG ArrayField',
    long_description=long_description,
    author='Curtis Maloney',
    author_email='curtis@tinbrain.net',
    url='http://github.com/funkybob/django-array-tags',
    packages = find_packages(exclude=('tests*',)),
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    requires = [
        'Django (>=1.7)',
    ],
    install_requires = [
        'Django>=1.7',
    ],
)
