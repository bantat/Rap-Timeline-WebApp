#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'Tore Banta & Charlie Sarano'
import model

def buildAlbumPage(content_dictionary):
    """This method takes a dictionary of content strings as an argument, and uses it to populate a template HTML file
    for the album page component of the web application. The method returns a string of HTML text for the album page"""

    html_dict = {'album'='','album_img'='','artist'='','description'=''}
    albumString = "<h1 id= album> %s (%s) </h1>" % (contentDictionary['album'],contentDictionary['year'])
    albumString = indent(albumString,1)
    album_img = "<img src=%s style ='width:250px,height:250px'>" % (contentDictionary['image'])
    album_img = indent(album_img,1)
    description = "<p>%s</p>" % (contentDictionary['summary'])
    description = indent(description, 1)
    artist = "<p>%s</p>" % (contentDictionary['artist_name'])
    artist = indent(artist, 1)

    html_dict{'album'=albumString,'album_img'=album_img,'artist'=artist,'description'=description}

    f = open("album.html")
    album_template = f.read()
    f.close()

    output = album_template.format(**html_dict)
    return output


def buildArtistPage(content_dictionary):
    """This method takes a dictionary of content strings as an argument, and uses it to populate a template HTML file
    for the artist page component of the web application. The method returns a string of HTML text for the artist page"""
    f = open("artist.html")
    artist_template = f.read()
    f.close()

    html_dict = {'artist'='', 'image'='', 'description'= '', 'albums' = ''}
    artist_String = "<h2> %s </h2>" % (contentDictionary[0]['name'])
    artist_String = indent(artist_String, 1)
    image_path = "<img src= %s style = 'width:250px;height:250px'>" % (contentDictionary[0]['image'])
    image_path = indent(image_path,1)
    description = "<p>%s</p>" % (contentDictionary[0]['summary'])
    description = indent(description, 1)
    albumsString = ""

    for x in range(1, len(contentDictionary)):
        albumsString = albumsString + "<p id=album>%s </p>" % (contentDictionary[x]['album_name'])
    albumsString = indent(albumsString, 1)
    html_dict['albums'] = albumsString
    html_dict['artist'] = artist_String
    html_dict['description']=description
    html_dict['image']=image_path

    output = artist_template.format(**html_dict)
    return output



def buildHeaderPage():
    """This method returns a string of HTML text for the header component of a web page for the application."""
    
    f= open("header.html")
    headerString = f.read()
    f.close()
    return headerString


def buildFooterPage():
    """This method returns a string of HTML text for the footer component of a web page for the application."""
    
    f= open("footer.html")
    footerString = f.read()
    f.close()
    return footerString


def buildTimelinePage(years_on_timeline):
    """This method builds HTML text for a complete timeline of albums. The method takes a list of years
    as an argument."""
    
    timelineString= ""
    for year in years_on_timeline:
        contentDictionary= model.getYearContent(year)
        timelineString = timelineString + buildYearPage(contentDictionary)
    return timelineString


def buildYearPage(content_dictionary):
    """This method takes a dictionary of content strings as an argument, and uses it to populate a template HTML file
    for the year page component of the web application. The method returns a string of HTML text for a year on the timeline."""
    year = contentDictionary[0]['year']
    yearString = "<h1> %s </h1>" % (year)
    yearString = indent(yearString, 1)
    html_dict = {'year': yearString, 'albums':''}
    
    albumString = "<ul>\n"

    for x in range(0,len(contentDictionary)):
        albumString = albumString + indent("<li>%s - %s</li>\n"(contentDictionary[x]['album'],contentDictionary[x]['artist']),1)
    
    albumString = indent(albumString, 1)
    html_dict['albums']= albumString
    f= open("year.html")
    year_template = f.read()
    f.close()
    output = year_template.format(**html_dict)

    return output


def indent(s, k):
    """Indents string argument k number of tab characters (four spaces) for the purposes of HTML page formatting."""

    return "\n".join([" "*(4*k) + line for line in s.splitlines()])

def main():
    year_dict=[{'album'= 'Life is Good','artist'='Nas','year'='2012'}
    print buildYearPage(year_dict)










