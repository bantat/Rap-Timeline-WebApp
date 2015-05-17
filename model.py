#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'Tore Banta & Charlie Sarano'

import view
import DataSource


def buildPageBasedOnParameters(parameters):
    """This method takes a dictionary of strings as an argument, and returns a string containing the complete HTML text
    for a web page, based on which parameters exist within the dictionary that is passed."""

    data_source = DataSource.DataSource()

    page_content = ""

    if parameters['year'] != '':
        year = parameters['year']

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
    elif parameters['artist'] != '':
        artist = parameters['artist']
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
    elif parameters['album'] != '':
        album = parameters['album']
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
    elif parameters['search'] != '':
        search_string = parameters['search']
        page_content += view.buildHeaderPage()
        page_content += view.buildSearchResultsPage(getSearchResults(search_string))
        page_content += view.buildFooterPage()
    else:
        page_content += view.buildHeaderPage()
        page_content += view.buildYearsMenu(data_source.getYearsOnTimeline())
        page_content += view.buildTimelinePage(data_source.getYearsOnTimeline())
        page_content += view.buildFooterPage()

    return page_content


def getAlbumContent(album_name):
    """This method takes an album name string as an argument, and builds a dictionary of strings containing content to
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
    """This method takes an artist name string as an argument, and builds a dictionary of strings containing content to
    be used in creating the artist page."""

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
    """This method takes an integer year value as an argument, and builds a dictionary of strings containing content to
    be used in creating the year page."""

    data = DataSource.DataSource()

    content_list = []

    year_object = data.getYear(year)
    albums = year_object.getAlbumsForYear()
    for album in albums:
        content_dictionary = {'album_id':'','album_name':'','album_img':'','artist_name':'','artist_id':'','year':''}
        # print "Adding album: " + album.getAlbumString()
        content_dictionary['album_name'] = album.getAlbumString()
        content_dictionary['album_id'] = album.getAlbumName()
        content_dictionary['album_img'] = album.getAlbumImage()
        # print "Artist name: " + album.getAlbumArtist()
        artist_name = album.getAlbumArtist()
        # print "CREATING ARTIST OBJECT FROM " + artist_name
        artist_object = data.getArtist(artist_name)
        # print "Artist string: " + artist_object.getArtistString()
        content_dictionary['artist_name'] = artist_object.getArtistString()
        content_dictionary['artist_id'] = artist_object.getArtistName()
        content_dictionary['year'] = year
        content_list.append(content_dictionary)

    return content_list

def getSearchResults(search_string):

    data_source = DataSource.DataSource()
    album_objects= data_source.getAllAlbumsFromDatabase()
    artist_objects=data_source.getAllArtistsFromDatabase()
    album_names = []
    artist_names = []
    for album in album_objects:
        album_names.append(album.getAlbumString())
    for artist in artist_objects:
        artist_names.append(artist.getArtistString())

    artist_results=[]
    album_results=[]
    if " " not in search_string:
        for x in len(album_names):
            if search_string in album_names[x]:
                album_results.append(album_objects[x])
        for x in len(artist_names):
            if search_string in artist_names[x]:
                artist_results.append(artist_objects[x])

    if " " in search_string:
        word_list = search_string.split(" ")
        for word in word_list:
            for x in len(album_names):
                if word in album_names[x]:
                    album_results.append(album_objects[x])
            for x in len(artist_names):
                if word in artist_names[x]:
                    artist_results.append(artist_objects[x])
    artist_results = list(set(artist_results))
    album_results = list(set(album_results))
    
    total_results= [artist_results,album_results]
    return total_results

def cleanDescription(description):
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

def main():
    year_content = getYearContent(2012)
    for dictionary in year_content:
        for key, value in dictionary.iteritems():
            print "['%s','%s']" % (str(key),str(value))

    artist_content = getArtistContent("Isaiah Rashad")
    for dictionary in artist_content:
        for key, value in dictionary.iteritems():
            print "['%s','%s']" % (str(key),str(value))

    album_content = getAlbumContent("My Name Is My Name")
    for key, value in album_content.iteritems():
        print "['%s','%s']" % (str(key),str(value))

# if __name__ == "__main__":
#     main()