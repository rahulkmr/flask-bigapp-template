from config import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    title = db.Column(db.String(200))
    content = db.Column(db.Text)

    def __init__(self, name, title, content):
        self.name = name
        self.title = title
        self.content = content

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    commenter = db.Column(db.String(80))
    body = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post', backref=db.backref('comments', lazy='dynamic'))

    def __init__(self, commenter, body, post_id):
        self.commenter = commenter
        self.body = body
        self.post_id = post_id
