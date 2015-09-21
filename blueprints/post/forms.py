from flask.ext.wtf import Form
from wtforms import validators
from wtforms.ext.sqlalchemy.orm import model_form
import models

PostForm = model_form(models.Post, models.db.session, Form, field_args={
    'name': {'validators': [validators.Required(), validators.Length(min=5, max=20)]},
    'title': {'validators': [validators.Required(), validators.Length(min=5, max=20)]},
    'content': {'validators': [validators.Required(), validators.Length(min=5, max=200)]},
})

CommentForm = model_form(models.Comment, models.db.session, Form, field_args={
    'commenter': {'validators': [validators.Required()]},
    'body': {'validators': [validators.Required()]},
})
