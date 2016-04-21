from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'} #fake name
	posts = [ #fake array of posts
		{
			'author': {'nickname': 'John'},
			'body': 'Beautiful day in Portland'
		},
		{
			'author': {'nickname': 'Susan'},
			'body': 'The Witch was such a scary movie!'
		},
		{
			'author': {'nickname': 'Mike'},
			'body': "Some of you are cool, don't go to school tomorrow >:)"
		},
	]
	return render_template("index.html", title='Home', 
										user=user, 
										posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' % 
			(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html',
							title='Sign In',
							form=form, 
							providers=app.config['OPENID_PROVIDERS'])