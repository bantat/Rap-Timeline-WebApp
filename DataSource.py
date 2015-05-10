__author__ = 'Tore Banta & Charlie Sarano'

import psycopg2
import os.path
import sys


class DataSource:

    # TODO(Tore) Add try catch blocks
    def __init__(self):
        USERNAME = 'bantat'
        DB_NAME = 'bantat'
        PASSWORD = "mike494java"

        db_connection = psycopg2.connect(user=USERNAME, database=DB_NAME, password=PASSWORD)
        self.cursor = db_connection.cursor()

        # try:
        #     f = open(os.path.join('/cs257', USERNAME))
        #     PASSWORD = f.read().strip()
        #     f.close()
        # except:
        #     print "Password read failed"
        #
        # try:
        #     db_connection = psycopg2.connect(user=USERNAME, database=DB_NAME, password=PASSWORD)
        # except:
        #     print "Connection failed"
        #
        # try:
        #     self.cursor = db_connection.cursor()
        # except:
        #     print "Cursor failed"

        # PASSWORD = "mike494java" # f.read().strip()
        # f.close()
        # db_connection = psycopg2.connect(user = 'bantat',database ='bantat',password=PASSWORD)

    # TODO(Tore) Check cursor returns something
    def getArtist(self, artist_name):
        sql_string = self.cursor.mogrify("SELECT * FROM artists WHERE name = %s;",(artist_name,))
        self.cursor.execute(sql_string)
        info = list(self.cursor.fetchone())

        album_names = []
        sql_string1=self.cursor.mogrify("SELECT name FROM albums WHERE artist = %s;",(artist_name,))
        self.cursor.execute(sql_string1)
        for item in self.cursor:
            album_names.append(item[0])

        album_objects = []

        for album in album_names:
            album_object = self.getAlbum(album)
            album_objects.append(album_object)

        artist_objects = Artist(info[0],info[1],info[2],album_objects)

        return artist_objects

    def getAlbum(self, album_name):
        sql_string = self.cursor.mogrify("SELECT * FROM albums WHERE name = %s;",(album_name,))
        self.cursor.execute(sql_string)

        album_info = list(self.cursor.fetchone())

        album_object = Album(album_info[0],album_info[1],album_info[2],album_info[3],album_info[4])

        return album_object

    def getYearsOnTimeline(self):
        self.cursor.execute("SELECT year FROM albums")
        years = []

        for row in self.cursor:
            years.append(int(row[0]))
        years = list(set(years))

        return years

    def getYear(self, year):
        self.cursor.execute("SELECT name FROM albums WHERE year= %s;",(year,))
        album_names = []

        for item in self.cursor:
            album_names.append(item[0])

        album_objects = []

        for album in album_names:
            album_object = self.getAlbum(album)
            album_objects.append(album_object)

        timeline_object = Timeline(year, album_objects)

        return timeline_object


class Album:

    def __init__(self, album_name, album_description, album_image, album_year, album_artist):
        self.album_name = album_name
        self.album_description = album_description
        self.album_year = album_year
        self.album_image = album_image
        self.album_artist = album_artist

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


class Artist:

    def __init__(self, artist_name, artist_description, artist_image, artist_albums):
        self.artist_name = artist_name
        self.artist_description = artist_description
        self.artist_image = artist_image
        self.artist_albums = artist_albums

    def getArtistName(self):
        return self.artist_name

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

    for year in data.getYearsOnTimeline:
        print year

    # print "Album: " + album.getAlbumName()
    # print "Album String: " + album.getAlbumString()
    # print "Year:"
    # print album.getAlbumYear()
    # print "Artist: " + artist.getArtistName()
    # print "Artist: " + album.getAlbumArtist()
    # print "Summary: " + album.getAlbumDescription()
    # print "Image: " + album.getAlbumImage()
    #
    # print "Artist: " + artist.getArtistName()
    # print "Summary: " + artist.getArtistDescription()
    # print "Image: " + artist.getArtistImage()
    # print "Albums: "
    # print "Getting albums for Outkast"
    # for album in artist.getArtistAlbums():
    #     print album.getAlbumName()

    # print "Getting albums for 1994"
    # for album in year.getAlbumsForYear():
    #     print album.getAlbumName()

if __name__ == '__main__':
    main()