from setuptools import setup

setup(
    name='gitopen',
    version='0.0.1',
    description='A command line tool for opening Git repository page in your browser',
    url='https://github.com/suzaku/gitopen',
    author='satoru',
    author_email='satorulogic@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    py_modules=["gitopen"],
    entry_points={
        'console_scripts': [
            'gitopen=gitopen:main'
        ]
    }
)
