from datetime import datetime
import re

from App.app import db


def slugify(s):
    string = r'[^\w+]'
    return re.sub(string, '-', s.lower())


st_table = db.Table('story_tag',
                        db.Column('story_id', db.Integer, db.ForeignKey('story.id')),
                        db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                    )


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    slug = db.Column(db.String, unique=True)
    time = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Story, self).__init__(*args, **kwargs)
        self.slug_gen()

    def slug_gen(self):
        self.slug = slugify(self.title)

    tag = db.relationship('Tag', secondary=st_table, backref=db.backref('story', lazy='dynamic'))  # Bridge to Tag table and back

    def __repr__(self):
        return 'id: {}, title: {}'.format(self.id, self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'id: {}, name: {}'.format(self.id, self.name)

