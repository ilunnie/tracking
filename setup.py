from setuptools import setup, find_packages

setup(
    name='tracking',
    version='1.1.0',
    packages=find_packages(),
    description='Monitor a person\'s body with just a webcam',
    long_description_content_type='text/markdown',
    author='ilunnie & marcoshrb',
    url='https://github.com/ilunnie/tracking',
    requires={
        'install': [
            'mediapipe',
            'numpy',
            'opencv_contrib_python'
        ],
        'extras': {
            'tests': ['pytest', 'pytest-cov']
            }
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)