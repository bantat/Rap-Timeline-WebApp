import unittest
from unittest import TestCase
import DataSource

__author__ = 'Tore Banta & Charlie Sarano'


class TestDataSource(TestCase):
    def test_getArtist(self):
        data = DataSource.DataSource()
        artist = data.getArtist("Kanye West")
        image = artist.getArtistImage()
        TestCase.assertEqual(self, image,'http://upload.wikimedia.org/wikipedia/commons/c/cd/'
                                         'Kanye_West_Lollapalooza_Chile_2011_2.jpg',"Image path string does not match "
                                                                                    "string returned by getArtistImage")

    def test_getAlbum(self):
        data = DataSource.DataSource()
        album = data.getAlbum("Yeezus")
        image = album.getAlbumImage()
        TestCase.assertEqual(self, image,'http://upload.wikimedia.org/wikipedia/en/8/83/Yeezus_Kanye_West.jpg',
                             "Image path string does not match string returned by getArtistImage")

    def verifyDatabaseConnections(self):
        data = DataSource.DataSource()
        albums = data.getAllAlbumsFromDatabase()
        for album in albums:
            album_name = album.getAlbumName()
            artist_name = album.getAlbumArtist()
            try:
                data.getArtist(artist_name)
            except:
                error_message = "Database inter-table connection failed, " \
                                "check artist: %s for album: %s" % (artist_name, album_name)
                self.fail(error_message)

    def verifyDatabaseAlbums(self):
        data = DataSource.DataSource()
        albums = data.getAllAlbumsFromDatabase()
        for album in albums:
            error_description = "Missing album description for %s" % (album.getAlbumName())
            error_description2 = "Invalid album description for %s" % (album.getAlbumName())
            error_image = "Missing album image for %s" % (album.getAlbumName())
            TestCase.assertTrue(self, len(album.getAlbumDescription()) > 0, error_description)
            TestCase.assertTrue(self, len(album.getAlbumImage()) > 0, error_image)
            TestCase.assertFalse(self, '}' in album.getAlbumDescription(), error_description2)
            TestCase.assertFalse(self, '{' in album.getAlbumDescription(), error_description2)

    def verifyDatabaseArtists(self):
        data = DataSource.DataSource()
        artists = data.getAllArtistsFromDatabase()
        for artist in artists:
            error_description = "Missing artist description for %s" % (artist.getArtistName())
            error_description2 = "Invalid artist description for %s" % (artist.getArtistName())
            error_image = "Missing artist image for %s" % (artist.getArtistName())
            TestCase.assertTrue(self, len(artist.getArtistDescription()) > 0, error_description)
            TestCase.assertTrue(self, len(artist.getArtistImage()) > 0, error_image)
            TestCase.assertFalse(self, '}' in artist.getArtistDescription(), error_description2)
            TestCase.assertFalse(self, '{' in artist.getArtistDescription(), error_description2)

if __name__ == '__main__':
    unittest.main()
    TestDataSource.verifyDatabaseConnections()
    TestDataSource.verifyDatabaseAlbums()
    TestDataSource.verifyDatabaseArtists()