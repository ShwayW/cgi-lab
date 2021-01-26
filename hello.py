#!/usr/bin/env python3
from templates import *
from http.cookies import SimpleCookie
import requests
import cgi
import secret
import json
import os
import sys

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

# print(json.dumps(dict(os.environ)))

for p in os.environ.keys():
	print("<li>" + p + ": " + os.environ[p] + "</li>")

page = "<br>"
page += "<li>QUERY_STRING: " + os.environ["QUERY_STRING"]
page += "</li>" + "<li>HTTP_USER_AGENT: " + os.environ["HTTP_USER_AGENT"]
page += "</li>"
print(page)
print(login_page())
print("<br>")

form = cgi.FieldStorage()
post_usrname = form["username"].value
post_pswrd = form["password"].value

print(f"<p> POSTED: <pre>")
print("username: ", post_usrname, "<br>")
print("password: ", post_pswrd, "<br>")
print("</pre></p>")

if secret.username == post_usrname and secret.password == post_pswrd:
	# set cookies
	print("Set cookies: UserID = {}<br>".format(post_usrname))
	print("Set cookies: UserPassword = {}".format(post_pswrd))

c = SimpleCookie(os.environ["HTTP_COOKIE"])
c_username = ""
c_password = ""
if c.get("UserID"):
	c_username = c.get("UserID").value
print(c_username)
if c.get("UserPassword"):
	c_password = c.get("UserPassword").value
print(c_password)