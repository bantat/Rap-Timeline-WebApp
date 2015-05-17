
"""Test module for the Artist class and methods. IMPORTANT: Test module does not function unless DataSource.py is
modified to include a hardcoded PASSWORD variable in the constructor.
"""

__author__ = 'Tore Banta, Charlie Sarano'

from unittest import TestCase
import unittest
import DataSource


class TestArtist(TestCase):

    def test_getArtistName(self):
        """Tests the method getArtistName() of the Artist class. Test fails if artist name used in constructor does not
        match string returned by method."""

        albums_list = ['MMLP2']
        artist_object = DataSource.Artist('Eminem (rapper)','Eminem is a talented rapper from Chicago.',
                                          'eminem.jpg', albums_list)
        TestCase.assertEqual(self,artist_object.getArtistName(),'Eminem (rapper)', "Name used in constructor does not "
                                                                              "match return string from "
                                                                              "getArtistName")

    def test_getArtistString(self):
        """Tests the method getArtistString() of the Artist class. Test fails if artist string returned by method is
        improperly formatted."""

        albums_list = ['MMLP2']
        artist_object = DataSource.Artist('Eminem (rapper)','Eminem is a talented rapper from Chicago.',
                                          'eminem.jpg', albums_list)
        TestCase.assertEqual(self,artist_object.getArtistString(),'Eminem', "String representation returned by "
                                                                       "getArtistString incorrectly formatted")

    def test_getArtistDescription(self):
        """Tests the method getArtistDescription() of the Artist class. Test fails if artist description used in
        constructor does not match string returned by method."""

        albums_list = ['MMLP2']
        artist_object = DataSource.Artist('Eminem (rapper)','Eminem is a talented rapper from Chicago.',
                                          'eminem.jpg', albums_list)
        TestCase.assertEqual(self,artist_object.getArtistDescription(),'Eminem is a talented rapper from Chicago.',
                             "String description returned by getArtistDescription incorrect")

    def test_getArtistImage(self):
        """Tests the method getArtistImage() of the Artist class. Test fails if image link used in constructor does not
        match string returned by method."""

        albums_list = ['MMLP2']
        artist_object = DataSource.Artist('Eminem (rapper)','Eminem is a talented rapper from Chicago.',
                                          'eminem.jpg', albums_list)
        TestCase.assertEqual(self,artist_object.getArtistImage(),'eminem.jpg',
                             "String image path returned by getArtistImage incorrect")

    def test_getArtistAlbums(self):
        """Tests the method getArtistAlbums() of the Artist class. Test fails if list of albums returned by method does
        not match list returned by method."""

        albums_list = ['MMLP2']
        artist_object = DataSource.Artist('Eminem (rapper)','Eminem is a talented rapper from Chicago.',
                                          'eminem.jpg', albums_list)
        TestCase.assertEqual(self,artist_object.getArtistAlbums()[0],'MMLP2',
                             "String album returned by getArtistAlbums incorrect")

if __name__ == '__main__':
    unittest.main()