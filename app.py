from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, PostForm, CommentForm, LoginForm
from base64 import b64encode
import database as db
import secrets
import os
from flask_socketio import SocketIO, send, emit
from flask_bcrypt import Bcrypt
import io
from PIL import Image
from flask_login import LoginManager, login_user, UserMixin, current_user, logout_user, login_required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abadsecretkey'
socketio = SocketIO(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'signin'

@login_manager.user_loader
def load_user(user_id):
    return User.get_user(user_id)

class User(UserMixin):

    def __init__(self, id):
        user = db.select_user(id)
        if user:
            user = user[0]
            self.id = id
            self.first_name = user[0]
            self.last_name = user[1]
            self.email = user[2]
            self.password = user[3]
            self.image = b64encode(user[4]).decode('"utf-8"')

    def get_user(id):
        user = User(id)
        return user


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')

@app.route('/friends')
@login_required
def friends():
    instances = db.select_friends(current_user.id)
    friends = []
    for item in instances:
        friend_id = 0
        if item[0] == current_user.id:
            friend_id = item[1]
        else:
            friend_id = item[0]
        friend = db.select_user(friend_id)
        image = b64encode(friend[4]).decode('"utf-8"')
        indiv = {
                 'first_name': friend[1],
                 'last_name': friend[2],
                 'image': image,
                 'id': friend[0]
                }
        friends.append(indiv)

    return render_template('friends.html', friends=friends, title='Friends')

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
    return render_template('mainfeed.html', projects=projects, title='Main Feed')

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        types = form.types.data
        image = form.image.data.read()
        count = form.number.data
        auth_id = current_user.id
        project_id = db.insert_project(title, description, types, image, count, auth_id)
        flash('Project Created for {}.'.format(form.title.data), 'success')
        image = b64encode(image).decode('"utf-8"')
        socketio.emit('update', {'title': title, 'description': description, 'types': types, 'image': image, 'count': count, 'id': project_id}, namespace='/posts')
        return redirect(url_for('projects'))
    return render_template('post.html', form=form, title='Post')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Profile')

@app.route('/projects')
@login_required
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
    return render_template('projects.html', projects=projects, title='My Projects')

@app.route('/dm/<int:friend_id>',  methods=['GET', 'POST'])
@login_required
def dm(friend_id):
    user_id = current_user.id
    messages = []
    first_name = db.select_name(friend_id)[0]
    last_name = db.select_name(friend_id)[1]
    full_name = first_name + ' ' + last_name
    messages_list = db.select_messages(current_user.id, friend_id)
    for message in messages_list:
        if message[0] == friend_id:
            indiv = {
                 'first_name': first_name,
                 'message': message[2]
                }
            messages.append(indiv)
        else:
            indiv = {
                 'first_name': 'You',
                 'message': message[2]
                }
            messages.append(indiv)
    messages.reverse
    return render_template('dm.html', name = full_name, messages=messages, title='Direct Messages')

@socketio.on('message', namespace='/message')
def handle_my_message_event(data):
    sender_id = current_user.id
    receiver_id = data['project_id']
    message = data['message'];
    db.insert_message(sender_id, receiver_id)
    first_name = db.select_name(receiver_id)[0]
    emit('update', {'first_name': first_name, 'message': message})


@socketio.on('like', namespace='/likes')
def handle_my_custom_event(data):
    user_id = current_user.id
    project_id = data['project_id']
    liked = db.is_liked(user_id, project_id)
    if not liked:
        db.insert_likes(user_id, project_id)
        likes = db.select_likes_count(project_id)[0][0]
        emit('update', {'project_id': project_id, 'likes': likes}, broadcast=True)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    #return render_template('registration.html')
    if current_user.is_authenticated:
        return redirect(url_for('feed'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        first = form.first_name.data
        last = form.last_name.data
        email = form.email.data
        image = form.image.data
        if not image:
            image = Image.open('static/user_default.jpg', mode='r')
            imgByteArr = io.BytesIO()
            image.save(imgByteArr, format=image.format)
            image = imgByteArr.getvalue()
        else:
            image = form.image.data.read()
        db.insert_user(first, last, email, hashed_password, image)
        flash('Account created for {}!'.format(form.first_name.data), 'success')
        return redirect(url_for('signin'))
    return render_template('registration.html', title='Register', form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('feed'))
    form = LoginForm()
    if form.validate_on_submit() :
        user = db.select_user_email(form.email.data)
        if user and bcrypt.check_password_hash(user[0][3], form.password.data):
            usernew = User(user[0][0])
            login_user(usernew)
            return redirect(url_for('feed'))
        else:
            flash('Try Again', 'warning')
        return redirect(url_for('signin'))
    return render_template('signin.html', title='Sign In', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/likes')
@login_required
def likes():
    return render_template('likes.html', title='Likes')

@app.route('/project/<int:project_id>',  methods=['GET', 'POST'])
def project(project_id):
    data = db.select_project(project_id)
    if data:
        data = data[0]
        image = b64encode(data[3]).decode('"utf-8"')
        author = db.select_user(data[5])[0]
        project = {'title': data[0],
                    'description': data[1],
                    'type': data[2],
                    'image': image,
                    'count': data[4],
                    'id': project_id,
                    'author_name': author[0] + ' ' + author[1]
                    }
        form = CommentForm()
        comment_list = db.select_comment_project(project_id)
        comments = []
        for comment in comment_list:
            user = db.select_user(comment[0])[0]
            x = {'name': user[0] + ' ' + user[1], 'text': comment[1]}
            comments.append(x)
        return render_template('project.html', project=project, form=form, comments=comments, title=project.get('title'))
    return render_template('404.html'), 404

@socketio.on('comment', namespace='/comments')
def handle_my_custom_event(data):
    user_id = current_user.id
    project_id = data['project_id']
    comment = data['comment']
    db.insert_comments(user_id, project_id, comment)
    user = db.select_user(user_id)[0]
    name = user[0] + ' ' + user[1]
    comment = clean_html(comment)
    emit('update', {'name': name, 'project_id': project_id, 'comment': comment}, broadcast=True)

def clean_html(data):
    data = data.replace('&', '&amp;')
    data = data.replace('<', '&lt;')
    data = data.replace('>', '&gt;')
    data = data.replace('"', '&quot;')
    data = data.replace("'", '&apos;')
    return data

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=8000)