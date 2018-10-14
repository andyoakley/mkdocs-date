from distutils.core import setup

setup(
    name='mkdocs-date',
    version='0.1.0',
    author='Andy Oakley',
    author_email='ao@ao.vc',
    packages=['mkdocs_date'],
    license='LICENSE.txt',
    description='Simple blogging in mkdocs',
    install_requires=[
    ],

    entry_points={
        'mkdocs.plugins': [
            'date = mkdocs_date:Date',
        ]
    }
)
