Learning Notes for Flask
========================

10.24
-----
+ virtualenv
    + create a virtual env
    + after 'activate', it is the python environment we working on
+ directory structure
    + root directory
        + env (the virtual environment we created above)
        + templates
        + static
            + css
            + js
            + img
        + app
            + __init__.py
            + view.py
        + run.py
        + config.py
+ how to create a 'Flask' object
    '''python
    from flask import Flask
    app = Flask(__name__)
    '''
+ using database
    + flask-sqlalchemy
    + need to create a database object
        '''python
        app.config['SQLALCHEMY_DATABASE'] = 'sqlite:////tmp/test.db'
        db = SQLAlchemy(app)
        '''
    + it looks like I need to create a class for row of db
        + class Name(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            username = db.Column(db.String(80), unique=True)
            def __init__(self.--,--):----
            def __repr__(self): ---
    + database method
        + db.session.add(--)
            + add info into db
        + db.session.commit
            + save info into db
        + Name.query.all()
            + return list of dicts
        + Name.query.filter_by(username = '---').first()
        + Name.query.filter_by(username = '---').all()
+ some methods
    + @app.route('/', method = ['GET', 'POST'])
        def index():
    + render\_tamplate('--.html', input\_argument)
    + app.debug = True
    + redirect(url\_for('index'))
    + request.form['username']
    + dynamic url
        ''' python
        @app.route('/profile/<username>')
        def profile(username):
            ----
        '''
        + @app.before_first_request
+ html
    + form
        + method = 'post'
        + action = '/post_user' (redirect to 'post_user' after submit)
    + {% for user in users %}
        <li> {{ user.name }} </li>
      {% endfor %}
    + double bracket for variable
        {{ username }}

10.25
-----
+ user authentation
    + flask-login
    + flask-security: new, recommended
    + how to do
        + paster some template codes from online
        + app.config['SECRET_KEY'] = '----'
        + app.config['SECRET_REAGISTERABLE'] = True
        + after login successfully, redirect to root directory
        + @login_required
        + /register, /login, /logout
    + encrypt password
    + how to use template for security page
        + copy and paste original templates from flask-security
            package folder
        + paste into --/template/security/
+ bootstrap
    + startbootstrap: can download some free templates here
    + homepage is called index
+ flask - html
    + {% extends 'layout.html' %}
    + in layout.html {% block --- %}{% endblock %}
    + in index.html {% block ---} ---- {% endblock %}
    + {{ variable_name }}
+ small notes
    + forward slash '/' means directory
