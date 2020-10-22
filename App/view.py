from flask import render_template, redirect, url_for
from flask import request

from App.forms import *
from App.app import *
from App.models import *


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/stories')
def stories():
    stories = Story.query.all()
    return render_template('stories.html', stories=stories)


@app.route('/story/<slug>')
def story(slug):
    story = Story.query.filter(Story.slug == slug).first()
    tags = story.tag
    return render_template('story.html', story=story, tags=tags)


@app.route('/create_story', methods=['POST', 'GET'])
def create_story():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        if request.form.get('tag'):
            tag = Tag.query.filter(Tag.name == request.form['tag']).first()

        try:
            story = Story(title=title, body=body)
            story.tag.append(tag)
            db.session.add(story)
            db.session.commit()
        except:
            print('Error')
        return redirect(url_for('stories'))

    form = StoryForm()
    return render_template('create_story.html', form=form)


@app.route('/tags')
def tags():
    tags = Tag.query.all()
    return render_template('tags.html', tags=tags)


@app.route('/tag/<slug>')
def tag(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    stories = tag.story.all()
    return render_template('tag.html', tag=tag, stories=stories)


@app.route('/create_tag', methods=['POST', 'GET'])
def create_tag():

    if request.method == 'POST':
        name = request.form['name']

        try:
            tag = Tag(name=name)
            db.session.add(tag)
            db.session.commit()
        except:
            print('Error')
        return redirect(url_for('stories'))

    form = TagForm()
    return render_template('create_tag.html', form=form)
