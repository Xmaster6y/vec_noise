import sys

from setuptools import setup, Extension

import numpy

if sys.platform != 'win32':
    compile_args = ['-funroll-loops']
else:
    # XXX insert win32 flag to unroll loops here
    compile_args = []

setup(
    package_dir={'vec_noise': 'src/vec_noise'},
    setup_requires=['numpy'],
    install_requires=['numpy'],
    ext_modules=[
        Extension('vec_noise._simplex', ['src/vec_noise/_simplex.c'],
            extra_compile_args=compile_args,
            include_dirs=[numpy.get_include()],
        ),
        Extension('vec_noise._perlin', ['src/vec_noise/_perlin.c'],
            extra_compile_args=compile_args,
            include_dirs=[numpy.get_include()],
        )
    ],
)
