#/usr/bin/python

__author__ = 'Tore Banta & Charlie Sarano'

import psycopg2
import os.path
import sys


class DataSource:

    # TODO(Tore) Add try catch blocks
    def __init__(self):
        USERNAME = 'bantat'
        DB_NAME = 'bantat'

        # try:
        #     f = open(os.path.join('/cs257', USERNAME))
        #     PASSWORD = f.read().strip()
        #     f.close()
        # except:
        #     sys.exit()
        #
        # try:
        #     db_connection = psycopg2.connect(user=USERNAME,
        #                              database=DB_NAME,
        #                              password=PASSWORD)
        # except:
        #     sys.exit()
        #
        # try:
        #     cursor = db_connection.cursor()
        # except:
        #     sys.exit()

        PASSWORD = "mike494java"

        db_connection = psycopg2.connect(user=USERNAME, database=DB_NAME, password=PASSWORD)
        self.cursor = db_connection.cursor()



    # TODO(Tore) Check cursor returns something
    def getArtist(self, artist_name):
        #sets the select statement for the artist we want
        sql_string = self.cursor.mogrify("SELECT * FROM artists WHERE name = %s;",(artist_name,))
        self.cursor.execute(sql_string)
        #the list should only be one item with the name, description, and image path as 0, 1, and 2 respectively
        info = list(self.cursor.fetchone())

        #this makes a list of items that has the names of the albums, and then makes album object for each album
        album_names = []
        sql_string1=self.cursor.mogrify("SELECT name FROM albums WHERE artist = %s;",(artist_name,))
        self.cursor.execute(sql_string1)
        for item in self.cursor:
            album_names.append(item[0])

        album_objects = []

        for album in album_names:
            album_object = self.getAlbum(album)
            album_objects.append(album_object)

        #creates an object of the artist class, and then returns it
        artist_objects = Artist(info[0],info[1],info[2],album_objects)

        return artist_objects

    def getAlbum(self, album_name):
        #selects the one album in the database that should have the same name.
        sql_string = self.cursor.mogrify("SELECT * FROM albums WHERE name = %s;",(album_name,))
        self.cursor.execute(sql_string)
        #converts the database information into a list
        album_info = list(self.cursor.fetchone())
        #creates an object of the album class, and returns it
        album_object = Album(album_info[0],album_info[1],album_info[2],album_info[3],album_info[4])

        return album_object

    def getYearsOnTimeline(self):
        #selects every year in the database
        self.cursor.execute("SELECT year FROM albums")
        years = []

        #selects the integers from the tuples in the cursor
        for row in self.cursor:
            years.append(int(row[0]))
        #turns the list into a set to eliminate doubles, and then reverses the order because we want to start 
        #in the year we are in.
        years = list(set(years))
        years = reversed(years)

        return years

    def getYear(self, year):
        #selects the name of the albums with the year that is passed, and places them in album_names
        self.cursor.execute("SELECT name FROM albums WHERE year= %s;",(year,))
        album_names = []

        for item in self.cursor:
            album_names.append(item[0])

        album_objects = []
        #turns each album name into an album object
        for album in album_names:
            album_object = self.getAlbum(album)
            album_objects.append(album_object)
        #creates a timeline object, and returns it
        timeline_object = Timeline(year, album_objects)

        return timeline_object


class Album:
    """This class serves as the class that allows other modules to access information particular to one 
    album
    """
    #constructs an album with the following information
    def __init__(self, album_name, album_description, album_image, album_year, album_artist):
        self.album_name = album_name
        self.album_description = album_description
        self.album_year = album_year
        self.album_image = album_image
        self.album_artist = album_artist

    #returns the name of the album on the wikipedia page
    def getAlbumName(self):
        return self.album_name

    #returns a string of the album without any qualifiers from the wikipedia
    def getAlbumString(self):
        album_string = self.album_name

        for i in range(len(self.album_name)):
            if (self.album_name[i] == '('):
                album_string = self.album_name[:i].strip()

        return album_string

    def getAlbumDescription(self):
        return self.album_description

    def getAlbumYear(self):
        return self.album_year

    def getAlbumImage(self):
        return self.album_image

    def getAlbumArtist(self):
        return self.album_artist


class Artist:
    """This class serves as the class that will allow other modules to access information particular to one 
    artist
    """
    #constructs an artist object with this information stored
    def __init__(self, artist_name, artist_description, artist_image, artist_albums):
        self.artist_name = artist_name
        self.artist_description = artist_description
        self.artist_image = artist_image
        self.artist_albums = artist_albums
    #returns the name of the album according to the wikipedia
    def getArtistName(self):
        return self.artist_name
    #returns the name of the artist without any qualifiers from the Wikipedia
    def getArtistString(self):
        artist_string = self.artist_name

        for i in range(len(self.artist_name)):
            if (self.artist_name[i] == '('):
                artist_string = self.artist_name[:i].strip()

        return artist_string

    def getArtistDescription(self):
        return self.artist_description

    def getArtistImage(self):
        return self.artist_image

    def getArtistAlbums(self):
        return self.artist_albums


class Timeline:
    """This class serves to build a timeline based on one year. This stores the ablum objects for that particular year
    """

    def __init__(self, year, albums):
        self.year = year
        self.albums = albums

    def getYear(self):
        return self.year

    def getAlbumsForYear(self):
        return self.albums


def main():
    data = DataSource()
    album = data.getAlbum("Yeezus")
    artist = data.getArtist("Outkast")
    year = data.getYear(1994)

    for year in data.getYearsOnTimeline():
        print year
