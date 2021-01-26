#!/usr/bin/env python3
import os, json
from templates import login_page, secret_page

# ====================================================================================
# Question 1: How do you inspect all environment variables in Python?
# ====================================================================================
#       - os.environ
# print('Content-Type: application/json')    # HTTP header, tells browser what type of file we're sending
# print() # Add extra line b/c 
# print(json.dumps(dict(os.environ), indent=2))


# ====================================================================================
# Question 2: What environment variable contains the query parameter data?
# ====================================================================================
#     - os.environ['QUERY_STRING']

# Output of a CGI script consists of 2 sections 
# - which is separated by a blank line
# - 1st section contains header(s)
# - 2nd section is usually HTML (which we print as well))
print('Content-Type: text/html')    # HTTP header, tells browser what type of file we're sending
print()                             # Blank line follows, end of headerse

print("""
<!doctype html>
<html>
<body>
<h1>Lab 3</h1>
""")
if len(os.environ["QUERY_STRING"]) > 0:
    print(f"<p> QUERY_STRING={os.environ['QUERY_STRING']} </p>")
    print("<ul>")
    for param in os.environ["QUERY_STRING"].split('&'):
        (name, value) = param.split('=')
        print(f"<li><em>{name}</em> = {value}</li>")
    print("</ul>")

else: 
    print(f"<p> QUERY_STRING: <ul><li>No Query Found</li></ul></p>")


# ====================================================================================
# Question 3: What environment variable contains information about the user’s browser?
# ====================================================================================
#       - os.environ["HTTP_USER_AGENT"]
print("<p>User's Browser Info=<ul><li>{}</li></ul></p>".format(os.environ["HTTP_USER_AGENT"]))

print("""
</body>
</html>
""")
