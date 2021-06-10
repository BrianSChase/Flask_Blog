import sqlite3
from datetime import date
#Functions to work with the blog database


def show_tables():
    """Show all tables"""
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(c.fetchall())

    conn.close()
    
def add_table():
    """Update later to take user input"""
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("CREATE TABLE posts (post_id INTEGER primary key AUTOINCREMENT, title VARCHAR(50), date VARCHAR(14), content TEXT);")
    conn.close()
    
    
def print_table():
    val = input("Enter the table to view ")
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("SELECT * from {}".format(val))
    print(c.fetchall())
    conn.close()


def add_post(title, body):
    """Create new post content, input will be a list"""
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    todays_date = date.today()
    #c.execute("INSERT INTO blog_posts(post_id, title, date, content) values(3, title, '05-05-2021', body);")
    c.execute("INSERT INTO blog_posts(post_id, title, date, content) values(4, title, '02-04-2021', body);")
    conn.commit()
    conn.close()
    
def add_post_test():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("INSERT INTO blog_posts(post_id, title, date, content) values(3, 'test1', '02-04-2021', 'THis will be the content of the post');")
    conn.commit()
    print(c.fetchall())

    conn.close()    

def test():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("Select * from blog_posts;")
    print(c.fetchone()[1])
        

#add_post_test()
#print_table()
#add_table()
#test()
#add_post("internal test", "This is the body test for internal test")