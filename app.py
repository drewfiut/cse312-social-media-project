from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, PostForm, CommentForm
from base64 import b64encode
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
    project_list = db.select_projects_all()
    projects = []
    for item in project_list:
        image = b64encode(item[3]).decode('"utf-8"')
        indiv = {'title': item[0],
                 'description': item[1],
                 'type': item[2],
                 'image': image,
                 'count': item[4],
                 'id': item[5]
                }
        projects.append(indiv)
    return render_template('projects.html', projects=projects)

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
    return render_template('signin.html')

@app.route('/likes')
def likes():
    return render_template('likes.html')

@app.route('/project/<int:project_id>',  methods=['GET', 'POST'])
def project(project_id):
    data = db.select_project(project_id)
    if data:
        data = data[0]
        image = b64encode(data[3]).decode('"utf-8"')
        project = {'title': data[0],
                    'description': data[1],
                    'type': data[2],
                    'image': image,
                    'count': data[4]
                    }
        form = CommentForm()
        if form.validate_on_submit():
            user_id = 1
            comment = form.comment.data
            db.insert_comments(user_id, project_id, comment)
            return redirect(url_for('project', project_id=project_id))
        comment_list = db.select_comment_project(project_id)
        comments = []
        for comment in comment_list:
            user = db.select_user(comment[0])[0]
            x = {'name': user[0] + ' ' + user[1], 'text': comment[1]}
            comments.append(x)
        return render_template('project.html', project=project, form=form, comments=comments)
    return render_template('404.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')