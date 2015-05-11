#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'Tore Banta & Charlie Sarano'
import model
import urllib

def buildAlbumPage(content_dictionary):
    """This method takes a dictionary of content strings as an argument, and uses it to populate a template HTML file
    for the album page component of the web application. The method returns a string of HTML text for the album page"""

    #sets the variables to take their place in the template.html file
    album_string = "<h1>%s (%s) </h1>" % (content_dictionary['album'], content_dictionary['year'])
    album_string = indent(album_string,3)
    album_img = "<img src=%s align ='middle'>" % (content_dictionary['image'])
    album_img = indent(album_img,3)
    description = "<p>%s</p>" % (content_dictionary['summary'])
    description = indent(description, 1)
    path = {'artist':content_dictionary['artist_id']} 
    urlpath = urllib.urlencode(path)
    artist = "<h2><a href='index.py?%s'>%s</a></h2>" % (urlpath, content_dictionary['artist_name'])
    artist = indent(artist, 3)

    html_dictionary = {'album': album_string, 'album_img': album_img, 'artist': artist, 'description': description}

    f = open("album.html")
    album_template = f.read()
    f.close()
    #sends the output with the items in the dictionary replaced in the template
    output = album_template.format(**html_dictionary)
    return output


def buildArtistPage(content_dictionary):
    """This method takes a dictionary of content strings as an argument, and uses it to populate a template HTML file
    for the artist page component of the web application. The method returns a string of HTML text for the artist page"""
    f = open("artist.html")
    artist_template = f.read()
    f.close()
    #The first item in content dictionary is the information for the artist
    #sets the dictionary values for the template artists.html
    html_dictionary = {'artist': '', 'image': '', 'description': '', 'albums': ''}
    path = {'artist':content_dictionary[0]['artist_id']} 
    urlpath = urllib.urlencode(path)
    artist_string = "<h2><a href='index.py?%s'>%s </a></h2>" % (urlpath,content_dictionary[0]['artist_name'])
    artist_string = indent(artist_string, 3)
    image_path = "<img src= %s align='middle'>" % (content_dictionary[0]['image'])
    image_path = indent(image_path,3)
    description = "<p>%s</p>" % (content_dictionary[0]['summary'])
    description = indent(description, 1)
    albums_string = "<ul>\n"
    #Every item in the list after the first is a dictionary that contains the information for one album
    #This loop sets the album information to an album string
    for x in range(1, len(content_dictionary)):
        path = {'album':content_dictionary[x]['album_id']} 
        urlpath = urllib.urlencode(path)
        albums_string = albums_string + "<li><a href='index.py?%s'>%s</a></li>" % (urlpath, content_dictionary[x]['album_name'])
        albums_string += '\n'
    albums_string = indent(albums_string, 1)
    html_dictionary['albums'] = albums_string
    html_dictionary['artist'] = artist_string
    html_dictionary['description'] = description
    html_dictionary['image'] = image_path

    output = artist_template.format(**html_dictionary)
    return output



def buildHeaderPage():
    """This method returns a string of HTML text for the header component of a web page for the application."""
    
    f = open("header.html")
    header_string = f.read()
    f.close()
    return header_string


def buildFooterPage():
    """This method returns a string of HTML text for the footer component of a web page for the application."""
    
    f= open("footer.html")
    footer_string = f.read()
    f.close()
    return footer_string


def buildTimelinePage(years_on_timeline):
    """This method builds HTML text for a complete timeline of albums. The method takes a list of years
    as an argument."""

    years_list = years_on_timeline

    timeline_page = ""

    timeline_string = "<p><form action=\"index.py\" method=\"get\">\n"
    timeline_substring = "<select name=\"year\">\n"
    timeline_string += indent(timeline_substring,1)
    timeline_substring = "<option value=\"\" selected>Pick a year</option>\n"
    timeline_string += indent(timeline_substring,2)

    # Builds HTML drop-down menu for selecting year
    for year in years_list:
        timeline_substring = "<option value=\"%d\">%s</option>\n" % (year,str(year))
        timeline_string += indent(timeline_substring,2)

    timeline_substring = "</select>\n"
    timeline_string += indent(timeline_substring,1)
    timeline_substring = "<input type=\"submit\" value=\"Go\"/>\n"
    timeline_string += indent(timeline_substring,1)
    timeline_string += "</form></p>\n\n"

    timeline_page = timeline_page + timeline_string

    timeline_year = ""

    #creates a page by putting together the year pages
    for year in years_on_timeline:
        print year
        content_dictionary = model.getYearContent(year)
        timeline_year = timeline_year + buildYearPage(content_dictionary)

    timeline_page = timeline_page + timeline_year

    return timeline_page


def buildYearPage(content_dictionary):
    """This method takes a dictionary of content strings as an argument, and uses it to populate a template HTML file
    for the year page component of the web application. The method returns a string of HTML text for a year on the
    timeline."""
    year = content_dictionary[0]['year']
    year_string = "<h1> %s </h1>" % (year)
    year_string = indent(year_string, 1)
    html_dictionary = {'year': year_string, 'albums': ''}
    
    albums_in_year_string = "<ul>\n"
    #each line in a dictionary is an album dictionary
    #builds a string so that each album is represented by one string
    for x in range(len(content_dictionary)):
        album_id = content_dictionary[x]['album_id']
        album_name = content_dictionary[x]['album_name']
        artist_name = content_dictionary[x]['artist_name']
        artist_path = {'artist': content_dictionary[x]['artist_id']} 
        urlpath_artist = urllib.urlencode(artist_path)
        album_path = {'album':content_dictionary[x]['album_id']} 
        urlpath_album = urllib.urlencode(album_path)
        album_string = "<li><a href='index.py?%s'>%s</a> - <a href='index.py?%s'>%s</a></li>"
        album_string = album_string % (urlpath_album, album_name, urlpath_artist, artist_name)
        album_string = indent(album_string, 1)
        if x != (len(content_dictionary) - 1):
            album_string += '\n'
        albums_in_year_string += album_string

    #ends the albums for that year, and stops adding bullets
    albums_in_year_string += '\n'
    albums_in_year_string += "</ul>"
    albums_in_year_string = indent(albums_in_year_string, 1)
    html_dictionary['albums'] = albums_in_year_string
    f = open("year.html")
    year_template = f.read()
    f.close()
    #prints the output with the dictionary items taking their place
    output = year_template.format(**html_dictionary)

    return output


def indent(s, k):
    """Indents string argument k number of tab characters (four spaces) for the purposes of HTML page formatting."""

    return "\n".join([" "*(4*k) + line for line in s.splitlines()])
