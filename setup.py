from setuptools import setup

setup(
    name='ehostess',
    version='0.0.3',
    description='A toolkit for working with eHost, pyConText, and other annotation and NLP tools.',
    url='https://github.com/MMontgomeryTaggart/eHostess',
    author='Max Taggart',
    author_email = "max.taggart@utah.edu",
    license='MIT',
    packages = ['eHostess', 
        'eHostess.Analysis',
        'eHostess.Annotations',
        'eHostess.DevelopmentAids',
        'eHostess.eHostInterface',
        'eHostess.MongoDBInterface',
        'eHostess.NotePreprocessing',
        'eHostess.PyConTextInterface',
        'eHostess.PyConTextInterface',
        'eHostess.PyConTextInterface.SentenceSplitters',
        'eHostess.Utilities'
        ],
    package_dir={'eHostess.PyConTextInterface' : 'PyConTextInterface'},
    package_data = {'eHostess.PyConTextInterface' : ['TargetsAndModifiers/*.tsv']},
    download_url = 'https://github.com/MMontgomeryTaggart/eHostess/archive/0.0.3.tar.gz'
)
