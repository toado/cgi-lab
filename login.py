#!/usr/bin/env python3
import os, sys, json
from templates import login_page, secret_page
from secret import username, password

print("Content-Type: text/html")

# How to read cookies
# - https://stackoverflow.com/a/20899685 By user "Mosiur"
is_logged_in = False
if "HTTP_COOKIE" in os.environ:
    # Will probably have more than one cookie, so split them by "; "
    for cookie in os.environ["HTTP_COOKIE"].split("; "):
        key, val = cookie.split("=")
        if key == "logged-in" and val == "true":
            is_logged_in = True
            
if is_logged_in:
    print()
    print(secret_page(username, password))
    
else:
    # ====================================================================================
    # Question 4: How does the POSTed data come to the CGI script?
    # ====================================================================================
    #  - POST data is appended through the request header, and read from stdin
    #       - Answer found "https://stackoverflow.com/a/5451943" By user "slezica"
    #
    #   - Retrieving POSTed data 
    #       - https://stackoverflow.com/a/24638449 -- user "NuclearPeon"
    #       - https://stackoverflow.com/a/27893309 -- user "Schien"
    data_len = os.environ["CONTENT_LENGTH"]

    # Parse POST if a POST exists
    if data_len:
        post_args = sys.stdin.read(int(data_len)).split("&")

        # Verifying POST data
        # If credentials are correct, set a cookie 
        # - Info found on setting cookies: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies 
        post_usr = ""
        post_pwd  = ""
        for arg in post_args:
            arg = arg.split("=")   # split the entered login info (usr & pwd) from field name
            if arg[0] == "username":
                post_usr = arg[1]
            elif arg[0] == "password":
                post_pwd = arg[1]
        if post_usr == username and post_pwd == password:
            print(f"Set-Cookie: logged-in=true")
            print()
            print(f"Set cookies, here is your login info={post_usr} || {post_pwd}")
        
    else:
        print()
    print(login_page())
