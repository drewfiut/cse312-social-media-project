from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, PostForm, CommentForm
import database as db
import secrets
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'abadsecretkey'

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/dm')
def dm():
    return render_template('dm.html')

@app.route('/friends')
def friends():
    return render_template('friends.html')

@app.route('/feed')
def feed():
    return render_template('mainfeed.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        types = form.types.data
        image = form.image.data.read()
        count = form.number.data
        db.insert_project(title, description, types, image, count)
        flash('Project Created for {}.'.format(form.title.data), 'success')
        return redirect(url_for('projects'))
    return render_template('post.html', form=form)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    #return render_template('registration.html')
    form = RegistrationForm()
    if form.validate_on_submit():
        first = form.first_name.data
        last = form.last_name.data
        email = form.email.data
        password = form.password
        db.insert_user(first, last, email, password, 'image')
        flash('Account created for {}!'.format(form.first_name.data), 'success')
        return redirect(url_for('home'))
    return render_template('registration.html', title='Register', form=form)

@app.route('/signin')
def signin():
    form = LoginForm()
    if form.validate_on_submit() :
        email = form.email.data
        password = form.password.data
        db.select_user(email)
        # TODO: Fill in database implementation
        flash('Successful! Welcome {}!'.format(form.first_name.data), 'success')
        return redirect(url_for('home'))
    else :
        return redirect(url_for('registration'))
    return render_template('signin.html')

@app.route('/hippo',  methods=['GET', 'POST'])
def hippo_proj():
    form = CommentForm()
    if form.validate_on_submit():
        user = 'user'
        project = 'hippo'
        comment = form.comment.data
        db.insert_comments(user, project, comment)
    comments = db.select_comment_project('hippo')
    return render_template('hippo_project.html', form=form, comments=comments)

@app.route('/rocket',  methods=['GET', 'POST'])
def rocket_proj():
    form = CommentForm()
    if form.validate_on_submit():
        user = 'user'
        project = 'rocket'
        comment = form.comment.data
        db.insert_comments(user, project, comment)
    comments = db.select_comment_project('rocket')
    return render_template('rocket_project.html', form=form, comments=comments)

@app.route('/likes')
def likes():
    return render_template('likes.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')