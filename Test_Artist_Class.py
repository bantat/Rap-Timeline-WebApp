from unittest import TestCase
import unittest
import DataSource

__author__ = 'Tore Banta & Charlie Sarano'


class TestArtist(TestCase):
    def test_getArtistName(self):
        albums_list = ['MMLP2']
        artist_object = DataSource.Artist('Eminem (rapper)','Eminem is a talented rapper from Chicago.',
                                          'eminem.jpg', albums_list)
        TestCase.assertEqual(self,artist_object.getArtistName(),'Eminem (rapper)', "Name used in constructor does not "
                                                                              "match return string from "
                                                                              "getArtistName")

    def test_getArtistString(self):
        albums_list = ['MMLP2']
        artist_object = DataSource.Artist('Eminem (rapper)','Eminem is a talented rapper from Chicago.',
                                          'eminem.jpg', albums_list)
        TestCase.assertEqual(self,artist_object.getArtistString(),'Eminem', "String representation returned by "
                                                                       "getArtistString incorrectly formatted")

    def test_getArtistDescription(self):
        albums_list = ['MMLP2']
        artist_object = DataSource.Artist('Eminem (rapper)','Eminem is a talented rapper from Chicago.',
                                          'eminem.jpg', albums_list)
        TestCase.assertEqual(self,artist_object.getArtistDescription(),'Eminem is a talented rapper from Chicago.',
                             "String description returned by getArtistDescription incorrect")

    def test_getArtistImage(self):
        albums_list = ['MMLP2']
        artist_object = DataSource.Artist('Eminem (rapper)','Eminem is a talented rapper from Chicago.',
                                          'eminem.jpg', albums_list)
        TestCase.assertEqual(self,artist_object.getArtistImage(),'eminem.jpg',
                             "String image path returned by getArtistImage incorrect")

    def test_getArtistAlbums(self):
        albums_list = ['MMLP2']
        artist_object = DataSource.Artist('Eminem (rapper)','Eminem is a talented rapper from Chicago.',
                                          'eminem.jpg', albums_list)
        TestCase.assertEqual(self,artist_object.getArtistAlbums()[0],'MMLP2',
                             "String album returned by getArtistAlbums incorrect")

if __name__ == '__main__':
    unittest.main()