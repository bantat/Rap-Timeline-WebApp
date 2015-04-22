#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The server-side script of a very simple web application that involves an HTML
form with two <input type="text"> elements (one named "animal" and the other
named "badanimal").  See tinywebapp.html for the form.

Jadrian Miles, 2015; adapted from Jeff Ondich's sample, 2012.
"""

import cgi

# Get the user input from the client's request.  These can be received by POST
# or GET (or both).
form = cgi.FieldStorage()
animal = form['animal'].value
bad_animal = form['badanimal'].value

# Sanitize the user input. You can't trust users not to mess with
# your scripts. In this case, we allow only letters in our animal
# names. Otherwise, you're stuck with the default animal.
if not animal.isalpha():
    animal = 'DEFAULT ANIMAL'
if not bad_animal.isalpha():
    bad_animal = 'DEFAULT ANIMAL'

# Construct the output page.
output = '''<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <title>Tiny web app results</title>
</head>
<body>
    <p>I like %ss, too.</p>
    <p>Also, %ss are gross.</p>
</body>
</html>
''' % (animal, bad_animal)

# Send the output page back to the client.
print "Content-type: text/html\r\n\r\n",
print output

