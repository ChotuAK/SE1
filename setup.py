from setuptools import setup, find_packages

setup(
    name='wcpslib',
    version='0.1.0',
    description='A Python library for interacting with WCPS servers for datacube operations.',
    author='Jonathan Brown and Anshu Kushwaha',
    author_email='ankushwaha@constructor.university, ',
    url='https://github.com/Constructor-Uni-SE-non-official/Sprint1_Pair19/tree/main', 
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: GIS'
    ],
    python_requires='>=3.7'
)
