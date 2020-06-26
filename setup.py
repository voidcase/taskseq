from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).parent

README = (HERE / 'README.md').read_text()

VERSION = '0.1.0'

NAME = 'taskseq'

setup(
        name=NAME,
        version=VERSION,
        description='Script to quickly sequence taskwarrior tasks',
        long_description=README,
        long_description_content_type='text/markdown',
        url='https://github.com/voidcase/{NAME}',
        download_url=f'https://github.com/voidcase/{NAME}/archive/v{VERSION}.tar.gz',
        author='Isak Lindhé',
        author_email='isak.e.lindhe@gmail.com',
        license='MIT',
        py_modules=['taskseq'],
        packages=find_packages(),
        python_requires='>=3.6',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Environment :: Console',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Operating System :: POSIX',
            'Operating System :: MacOS',
            ],
        install_requires=['taskw'],
        entry_points={
            'console_scripts': [
                'taskseq=taskseq:run',
            ],
        }
)
