from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.ext.sqlalchemy.orm import model_form
from . import models

PostForm = model_form(models.Post, models.db.session, FlaskForm, field_args={
    'name': {'validators': [validators.Required(), validators.Length(min=5, max=20)]},
    'title': {'validators': [validators.Required(), validators.Length(min=5, max=20)]},
    'content': {'validators': [validators.Required(), validators.Length(min=5, max=200)]},
})

CommentForm = model_form(models.Comment, models.db.session, FlaskForm, field_args={
    'commenter': {'validators': [validators.Required()]},
    'body': {'validators': [validators.Required()]},
})
