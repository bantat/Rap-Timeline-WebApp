#/usr/bin/python

"""A module used for accessing information stored in the SQL database. The module contains classes for Album, Artist,
and Timeline objects. The module also contains a core class DataSource which is used to establish a connection to the
database, and retrieve the necessary information to construct each of the other classes.

By Tore Banta & Charlie Sarano
CS 257 - Software Design (Jadrian Miles)
Carleton College
"""

__author__ = 'Tore Banta, Charlie Sarano'

import psycopg2
import os.path
import sys


class DataSource:
    """Class for connecting to and accessing information from the database."""

    def __init__(self):
        """Constructor takes no arguments, and stores a database connection cursor object as an instance variable."""

        USERNAME = 'bantat'
        DB_NAME = 'bantat'
        PASSWORD = 'mike494java'

        db_connection = None
        self.cursor = None

        # Attempts to read the database password from a file stored on the server, and assign to variable PASSWORD
        # try:
        #     f = open(os.path.join('/cs257', USERNAME))
        #     PASSWORD = f.read().strip()
        #     f.close()
        # except:
        #     print "Password failed"

        # Attempts to establish a database connection using password string variable read from file on the server
        try:
            db_connection = psycopg2.connect(user=USERNAME,
                                     database=DB_NAME,
                                     password=PASSWORD)
        except:
            sys.exit()

        # Attempts to create a cursor object using the database connection
        try:
            self.cursor = db_connection.cursor()
        except:
            sys.exit()

    def getArtist(self, artist_name):
        """Takes an artist name string as an argument, and returns an artist object containing all data about that
        artist."""

        # Sets the select statement for the artist we want
        sql_string = self.cursor.mogrify("SELECT * FROM artists WHERE name = %s;",(artist_name,))
        self.cursor.execute(sql_string)
        # Cursor should return one item with the name, description, and image path for the artist
        info = list(self.cursor.fetchone())

        # Makes a list of items that has the names of the albums, and then constructs an album object for each album
        album_names = []
        sql_string1 = self.cursor.mogrify("SELECT name FROM albums WHERE artist = %s;",(artist_name,))
        self.cursor.execute(sql_string1)
        for item in self.cursor:
            album_names.append(item[0])

        album_objects = []

        for album in album_names:
            album_object = self.getAlbum(album)
            album_objects.append(album_object)

        # Creates an object of the artist class, and then returns it
        artist_objects = Artist(info[0],info[1],info[2],album_objects)

        return artist_objects

    def getAllArtistsFromDatabase(self):
        """Returns a list of Artist objects for all artists stored in the database."""

        self.cursor.execute("SELECT * FROM artists;")
        info = list(self.cursor.fetchall())

        artists = []

        for x in range(len(info)):
            artist_object = self.getArtist(info[x][0])
            artists.append(artist_object)

        return artists

    def getAlbum(self, album_name):
        """Takes an album name string as an argument, and returns an album object containing all data about that
        album."""

        # Selects the one album in the database that should have the same name.
        sql_string = self.cursor.mogrify("SELECT * FROM albums WHERE name = %s;",(album_name,))
        self.cursor.execute(sql_string)
        # Converts the database information into a list
        album_info = list(self.cursor.fetchone())
        # Creates an object of the album class, and returns it
        album_object = Album(album_info[0],album_info[1],album_info[2],album_info[3],album_info[4],album_info[5])

        return album_object

    def getAllAlbumsFromDatabase(self):
        """Returns a list of Album objects for all albums stored in the database."""

        self.cursor.execute("SELECT * FROM albums;")
        info = list(self.cursor.fetchall())

        albums = []

        for x in range(len(info)):
            album_object = self.getAlbum(info[x][0])
            albums.append(album_object)

        return albums

    def getYearsOnTimeline(self):
        """Returns a list of integers indicating which years have information in the database."""

        # Selects every year in the database
        self.cursor.execute("SELECT year FROM albums")
        years = []

        # Selects the integers from the tuples in the cursor
        for row in self.cursor:
            years.append(int(row[0]))
        # Turns the list into a set to eliminate doubles, and then reverses the order because we want to start
        # In the year we are in.
        years = list(set(years))
        years = reversed(years)

        return years

    def getYear(self, year):
        """Takes an integer year value as an argument, and returns a year object containing album objects for each of
        the albums which were released during that year."""

        # Selects the name of the albums with the year that is passed, and places them in album_names
        self.cursor.execute("SELECT name FROM albums WHERE year= %s;",(year,))
        album_names = []

        for item in self.cursor:
            album_names.append(item[0])

        album_objects = []
        # Turns each album name into an album object
        for album in album_names:
            album_object = self.getAlbum(album)
            album_objects.append(album_object)
        # Creates a timeline object, and returns it
        timeline_object = Timeline(year, album_objects)

        return timeline_object


