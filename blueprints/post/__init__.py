from lib.utils import http_dont_auth
import config.settings as settings

BEFORE_REQUESTS = [http_dont_auth(settings.HTTP_USERNAME, settings.HTTP_PASSWORD,
                                  'post.index', 'post.show', 'post.comment_new')]
