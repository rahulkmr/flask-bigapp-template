from flask import render_template, redirect, url_for, request
from config import db
from . import models, forms


def post_index():
    object_list = models.Post.query.all()
    return render_template('post/index.jinja2', object_list=object_list)

def post_show(id):
    post = models.Post.query.get(id)
    form = forms.CommentForm()
    return render_template('post/show.jinja2', post=post, form=form)

def post_new():
    form = forms.PostForm()
    if form.validate_on_submit():
        post = models.Post(form.name.data, form.title.data, form.content.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('post.index'))
    return render_template('post/new.jinja2', form=form)

def post_edit(id):
    post = models.Post.query.get(id)
    form = forms.PostForm(request.form, obj=post)
    if form.validate_on_submit():
        post.name = form.name.data
        post.title = form.title.data
        post.content = form.content.data
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('post.show', id=id))
    return render_template('post/edit.jinja2', form=form, post=post)

def post_delete(id):
    post = models.Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('post.index'))

def comment_new(post_id):
    post = models.Post.query.get(post_id)
    form = forms.CommentForm()
    if form.validate_on_submit():
        comment = models.Comment(form.commenter.data, form.body.data, post_id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('.show', id=post_id))
    return render_template('post/show.jinja2', post=post, form=form)

def comment_delete(post_id, id):
    comment = models.Comment.query.get(id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('.show', id=post_id))
