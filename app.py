from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, PostForm
import database as db

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
        db.insert_project(title, description, 'none', 'none', 'image')
        flash('Project Created for {}.'.format(form.title.data), 'success')
        return redirect(url_for('projects'))
    return render_template('post.html', form=form)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/registration')
def registration():
    #return render_template('registration.html')
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {}!'.format(form.first_name.data), 'success')
        return redirect(url_for('home'))
    return render_template('registration.html', title='Register', form=form)

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/hippo')
def hippo_proj():
    return render_template('hippo_project.html')

@app.route('/rocket')
def rocket_proj():
    return render_template('rocket_project.html')

@app.route('/likes')
def likes():
    return render_template('likes.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')