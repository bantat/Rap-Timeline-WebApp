#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'Tore Banta & Charlie Sarano'
import model

def buildAlbumPage(content_dictionary):
    """This method takes a dictionary of content strings as an argument, and uses it to populate a template HTML file
    for the album page component of the web application. The method returns a string of HTML text for the album page"""

    album_string = "<h1 id= album> %s (%s) </h1>" % (content_dictionary['album'], content_dictionary['year'])
    album_string = indent(album_string,1)
    album_img = "<img src=%s style ='width:250px,height:250px'>" % (content_dictionary['image'])
    album_img = indent(album_img,1)
    description = "<p>%s</p>" % (content_dictionary['summary'])
    description = indent(description, 1)
    artist = "<p>%s</p>" % (content_dictionary['artist_name'])
    artist = indent(artist, 1)

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
    artist_string = "<h2> %s </h2>" % (content_dictionary[0]['name'])
    artist_string = indent(artist_string, 1)
    image_path = "<img src= %s style = 'width:250px;height:250px'>" % (content_dictionary[0]['image'])
    image_path = indent(image_path,1)
    description = "<p>%s</p>" % (content_dictionary[0]['summary'])
    description = indent(description, 1)
    albums_string = ""

    for x in range(1, len(content_dictionary)):
        albums_string = albums_string + "<p id=album>%s </p>" % (content_dictionary[x]['album_name'])
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
        print x
        album_name = content_dictionary[x]['album']
        artist_name = content_dictionary[x]['artist']
        album_string = "<li>%s - %s</li>\n" % (album_name, artist_name)
        album_string = indent(album_string, 1)
        albums_in_year_string += album_string
    
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

if __name__ == '__main__':
    year_dict1 = {'album': 'Life is Good','artist': 'Nas','year': '2012'}
    year_dict2 = {'album': 'Control System', 'artist': 'Ab-Soul','year':'2012'}
    dict_list = []
    dict_list.append(year_dict1)
    dict_list.append(year_dict2)
    print buildYearPage(dict_list)