#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import os
import secret
from http.cookies import SimpleCookie


s = cgi.FieldStorage() #Q4
username = s.getfirst("username")
password = s.getfirst("password")

form_ok = username == secret.username and password == secret.password

#Q5 from the type HTTP_COOKIE from the os environment

cookie = SimpleCookie(os.environ.get(("HTTP_COOKIE")))
cookie_username = None
cookie_password = None

if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

cookie_ok = cookie_username == secret.username and cookie_password == secret.password

if cookie_ok:
    username = cookie_username
    password = cookie_password

print("Content-Type: text/html")
if form_ok:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")


if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(login_page())
    print(after_login_incorrect())

#Q5 Set-Cookie: username=

#Q6 