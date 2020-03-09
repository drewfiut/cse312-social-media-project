from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
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

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/hippo')
def hippo_proj():
    return render_template('hippo_project.html')

@app.route('/rocket')
def rocket_proj():
    return render_template('rocket_project.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')