from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, PostForm, CommentForm, LoginForm
from base64 import b64encode
import database as db
import secrets
import os
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abadsecretkey'
socketio = SocketIO(app)

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
    project_list = db.select_projects_all()
    projects = []
    for item in project_list:
        image = b64encode(item[3]).decode('"utf-8"')
        id = item[5]
        likes = db.select_likes_count(id)[0][0]
        indiv = {
                 'title': item[0],
                 'description': item[1],
                 'type': item[2],
                 'image': image,
                 'count': item[4],
                 'id': id,
                 'likes': likes
                }
        projects.append(indiv)
    projects.reverse()
    return render_template('mainfeed.html', projects=projects)

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        types = form.types.data
        image = form.image.data.read()
        count = form.number.data
        project_id = db.insert_project(title, description, types, image, count)
        flash('Project Created for {}.'.format(form.title.data), 'success')
        image = b64encode(image).decode('"utf-8"')
        socketio.emit('update', {'title': title, 'description': description, 'types': types, 'image': image, 'count': count, 'id': project_id}, namespace='/posts')
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
        id = item[5]
        likes = db.select_likes_count(id)[0][0]
        indiv = {
                 'title': item[0],
                 'description': item[1],
                 'type': item[2],
                 'image': image,
                 'count': item[4],
                 'id': id,
                 'likes': likes
                }
        projects.append(indiv)
    projects.reverse()
    return render_template('projects.html', projects=projects)


@socketio.on('like', namespace='/likes')
def handle_my_custom_event(data):
    user_id = data['user_id']
    project_id = data['project_id']
    db.insert_likes(user_id, project_id)
    likes = db.select_likes_count(project_id)[0][0]
    emit('update', {'project_id': project_id, 'likes': likes}, broadcast=True)

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
                    'count': data[4],
                    'id': project_id
                    }
        form = CommentForm()
        comment_list = db.select_comment_project(project_id)
        comments = []
        for comment in comment_list:
            user = db.select_user(comment[0])[0]
            x = {'name': user[0] + ' ' + user[1], 'text': comment[1]}
            comments.append(x)
        return render_template('project.html', project=project, form=form, comments=comments)
    return render_template('404.html'), 404

@socketio.on('comment', namespace='/comments')
def handle_my_custom_event(data):
    user_id = data['user_id']
    project_id = data['project_id']
    comment = data['comment']
    db.insert_comments(user_id, project_id, comment)
    user = db.select_user(user_id)[0]
    name = user[0] + ' ' + user[1]
    emit('update', {'name': name, 'project_id': project_id, 'comment': comment}, broadcast=True)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')