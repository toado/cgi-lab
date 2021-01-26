#!/usr/bin/env python3
import os, json

# ====================================================================================
# Question 1: How do you inspect all environment variables in Python?
# ====================================================================================
# - os.environ
# print('Content-Type: application/json')    # HTTP header, tells browser what type of file we're sending
# print() # Add extra line b/c 
# print(json.dumps(dict(os.environ), indent=2))

# print('Content-Type: text/plain')
# print()
# print("HELLOW, WORLD!!!!! :3333")

# ====================================================================================
# Question 2: What environment variable contains the query parameter data?
# ====================================================================================
#     - os.environ['QUERY_STRING']
print('Content-Type: text/html')
print()
print("""
<!doctype html>
<html>
<body>
<h1>HELLO I AM HTML</h1>
""")

print(f"<p> QUERY_STRING={os.environ['QUERY_STRING']} </p>")
print("<ul>")
for param in os.environ['QUERY_STRING'].split('&'):
    (name, value) = param.split('=')
    print(f"<li><em>{name}</em> = {value}</li>")

print("""
</ul>
</body>
</html>
""")

# ====================================================================================
# Question 3: What environment variable contains information about the user’s browser?
# ====================================================================================
#     - 

# ====================================================================================
# Question 4: How does the POSTed data come to the CGI script?
# ====================================================================================
#     - 

# ====================================================================================
# Question 5: What is the HTTP header syntax to set a cookie from the server?
# ====================================================================================
#     - 

# ====================================================================================
# Question 6: What is the HTTP header syntax the browser uses to send the cookie back?
# ====================================================================================
#     - 

# ====================================================================================
# Question 7: In your own words, what are cookies used for? 
# ====================================================================================
#     - 