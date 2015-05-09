import psycopg2
import os.path
import sys

class DataSource:
    def __init__(self):
        #f = open(os.path.join('/cs257', 'bantat'))
    	PASSWORD = "mike494java"      #f.read().strip()
        #f.close()
        db_connection = psycopg2.connect(user = 'bantat',database ='bantat',password=PASSWORD)
        self.cursor = db_connection.cursor()

    def getArtist(self, artist_name):
        self.cursor.execute("SELECT * FROM artists WHERE name = %s;",(artist_name,))
        info = list(self.cursor.fetchone())

        albums = []
        self.cursor.execute("SELECT name FROM albums WHERE artist = %s;",(artist_name,))
        for object in self.cursor:
            albums.append(object[0])

        print "Albums: " + albums

        artist_object = Artist(info[0],info[1],info[2],albums)

        return artist_object

    def getAlbum(self, album_name):
        self.cursor.execute("SELECT * FROM albums WHERE name = %s;",(album_name,))

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
        albums = []

        for row in self.cursor:
            albums.append(row[0])
        timeline_object = Timeline(year, albums)

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

    def getArtistDescription(self):
        return self.artist_description

    def getArtistImage(self):
        return self.artist_image

    def getArtistAlbums(self):
        albums_by_artist = []

        for album_name in self.artist_albums:
            album_object = getAlbum(album_name)
            albums_by_artist.append(album_object)

        return albums_by_artist

class Timeline:
    def __init__(self, year, albums):
        self.year = year
        self.albums = albums

    def getYear(self):
        return self.year

    def getAlbumsForYear(self):

        albums_for_year = []

        for album_name in self.albums:
            album_object = getAlbum(album_name)
            albums_for_year.append(album_object)

        return albums_for_year

def main():
    data = DataSource()
    album = data.getAlbum("Good Kid, M.A.A.D City")
    artist = data.getArtist("The Notorious B.I.G.")

    print "Album: " + album.getAlbumName()
    print "Year:"
    print album.getAlbumYear()
    # print "Artist: " + album.getAlbumArtist()
    # print "Summary: " + album.getAlbumDescription()
    # print "Image: " + album.getAlbumImage()
    #
    # print "Artist: " + artist.getArtistName()
    # print "Summary: " + artist.getArtistDescription()
    # print "Image: " + artist.getArtistImage()
    print "Albums: "
    for album in artist.getArtistAlbums():
        print album.getAlbumName()

main()