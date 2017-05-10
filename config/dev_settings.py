#: Dev setup. Enable debugger.
DEBUG = True
#: Enable testing for development.
TESTING = True
#: Database to use for SQLAlchemy.
SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/dev.db'
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

USE_X_SENDFILE = False
CACHE_TYPE = 'simple'

#: webassets settings.
ASSETS_DEBUG = True
#: Session signing key.
# setting a string key. flask debugtoolbar was concatenating this with strings and failing.
SECRET_KEY = '8095d1aab8d98613102593955e48258eda86d135'
