#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'Tore Banta, Charlie Sarano'

import model
import urllib

def buildAlbumPage(content_dictionary):
    """This method takes a dictionary of content strings as an argument, and uses it to populate a template HTML file
    for the album page component of the web application. The method returns a string of HTML text for the album page"""

    # Sets the variables to take their place in the template.html file
    album_string = "<h1>%s (%s) </h1>" % (content_dictionary['album_name'], content_dictionary['year'])
    album_string = indent(album_string,3)
    album_img = "<img src=%s align ='middle'>" % (content_dictionary['image'])
    album_img = indent(album_img,3)
    description = "<p>%s</p>" % (content_dictionary['summary'])
    description = indent(description, 3)

    # Following 2 lines are to create the path from the album page to the artist page
    path = {'artist':content_dictionary['artist_id']} 
    urlpath = urllib.urlencode(path)

    # Checking if the spotify links are available, and if they are we change the output. 
    spotify_id = content_dictionary['spotify']
    spotify_string = ""
    if spotify_id != "NONE":
        spotify_string = "<iframe src='https://embed.spotify.com/?uri=%s' frameborder = '0' width = '300'" \
                         " height= '380' allowtransparency = 'true'></iframe> " % (spotify_id)
        spotify_string = indent(spotify_string, 3)
    artist = "<h2><a href='index.py?%s'>%s</a></h2>" % (urlpath, content_dictionary['artist_name'])
    artist = indent(artist, 3)
    album_id = content_dictionary['album_id']
    album_url = ""
    #trying to create the wikipedia link with the urlencode, but if that doesn't work, then replacing the string with underscores should
    try:
        album_url = urllib.urlencode(album_id)
    except:
        album_url = album_id.replace(' ','_')

    more_info="<p><a href=http://en.wikipedia.org/wiki/%s>Wikipedia: %s</a></p>" % (album_url, album_id)
    more_info = indent(more_info,3)
    # Finalizing the html dictionary
    html_dictionary = {'album': album_string, 'album_img': album_img, 'artist': artist, 'description': description, 'spotify':spotify_string, /
    'more_info':more_info}

    f = open("album.html")
    album_template = f.read()
    f.close()
    # Sends the output with the items in the dictionary replaced in the template
    output = album_template.format(**html_dictionary)
    return output


def buildArtistPage(content_dictionary):
    """This method takes a dictionary of content strings as an argument, and uses it to populate a template HTML file
    for the artist page component of the web application. The method returns a string of HTML text for the artist page"""
    f = open("artist.html")
    artist_template = f.read()
    f.close()
    # The first item in content dictionary is the information for the artist
    # Sets the dictionary values for the template artists.html
    html_dictionary = {'artist': '', 'image': '', 'description': '', 'albums': '','more_info':''}
    artist_string = "<h2> %s </h2>" % (content_dictionary[0]['artist_name'])
    artist_string = indent(artist_string, 3)
    image_path = "<img src= %s align='middle'>" % (content_dictionary[0]['image'])
    image_path = indent(image_path,3)
    description = "<p>%s</p>" % (content_dictionary[0]['summary'])
    description = indent(description, 3)
    
    # Every item in the list after the first is a dictionary that contains the information for one album
    # This loop sets the album information to an album string
    albums_string = ""
    for x in range(1, len(content_dictionary)):
        path = {'album':content_dictionary[x]['album_id']} 
        urlpath = urllib.urlencode(path)
        albums_string = albums_string + "<p><a href='index.py?%s'>%s</a></p>" % (urlpath, content_dictionary[x]['album_name'])
        albums_string += '\n'
    albums_string = indent(albums_string, 3)
    artist_id = content_dictionary[0]['artist_id']
    

    # Creating the path for the wikipedia link
    artist_url = ""
    try:
        artist_url = urllib.urlencode(artist_id)
    except:
        artist_url = artist_id.replace(' ','_')
    more_info="<p><a href=http://en.wikipedia.org/wiki/%s>Wikipedia: %s</a></p>" % (artist_url,artist_id)
    more_info = indent(more_info,3)

    # Finalizing the dictionary to pass
    html_dictionary['albums'] = albums_string
    html_dictionary['artist'] = artist_string
    html_dictionary['description'] = description
    html_dictionary['image'] = image_path
    html_dictionary['more_info']=more_info

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


def buildErrorPage(error_description):
    """This method is used if the user tries to pass invalid input to the url, and returns a simple description of why their page could
    not be printed. """

    error_string = "<p>System Error: "
    error_string += error_description
    error_string += "</p>\n<br>"

    return error_string


