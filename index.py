#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'Tore Banta & Charlie Sarano'

import model
import cgi
import cgitb

cgitb.enable()


def main():
    parameters = getCgiParameters()
    page_content = model.buildPageBasedOnParameters(parameters)
    print page_content


def getCgiParameters():
    """Sanitizes and returns a dictionary of CGI parameters needed for page content generation."""
    data = cgi.FieldStorage()
    parameters = {'year' : '', 'artist' : '','album' : ''}
    if 'year' in data:
        parameters['year'] = sanitizeUserInput(data['year'].value)

    if 'artist' in data:
        parameters['artist'] = sanitizeUserInput(data['artist'].value)

    if 'album' in data:
        parameters['album'] = sanitizeUserInput(data['album'].value)

    return parameters


def sanitizeUserInput(input):
    """Removes characters from user input string which might be used to perform SQL injection."""
    illegal_chars = ";,\\/:'\"<>@"
    for ch in illegal_chars:
        input = input.replace(ch, '')
    return input


if __name__ == '__main__':
    main()