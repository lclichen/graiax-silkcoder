from setuptools import Extension, setup
from glob import glob
import sys


ext = Extension('graiax.silkcoder._silkv3',
                sources=[*glob('src/c_silkv3/src/*.c'),
                         *glob("src/c_silkv3/*.c"),],
                include_dirs=["src/c_silkv3/interface/"])

if sys.byteorder == "big":
    ext.define_macros.append(("_SYSTEM_IS_BIG_ENDIAN", True))

setup(
    ext_modules=[ext]
)