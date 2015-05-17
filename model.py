#!/usr/bin/python

"""A module used for generating the necessary content to be used in creating web pages, this module contains methods
for the Model component of our web application.

By Tore Banta & Charlie Sarano
CS 257 - Software Design (Jadrian Miles)
Carleton College
"""

__author__ = 'Tore Banta, Charlie Sarano'

import view
import DataSource


def buildPageBasedOnParameters(cgi_parameters):
    """Takes a dictionary of Common Gateway Interface parameter strings as an argument, and returns a string containing
    the complete HTML text for a web page, based on which parameters exist within the dictionary that is passed."""

    data_source = DataSource.DataSource()

    page_content = ""

    if cgi_parameters['year'] != '':
        year = cgi_parameters['year']

        if int(year) in data_source.getYearsOnTimeline():
            page_content += view.buildHeaderPage()
            page_content += view.buildYearsMenu(data_source.getYearsOnTimeline())
            page_content += view.buildYearPage(getYearContent(year))
            page_content += view.buildFooterPage()
        else:
            error_description = "Invalid year, %s not on timeline." % (str(year))
            page_content += view.buildHeaderPage()
            page_content += view.buildErrorPage(error_description)
            page_content += view.buildYearsMenu(data_source.getYearsOnTimeline())
            page_content += view.buildTimelinePage(data_source.getYearsOnTimeline())
            page_content += view.buildFooterPage()

    elif cgi_parameters['artist'] != '':
        artist = cgi_parameters['artist']

        artist_objects = data_source.getAllArtistsFromDatabase()
        artist_names = []
        for artist_object in artist_objects:
            artist_names.append(artist_object.getArtistName())

        if artist in artist_names:
            page_content += view.buildHeaderPage()
            page_content += view.buildArtistPage(getArtistContent(artist))
            page_content += view.buildFooterPage()
        else:
            error_description = "Invalid artist, %s not in database." % (artist)
            page_content += view.buildHeaderPage()
            page_content += view.buildErrorPage(error_description)
            page_content += view.buildYearsMenu(data_source.getYearsOnTimeline())
            page_content += view.buildTimelinePage(data_source.getYearsOnTimeline())
            page_content += view.buildFooterPage()

    elif cgi_parameters['album'] != '':
        album = cgi_parameters['album']

        album_objects = data_source.getAllAlbumsFromDatabase()
        album_names = []
        for album_object in album_objects:
            album_names.append(album_object.getAlbumName())
        if album in album_names:
            page_content += view.buildHeaderPage()
            page_content += view.buildAlbumPage(getAlbumContent(album))
            page_content += view.buildFooterPage()
        else:
            error_description = "Invalid album, %s not in database." % (album)
            page_content += view.buildHeaderPage()
            page_content += view.buildErrorPage(error_description)
            page_content += view.buildYearsMenu(data_source.getYearsOnTimeline())
            page_content += view.buildTimelinePage(data_source.getYearsOnTimeline())
            page_content += view.buildFooterPage()

    elif cgi_parameters['search'] != '':
        search_string = cgi_parameters['search']

        page_content += view.buildHeaderPage()
        page_content += view.buildSearchResultsPage(getSearchResults(search_string),search_string)
        page_content += view.buildFooterPage()

    else:
        page_content += view.buildHeaderPage()
        page_content += view.buildYearsMenu(data_source.getYearsOnTimeline())
        page_content += view.buildTimelinePage(data_source.getYearsOnTimeline())
        page_content += view.buildFooterPage()

    return page_content


def getAlbumContent(album_name):
    """Takes an album name string as an argument, and returns a dictionary of strings containing content to
    be used in creating the album page."""

    data = DataSource.DataSource()

    album_object = data.getAlbum(album_name)
    content_dictionary = {'album':'','summary':'','image':'','year':'','artist_id':'','artist_name':'','spotify':''}
    content_dictionary['album'] = album_object.getAlbumString()
    content_dictionary['summary'] = cleanDescription(album_object.getAlbumDescription())
    content_dictionary['image'] = album_object.getAlbumImage()
    content_dictionary['year'] = album_object.getAlbumYear()
    content_dictionary['spotify'] = album_object.getAlbumSpotify()
    artist_name = album_object.getAlbumArtist()
    artist_object = data.getArtist(artist_name)
    content_dictionary['artist_id'] = artist_object.getArtistName()
    content_dictionary['artist_name'] = artist_object.getArtistString()

    return content_dictionary


