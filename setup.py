from setuptools import setup, find_packages

setup(
    name='climasmart',
    version='0.1.0',
    description='ClimaSmart: A Climate Monitoring Toolkit with SPI, SPEI, VCI, LSTM Forecasting, and GEE Support',
    author='Tadele Melese',
    author_email='tadelemelese21m@gmail.com',
    url='https://github.com/tadele-melese/ClimaSmart',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'scipy',
        'tensorflow',
        'streamlit',
        'geemap',
        'earthengine-api',
        'xarray',
        'rasterio',
        'statsmodels'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.8',
)
