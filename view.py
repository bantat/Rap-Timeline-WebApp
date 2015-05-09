#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'Tore Banta & Charlie Sarano'


def buildAlbumPage(content_dictionary):
    """This method takes a dictionary of content strings as an argument, and uses it to populate a template HTML file
    for the album page component of the web application. The method returns a string of HTML text for the album page"""

    return ""


def buildArtistPage(content_dictionary):
    """This method takes a dictionary of content strings as an argument, and uses it to populate a template HTML file
    for the artist page component of the web application. The method returns a string of HTML text for the artist page"""

    return ""


def buildHeaderPage():
    """This method returns a string of HTML text for the header component of a web page for the application."""

    return ""


def buildFooterPage():
    """This method returns a string of HTML text for the footer component of a web page for the application."""

    return ""


def buildTimelinePage(years_on_timeline):
    """This method builds HTML text for a complete timeline of albums. The method takes a list of years
    as an argument."""

    return ""


def buildYearPage(content_dictionary):
    """This method takes a dictionary of content strings as an argument, and uses it to populate a template HTML file
    for the year page component of the web application. The method returns a string of HTML text for a year on the timeline."""

    return ""


def indent(s, k):
    """Indents string argument k number of tab characters (four spaces) for the purposes of HTML page formatting."""

    return "\n".join([" "*(4*k) + line for line in s.splitlines()])