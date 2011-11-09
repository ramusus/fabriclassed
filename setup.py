from setuptools import setup, find_packages

setup(
    name='fabriclassed',
    version=__import__('fabriclassed').__version__,
    description='Class-based Fabric scripts via a Python metaprogramming hack',
    long_description=open('README').read(),
    author='ramusus',
    author_email='ramusus@gmail.com',
    url='https://github.com/ramusus/fabriclassed',
    download_url='https://github.com/ramusus/fabriclassed/downloads',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    install_requires=[
        'fabric',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
