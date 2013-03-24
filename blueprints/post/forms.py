from flask.ext.wtf import Form, validators
from wtforms.ext.sqlalchemy.orm import model_form
import models


PostForm = model_form(models.Post, models.db.session, Form, field_args = {
    'name': {'validators': [validators.Required()]},
    'title': {'validators': [validators.Required()]},
    'content': {'validators': [validators.Required()]},
})

CommentForm = model_form(models.Comment, models.db.session, Form, field_args = {
    'commenter': {'validators': [validators.Required()]},
    'body': {'validators': [validators.Required()]},
})
