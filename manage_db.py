import sqlite3
#Functions to work with the blog database


def show_tables():
    """Show all tables"""
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(c.fetchall())

    conn.close()
    
def add_table():
    """Update later to take user input instead of being hard coded"""
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("CREATE TABLE blog_posts (post_id INTEGER primary key, title VARCHAR(50), date VARCHAR(14), content TEXT);")
    conn.close()
    
    
def print_table():
    val = input("Enter the table to view ")
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("SELECT * from {}".format(val))
    print(c.fetchall())
    conn.close()


def add_post(input):
    """This will take a file and put it in the database"""
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()

    print(c.fetchall())

    conn.close()
    
def add_post_test():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("INSERT INTO blog_posts(post_id, title, date, content) values(1, 'test0', '02-04-2021', 'THis will be the content of the post');")
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
test()