#/usr/bin/python

__author__ = 'Tore Banta & Charlie Sarano'

import psycopg2
import os.path
import sys


class DataSource:

    # TODO(Grader) We were unable to access our password for this phase of the project
    def __init__(self):
        USERNAME = 'bantat'
        DB_NAME = 'bantat'
        PASSWORD = 'mike494java'

        db_connection = None
        self.cursor = None

        # try:
        #     f = open(os.path.join('/cs257', USERNAME))
        #     PASSWORD = f.read().strip()
        #     f.close()
        # except:
        #     print "Password failed"

        try:
            db_connection = psycopg2.connect(user=USERNAME,
                                     database=DB_NAME,
                                     password=PASSWORD)
        except:
            print "Could not connect"

        try:
            self.cursor = db_connection.cursor()
        except:
            print "Could not get cursor"



    # TODO(Tore) Check cursor returns something
    def getArtist(self, artist_name):
        """Takes an artist name string as an argument, and returns an artist object containing all data about that
        artist."""

        # Sets the select statement for the artist we want
        sql_string = self.cursor.mogrify("SELECT * FROM artists WHERE name = %s;",(artist_name,))
        self.cursor.execute(sql_string)
        # The list should only be one item with the name, description, and image path as 0, 1, and 2 respectively
        info = list(self.cursor.fetchone())

        # This makes a list of items that has the names of the albums, and then makes album object for each album
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

        self.cursor.execute("SELECT * FROM albums;")
        info = list(self.cursor.fetchall())

        albums = []

        for x in range(len(info)):
            album_object = self.getAlbum(info[x][0])
            albums.append(album_object)

        return albums

    def getYearsOnTimeline(self):
        """Returns a list of integer year values for which there exists data."""

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
        """Takes an integer year value as an argument, and returns a year object containing album objects for albums
        which were released during that year."""

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
    """This class serves as the class that allows other modules to access information particular to one 
    album."""

    # Constructs an album with the following information
    def __init__(self, album_name, album_description, album_image, album_year, album_artist, album_spotify):
        self.album_name = album_name
        self.album_description = album_description
        self.album_year = album_year
        self.album_image = album_image
        self.album_artist = album_artist
        self.album_spotify = album_spotify


    def getAlbumName(self):
        return self.album_name


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

    def getAlbumSpoify(self):
        return self.album_spotify


class Artist:
    """This class serves as the class that will allow other modules to access information particular to one 
    artist."""

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
    """This class serves to build a timeline based on one year. This stores the album objects for that particular
    year."""

    def __init__(self, year, albums):
        self.year = year
        self.albums = albums

    def getYear(self):
        return self.year

    def getAlbumsForYear(self):
        return self.albums


def main():
    data = DataSource()
    artists = data.getAllArtistsFromDatabase()
    for artist_object in artists:
        print artist_object.getArtistName()
    albums = data.getAllAlbumsFromDatabase()
    for album_object in albums:
        print album_object.getAlbumName()

if __name__ == '__main__':
    main()