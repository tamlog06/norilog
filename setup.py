import os
from setuptools import setup, find_packages

def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''

setup(
    name='norilog',
    version='1.0.0',
    description='The NoriLog web application.',
    long_description=read_file('README.rst'),
    author='tam1006',
    author_email='tamusyun1006@gmail.com',
    url='https://github.com/tam1006/norilog/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Flask',
        'Licence :: OSI Approved :: BSD Licence',
        'Programming Language :: Python',
    ],
    packages=find_packages(),
    include_package_data=True,
    keywords=['web', 'norilog'],
    license='BSD License',
    install_requires=[
        'Flask',
    ],
    entry_points="""
        [console_scripts]
        norilog = norilog:main
    """,
)