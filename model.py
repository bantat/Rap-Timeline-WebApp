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
        page_content += view.buildHeaderPage()
        page_content += view.buildYearPage(year)
        page_content += view.buildFooterPage()
    elif parameters['artist'] != '':
        artist = parameters['artist']
        page_content += view.buildHeaderPage()
        page_content += view.buildArtistPage(getArtistContent(artist))
        page_content += view.buildFooterPage()
    elif parameters['album'] != '':
        album = parameters['album']
        page_content += view.buildHeaderPage()
        page_content += view.buildAlbumPage(getAlbumContent(album))
        page_content += view.buildFooterPage()
    else:
        page_content += view.buildHeaderPage()
        page_content += view.buildTimelinePage(data_source.getYearsOnTimeline())
        page_content += view.buildFooterPage()

    return page_content


def getAlbumContent(album_name):
    """This method takes an album name string as an argument, and builds a dictionary of strings containing content to
    be used in creating the album page."""

    data = DataSource.DataSource()

    album_object = data.getAlbum(album_name)
    content_dictionary = {'album':'','summary':'','image':'','year':'','artist_id':'','artist_name':''}
    content_dictionary['album'] = album_object.getAlbumString()
    content_dictionary['summary'] = album_object.getAlbumDescription()
    content_dictionary['image'] = album_object.getAlbumImage()
    content_dictionary['year'] = album_object.getAlbumYear()
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
    artist_dictionary['summary'] = artist_object.getArtistDescription()
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
        content_dictionary = {'album_id':'','album_name':'','artist':'','year':''}
        # print "Adding album: " + album.getAlbumString()
        content_dictionary['album_name'] = album.getAlbumString()
        content_dictionary['album_id'] = album.getAlbumName()
        # print "Artist name: " + album.getAlbumArtist()
        artist_name = album.getAlbumArtist()
        # print "CREATING ARTIST OBJECT FROM " + artist_name
        artist_object = data.getArtist(artist_name)
        # print "Artist string: " + artist_object.getArtistString()
        content_dictionary['artist'] = artist_object.getArtistString()
        content_dictionary['year'] = year
        content_list.append(content_dictionary)

    return content_list

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