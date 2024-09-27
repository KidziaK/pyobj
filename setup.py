from setuptools import setup

setup(
    name='pyobj',
    version="0.0.1",
    description='Python wrapper for fast_obj C library for loading .obj files (https://github.com/thisistherk/fast_obj)',
    author='Mikolaj Kida',
    author_email='kida.miko@gmail.com',
    packages=['pyobj'],
    package_data={
        'pyobj': [
            "lib/*"
        ]
    },
    include_package_data=True,
    platforms=["linux"]
)
