import os
from setuptools import setup

environ = os.environ.get('FLASK_ENV')

requirements = [
    # Flask
    'Flask==0.10',

    # Flask extensions
    'Flask-Sqlalchemy==2.0',
    'Flask-Wtf==0.12',
    'Flask-Babel==0.9',
    'Flask-Cache==0.13.1',
    'Flask-Assets==0.11',
    'Flask-Script==2.0.5',
    'Flask-Bcrypt==0.6.2',

    # Misc 3rd party
    'augment==0.4',
]

# Add dev dependencies.
if not environ or environ == 'dev':
    requirements += [
        # 'closure',
        'jsmin',
        'cssmin',

        # db migrations
        'alembic',

        # Dev requirements
        'flask-debugtoolbar',
        'pylint',
        'ipython',
        'ipdb',
        'gevent'
        ]


setup(
    name='Flask Template',
    version="0.1",
    install_requires=requirements
)