def getArtistContent(artist_name):
    """Takes an artist name string as an argument, and returns a list of dictionaries containing content to be used in
    creating the artist page."""

    data = DataSource.DataSource()

    content_list = []

    artist_object = data.getArtist(artist_name)
    artist_dictionary = {'artist_name':'','artist_id':'','summary':'','image':''}
    artist_dictionary['artist_name'] = artist_object.getArtistString()
    artist_dictionary['artist_id'] = artist_object.getArtistName()
    artist_dictionary['summary'] = cleanDescription(artist_object.getArtistDescription())
    artist_dictionary['image'] = artist_object.getArtistImage()
    content_list.append(artist_dictionary)

    albums = artist_object.getArtistAlbums()
    for album in albums:
        content_dictionary = {'album_id':'','year':'','album_name':''}
        content_dictionary['album_id'] = album.getAlbumName()
        content_dictionary['year'] = album.getAlbumYear()
        content_dictionary['album_name'] = album.getAlbumString()
        content_list.append(content_dictionary)

    return content_list


def getYearContent(year):
    """Takes an integer year value as an argument, and returns a list of dictionaries containing content to be used in
    creating the year page."""

    data = DataSource.DataSource()

    content_list = []

    year_object = data.getYear(year)
    albums = year_object.getAlbumsForYear()
    for album in albums:
        content_dictionary = {'album_id':'','album_name':'','album_img':'','artist_name':'','artist_id':'','year':''}
        content_dictionary['album_name'] = album.getAlbumString()
        content_dictionary['album_id'] = album.getAlbumName()
        content_dictionary['album_img'] = album.getAlbumImage()

        artist_name = album.getAlbumArtist()
        artist_object = data.getArtist(artist_name)

        content_dictionary['artist_name'] = artist_object.getArtistString()
        content_dictionary['artist_id'] = artist_object.getArtistName()
        content_dictionary['year'] = year
        content_list.append(content_dictionary)

    return content_list


def getSearchResults(search_string):
    """Takes a query string that has been provided by the user as an argument, and returns a list of two lists, the
    first containing album object results and the second containing artist object results."""

    data_source = DataSource.DataSource()
    album_objects = data_source.getAllAlbumsFromDatabase()
    artist_objects = data_source.getAllArtistsFromDatabase()
    album_names = []
    artist_names = []

    for album in album_objects:
        album_names.append(album.getAlbumString().lower())
    for artist in artist_objects:
        artist_names.append(artist.getArtistString().lower())

    artist_results = []
    album_results = []

    if " " not in search_string:
        for x in range(len(album_names)):
            if search_string in album_names[x]:
                album_results.append(album_objects[x])
        for x in range(len(artist_names)):
            if search_string in artist_names[x]:
                artist_results.append(artist_objects[x])

    if " " in search_string:
        word_list = search_string.split(" ")
        for word in word_list:
            for x in range(len(album_names)):
                if word in album_names[x]:
                    album_results.append(album_objects[x])
            for x in range(len(artist_names)):
                if word in artist_names[x]:
                    artist_results.append(artist_objects[x])

    artist_results = list(set(artist_results))
    album_results = list(set(album_results))
    
    total_results = [album_results, artist_results]

    return total_results


def cleanDescription(description):
    """Takes a description string, and returns a description string that has been properly formatted for display as HTML
     text."""

    description_edit = description
    for i in range(len(description)):
        if description[i] == '^':
            description_edit = description[:i]
            break

    description = description_edit

    if "\\n" in description:
        description = description.replace("\\n","</p><p>")
    if "\u" in description:
        description = description.replace("\u","&#x")
    if "\\" in description:
        description = description.replace("\\",'')

    return description