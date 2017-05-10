import os
from setuptools import setup

environ = os.environ.get('FLASK_ENV')

requirements = [
    # Flask
    'Flask==0.12',

    # Flask extensions
    'Flask-Sqlalchemy',
    'Flask-Wtf',
    'Flask-Babel',
    'Flask-Cache',
    'Flask-Assets',
    'Flask-Script',
    'Flask-Bcrypt',

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
