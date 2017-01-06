from setuptools import setup

setup(
    name='dockercli',
    version='0.1',
    py_modules=['dockercli'],
    install_requires=[
        'Click',
        'docker'
    ],
    entry_points='''
        [console_scripts]
        dockercli=dockercli:cli
    ''',
)
