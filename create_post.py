"""This will be the function that creates new blog content. it will accept data from the create
html page, and then store it in the database."""

from flask import Flask, url_for, render_template, request, redirect
import cgi, cgitb 
import sqlite3
def create_post():
    # Create instance of FieldStorage 
    form = cgi.FieldStorage() 

    # Get data from fields, title and content of blog post
    title = form.getvalue('title')
    content  = form.getvalue('content')

    #enter the title and content into database
    #id for post will also need to be created
    print("hello from create post\n")
    print ("Content-type:text/html\r\n\r\n")
    print ("<html>")
    print ("<head>")
    print ("<title>Hello - Second CGI Program</title>")
    print ("</head>")
    print ("<body>")
    print ("<h2>Hello %s %s</h2>") % (title, content)
    print ("</body>")
    print ("</html>")
