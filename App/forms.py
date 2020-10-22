from wtforms import Form, StringField, TextAreaField, SelectField

from App.models import Tag


T_LST = [x.name for x in Tag.query.all()]


class StoryForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')
    tag = SelectField('Tag', choices=T_LST)


class TagForm(Form):
    name = StringField('Name')
