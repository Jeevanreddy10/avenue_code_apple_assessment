from setuptools import setup, find_packages

setup(
    name='apple_stock_analysis',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'matplotlib',
        'mplfinance',
        'pytest'
    ],
)

