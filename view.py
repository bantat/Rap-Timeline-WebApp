#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'Tore Banta & Charlie Sarano'
import model
import urllib

def buildAlbumPage(content_dictionary):
    """This method takes a dictionary of content strings as an argument, and uses it to populate a template HTML file
    for the album page component of the web application. The method returns a string of HTML text for the album page"""

    album_string = "<h1>%s (%s) </h1>" % (content_dictionary['album'], content_dictionary['year'])
    album_string = indent(album_string,3)
    album_img = "<img src=%s align ='middle'>" % (content_dictionary['image'])
    album_img = indent(album_img,3)
    description = "<p>%s</p>" % (content_dictionary['summary'])
    description = indent(description, 1)
    path = {'artist':content_dictionary['artist_id']} 
    urlpath = urllib.urlencode(path)
    artist = "<p><a href='index.py?%s'>%s</a></p>" % (urlpath, content_dictionary['artist_name'])
    artist = indent(artist, 3)

    html_dictionary = {'album': album_string, 'album_img': album_img, 'artist': artist, 'description': description}

    f = open("album.html")
    album_template = f.read()
    f.close()

    output = album_template.format(**html_dictionary)
    return output


def buildArtistPage(content_dictionary):
    """This method takes a dictionary of content strings as an argument, and uses it to populate a template HTML file
    for the artist page component of the web application. The method returns a string of HTML text for the artist page"""
    f = open("artist.html")
    artist_template = f.read()
    f.close()

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
    
    timeline_string= ""
    for year in years_on_timeline:
        content_dictionary = model.getYearContent(year)
        timeline_string = timeline_string + buildYearPage(content_dictionary)
    return timeline_string


def buildYearPage(content_dictionary):
    """This method takes a dictionary of content strings as an argument, and uses it to populate a template HTML file
    for the year page component of the web application. The method returns a string of HTML text for a year on the
    timeline."""
    year = content_dictionary[0]['year']
    year_string = "<h1> %s </h1>" % (year)
    year_string = indent(year_string, 1)
    html_dictionary = {'year': year_string, 'albums': ''}
    
    albums_in_year_string = "<ul>\n"

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

    albums_in_year_string += '\n'
    albums_in_year_string += "</ul>"
    albums_in_year_string = indent(albums_in_year_string, 1)
    html_dictionary['albums'] = albums_in_year_string
    f = open("year.html")
    year_template = f.read()
    f.close()
    output = year_template.format(**html_dictionary)

    return output


def indent(s, k):
    """Indents string argument k number of tab characters (four spaces) for the purposes of HTML page formatting."""

    return "\n".join([" "*(4*k) + line for line in s.splitlines()])

# if __name__ == '__main__':
#     # year_dict1 = {'album': 'Life is Good','artist': 'Nas','year': '2012'}
#     # year_dict2 = {'album': 'Control System', 'artist': 'Ab-Soul','year':'2012'}
#     # dict_list = []
#     # dict_list.append(year_dict1)
#     # dict_list.append(year_dict2)
#     # print buildYearPage(dict_list)
#     artist_dict1 = {'name':'Eminem','summary':'Eminem Summary','image':'eminem_is_cool.jpg'}
#     artist_dict2 = {'album_id':'The Marshall Mathers LP','year':2000,'album_name':'The Marshall Mathers LP'}
#     artist_dict3 = {'album_id':'The Slim Shady LP','year':1999,'album_name':'The Slim Shady LP'}
#     dict_list = []
#     dict_list.append(artist_dict1)
#     dict_list.append(artist_dict2)
#     dict_list.append(artist_dict3)
#     print buildArtistPage(dict_list)