class Album:
    """Class for storing and retrieving information about a particular album within the database."""

    def __init__(self, album_name, album_description, album_image, album_year, album_artist, album_spotify):
        """Constructor takes arguments for the album name (Wiki article title), description, image link, release year,
         artist, and Spotify URL."""

        self.album_name = album_name
        self.album_description = album_description
        self.album_year = album_year
        self.album_image = album_image
        self.album_artist = album_artist
        self.album_spotify = album_spotify

    def getAlbumName(self):
        """Returns the album name string, which is stored as the Wikipedia article title."""

        return self.album_name

    def getAlbumString(self):
        """Returns the album name (Wikipedia article title) stripped of additional identifying information, so that it
         is a human readable string. EX: 2001 (Dr. Dre album) is returned as 2001."""

        album_string = self.album_name

        for i in range(len(self.album_name)):
            if (self.album_name[i] == '('):
                album_string = self.album_name[:i].strip()

        return album_string

    def getAlbumDescription(self):
        """Returns the album description."""

        return self.album_description

    def getAlbumYear(self):
        """Returns the album release year."""

        return self.album_year

    def getAlbumImage(self):
        """Returns the album image link."""

        return self.album_image

    def getAlbumArtist(self):
        """Returns the album artist's name as a string (Wikipedia article title)."""

        return self.album_artist

    def getAlbumSpotify(self):
        """Returns the album's Spotify URL."""

        return self.album_spotify


class Artist:
    """Class for storing and retrieving information about a particular artist within the database."""

    def __init__(self, artist_name, artist_description, artist_image, artist_albums):
        """Constructor takes arguments for the artist name (Wiki article title), description, image link, and a list of
        album objects for each album in the database by the artist."""

        self.artist_name = artist_name
        self.artist_description = artist_description
        self.artist_image = artist_image
        self.artist_albums = artist_albums

    def getArtistName(self):
        """Returns the artist name string, which is stored as the Wikipedia article title."""

        return self.artist_name

    def getArtistString(self):
        """Returns the artist name (Wikipedia article title) stripped of additional identifying information, so that it
         is a human readable string. EX: Common (rapper) is returned as Common."""

        artist_string = self.artist_name

        for i in range(len(self.artist_name)):
            if (self.artist_name[i] == '('):
                artist_string = self.artist_name[:i].strip()

        return artist_string

    def getArtistDescription(self):
        """Returns the artist description."""

        return self.artist_description

    def getArtistImage(self):
        """Returns the artist image link."""

        return self.artist_image

    def getArtistAlbums(self):
        """Returns a list of album objects for each album in the database by the artist."""

        return self.artist_albums


class Timeline:
    """Class for storing and retrieving information about a particular year within the database."""

    def __init__(self, year, albums):
        """Constructor takes arguments for the integer value of the year, and a list of album objects for albums which
         were released during the year."""

        self.year = year
        self.albums = albums

    def getYear(self):
        """Returns the integer year value."""

        return self.year

    def getAlbumsForYear(self):
        """Returns a list of album objects for albums which were released during the year."""

        return self.albums