import os
import subprocess
import sys
import platform
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from setuptools.command.install import install

class CMakeBuild(build_ext):
    def run(self):
        # This is where CMake will be called
        for ext in self.extensions:
            self.build_cmake(ext)

    def build_cmake(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = [
            f'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}',
            f'-DPYTHON_EXECUTABLE={sys.executable}',
        ]

        build_args = ['--config', 'Release']
        if platform.system() == "Windows":
            cmake_args += ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE=' + extdir]
            build_args += ['--', '/m']
        else:
            build_args += ['--', '-j2']

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        # Run CMake configure
        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=self.build_temp)
        # Run CMake build
        subprocess.check_call(['cmake', '--build', '.'] + build_args, cwd=self.build_temp)

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        super().__init__(name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

setup(
    name='pyobj',
    version='0.0.2',
    packages=['pyobj'],
    ext_modules=[CMakeExtension('pyobj/fast_obj', sourcedir='src/fast_obj')],
    cmdclass=dict(build_ext=CMakeBuild),
    zip_safe=False,
    platforms=["linux"],
)
