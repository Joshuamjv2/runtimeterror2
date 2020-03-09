from flask import Flask, render_template, url_for, flash, redirect
from forms import Registrationform, LoginForm
app  = Flask(__name__)

app.config['SECRET_KEY'] = '14408aea95dec75a6d3ba51954b52498'

posts = [
    {
        'author':'Joshua Bryant',
        'title':'Blog post 1',
        'content':'Blog post content',
        'date_posted':'Apri 22, 2020'
    },

    {
        'author':'Jack Bryant',
        'title':'Blog post 2',
        'content':'Blog post content too',
        'date_posted':'Apri 24, 2020'
    }

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = Registrationform()
    if form.validate_on_submit():
        flash(f'Account created for {{ form.username.data }}!', 'succes')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)

if __name__ == '__main__':
    app.run(debug=True)


