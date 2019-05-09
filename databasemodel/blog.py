from databasemodel import db


class Blog(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    blog_name = db.Column(db.String(80), unique=True)
    blog_content = db.Column(db.String(255), unique=True)
    create_time = db.Column(db.Date, unique=True)

    def __init__(self, blog_name, blog_content, create_time):
        self.blog_name = blog_name
        self.blog_content = blog_content
        self.create_time = create_time

    def __repr__(self):
        return '<Blog %r>' % self.blog_name