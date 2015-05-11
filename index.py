#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'Tore Banta & Charlie Sarano'

import model
import DataSource
import cgi
import cgitb
import urlparse

cgitb.enable()


def main():
    data_source = DataSource.DataSource()
    parameters = getCgiParameters()
    page_content = model.buildPageBasedOnParameters(parameters)
    print 'Content-type: text/html\r\n\r\n'
    print page_content


def getCgiParameters():
    """Sanitizes and returns a dictionary of CGI parameters needed for page content generation."""
    data = cgi.FieldStorage()
    parameters = {'year' : '', 'artist' : '','album' : ''}
    if 'year' in data:
        year = data['year'].value
        parameters['year'] = sanitizeUserInput(year)

    if 'artist' in data:
        artist = data['artist'].value
        parameters['artist'] = sanitizeUserInput(artist)

    if 'album' in data:
        album = data['album'].value
        parameters['album'] = sanitizeUserInput(album)

    return parameters


def sanitizeUserInput(input):
    """Removes characters from user input string which might be used to perform SQL injection."""
    illegal_chars = ";\\:\"<>@"
    for ch in illegal_chars:
        input = input.replace(ch, '')
    return input


if __name__ == '__main__':
    main()