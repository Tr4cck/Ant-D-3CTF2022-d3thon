from distutils.core import setup
from Cython.Build import cythonize

setup (
    name = 'd3thon',
    ext_modules = cythonize("src/byte_analizer.py")
)