def buildYearsMenu(years_on_timeline):
    """Creates the button that appears at the top of the page that allows the user to select a year spefically"""
    # Sets up the form for options 
    timeline_string = "<p><form action=\"index.py\" method=\"get\">"
    timeline_string += '\n'
    timeline_substring = "<select name=\"year\">"
    timeline_substring += '\n'
    timeline_string += indent(timeline_substring,1)
    timeline_substring = "<option value=\"\" selected>Pick a year</option>"
    timeline_substring += '\n'
    timeline_string += indent(timeline_substring,2)

    # Builds HTML drop-down menu for selecting year
    for year in years_on_timeline:
        string_year = str(year)
        timeline_substring = "<option value=\"%d\">%s</option>" % (year,string_year)
        timeline_substring += '\n'
        timeline_string += indent(timeline_substring,2)

    timeline_substring = "</select>"
    timeline_substring += '\n'
    timeline_string += indent(timeline_substring,1)
    timeline_substring = "<input type=\"submit\" value=\"Go\"/>"
    timeline_substring += '\n'
    timeline_string += indent(timeline_substring,1)
    timeline_string += "</form></p>"
    timeline_string += '\n'

    return timeline_string


def buildTimelinePage(years_on_timeline):
    """This method builds HTML text for a complete timeline of albums. The method takes a list of years
    as an argument."""

    timeline_string = ""

    # Creates a page by putting together the year pages
    for year in years_on_timeline:
        content_dictionary = model.getYearContent(year)
        timeline_string = timeline_string + buildYearPage(content_dictionary)

    return timeline_string


def buildYearPage(content_dictionary):
    """This method takes a dictionary of content strings as an argument, and uses it to populate a template HTML file
    for the year page component of the web application. The method returns a string of HTML text for a year on the
    timeline."""
    year = content_dictionary[0]['year']
    year_string = "<h1 id='year'> %s </h1>" % (year)
    year_string = indent(year_string, 1)
    html_dictionary = {'year': year_string, 'albums': ''}
    
    albums_in_year_string = "<ul>\n"
    # Each line in a dictionary is an album dictionary
    # Builds a string so that each album is represented by one string
    for x in range(len(content_dictionary)):
        album_id = content_dictionary[x]['album_id']
        album_name = content_dictionary[x]['album_name']
        artist_name = content_dictionary[x]['artist_name']
        artist_path = {'artist': content_dictionary[x]['artist_id']} 
        urlpath_artist = urllib.urlencode(artist_path)
        album_path = {'album':content_dictionary[x]['album_id']} 
        urlpath_album = urllib.urlencode(album_path)
        #sets the image, and the button class on the year page for css page
        image_src = "<img src=%s>" % content_dictionary[x]['album_img']
        album_string = "<a class ='btn' href='index.py?%s'>%s<h3>%s</h3></a><p id='artist_timeline'><a href='index.py?%s'>%s</a></p>"
        album_string = album_string % (urlpath_album, image_src, album_name, urlpath_artist, artist_name)
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


def buildSearchResultsPage(results_list, search_string):
    """This method searches for the input that the user gave, and prints out whether or not the string could be found"""

    album_results = results_list[0]
    artist_results = results_list[1]

    results_string = ""
    #preset message if the results don't return anything on the website
    if len(album_results)==0 and len(artist_results) == 0:
        no_results_string = "<p id='no_results'><b> We're sorry, but that search didn't return anything. We may not have the " \
        "artist you want, but please feel free to try a different phrase, or write us an email if you feel an important artist is" \
        "missing</b></p>"
        return no_results_string
    else:
        #counts the results on the page
        num_results=0
        #for each result, builds a link to the page with the name of the item
        for album in album_results:
            num_results += 1
            album_name = album.getAlbumName()
            album_string = album.getAlbumString()
            artist = album.getAlbumArtist()
            #album link
            album_link = "<h2><a href='index.py?album=%s'>%s</a></h2>" % (album_name, album_string)
            #artist link to add to the album link
            album_link += "<p> An album by <a href='index.py?artist=%s'>%s</a></p>" % (artist, artist)
            results_string += album_link
        for artist in artist_results:
            num_results += 1
            artist_name = artist.getArtistName()
            artist_string = artist.getArtistString()
            artist_link = "<h2><a href='index.py?artist=%s'>%s</a></h2>" % (artist_name,artist_string)
            results_string +=artist_link
    
    f= open("search.html")
    search_template = f.read()
    f.close()

    #added for style
    search_string += "..."

    html_dictionary = {'search_string':search_string,'results':results_string, 'num_results':num_results}
    output= search_template.format(**html_dictionary)

    return output


def indent(s, k):
    """Indents string argument k number of tab characters (four spaces) for the purposes of HTML page formatting.
    Taken from Jadrian Miles's code for similar purpose"""

    return "\n".join([" "*(4*k) + line for line in s.splitlines()])
