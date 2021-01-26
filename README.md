# CMPUT404 CGI Experiments

Experimenting with CGI server stuff!

Question 1: How do you inspect all environment variables in Python?
    
    - os.environ

Question 2: What environment variable contains the query parameter data?
    
    - QUERY_STRING    -->   os.environ["QUERY_STRING"]

Question 3: What environment variable contains information about the user’s browser?
    
    - HTTP_USER_AGENT   -->   os.environ["HTTP_USER_AGENT"]

Question 4: How does the POSTed data come to the CGI script?

    - POST data is appended through the request header, and read from stdin
    - https://stackoverflow.com/a/5451943

Question 5: What is the HTTP header syntax to set a cookie from the server?
    
    - "Set-Cookie: <cookie-name>=<cookie-value>"

Question 6: What is the HTTP header syntax the browser uses to send the cookie back?
    
    - HTTP_COOKIE

Question 7: In your own words, what are cookies used for? 
    
    - a store of information (key-value pairs) that the browser memorizes -- essentially like a cache?