# RETRIEVING DATA FROM THE INTERNET
import urllib.request  # This line imports the urllib.request module,

# which provides tools for working with URLs (Uniform Resource Locators)
# and making HTTP requests to web servers.

pass  # this is a placeholder, do-nothing statement

weburl = urllib.request.urlopen("http://www.google.com")
# This line attempts to open a connection to a specific URL.

print("result code:", weburl.getcode())
# This line prints the HTTP status code of the response from the URL.
# The getcode() method returns the HTTP status code,
# which typically indicates whether the request was successful or encountered an error.
# A common success code is 200 (OK), while various error codes might include 404 (Not Found),
# 500 (Internal Server Error), and others.

data = weburl.read()
# This line reads the content of the webpage (or resource) from the URL that was opened in step 2 and stores it in the variable data.
# This content is typically in the form of bytes.

print(data)
# This line prints the content of the webpage to the console.
