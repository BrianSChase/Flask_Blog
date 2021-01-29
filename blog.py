"""
This will be a template for starting flask projects


"""

from flask import Flask, url_for, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
#import encryption as e
from hashlib import blake2b
from markupsafe import escape
import sqlite3

app = Flask(__name__)


conn = sqlite3.connect('blog.db')

c = conn.cursor()




"""

c.execute('''CREATE TABLE users
            (user_id text, password text)''')
            
       
c.execute("INSERT INTO users VALUES ('admin','blogferr10!')")
# Save (commit) the changes
conn.commit()
"""
for row in c.execute("SELECT user_id, password from users"):
    print(row)
#e.encrypt_store_password('admin')   
    
#This commented out section is how you can hash and update a password    
"""
c.execute("SELECT password from users where user_id = 'admin'")
val = c.fetchone()
print(val[0])


h = blake2b()
b = bytes(val[0], 'utf-8')
h.update(b)
print(h.hexdigest())


#Update password to the hash value
c.execute("UPDATE users set password = '{}' where user_id = '{}'".format(h.hexdigest(), 'admin'))
conn.commit()
"""

c.execute("UPDATE users set password = '{}' where user_id = '{}'".format('flaskword', 'admin'))
conn.commit()

conn.close()



@app.route('/test')
def test():
    return render_template('test.html')


      
    
@app.route('/')
def index():
    return render_template('index.html')

    
@app.route('/page2')
def page2():
    return render_template('page2.html')
    
@app.route('/blog_post')
def blog_post():
    return render_template('blog_post.html')
    
    
@app.route('/user')
def user():
    return render_template('user.html')
    
    
@app.route('/login',methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'flaskword':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)
 
 
 
@app.route('/register', methods=['POST', 'GET']) 
def register():
    error = None 
    if request.method == 'POST':
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        username = request.form['username']
        password = request.form['password']
      
        pw = generate_password_hash(password)
        c.execute("INSERT INTO users VALUES ('{}','{}!')".format(username, pw))

        conn.commit()
        conn.close()
    return render_template('register.html', error=error)

    





@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))



