
"""Test module for the Album class and methods. IMPORTANT: Test module does not function unless DataSource.py is
modified to include a hardcoded PASSWORD variable in the constructor.
"""

__author__ = 'Tore Banta, Charlie Sarano'

import unittest
from unittest import TestCase
import DataSource


class TestAlbum(TestCase):
    def test_getAlbumName(self):
        """Tests the method getAlbumName() of the Album class. Test fails if album name used in constructor does not
        match string returned by method."""

        album_object = DataSource.Album('Yeezus (album)',"Kanye's greatest accomplishment.",'yeezus.jpg',2013,
                                        'Kanye West','NONE')
        TestCase.assertEqual(self,album_object.getAlbumName(),'Yeezus (album)', "Album name does not match string "
                                                                                "returned by getAlbumName")

    def test_getAlbumString(self):
        """Tests the method getAlbumString() of the Album class. Test fails if album string returned by method is
        improperly formatted."""

        album_object = DataSource.Album('Yeezus (album)',"Kanye's greatest accomplishment.",'yeezus.jpg',2013,
                                        'Kanye West','NONE')
        TestCase.assertEqual(self,album_object.getAlbumString(),'Yeezus', "Album string representation does not match "
                                                                          "string returned by getAlbumName")

    def test_getAlbumDescription(self):
        """Tests the method getAlbumDescription() of the Album class. Test fails if album description used in
        constructor does not match string returned by method."""

        album_object = DataSource.Album('Yeezus (album)',"Kanye's greatest accomplishment.",'yeezus.jpg',2013,
                                        'Kanye West','NONE')
        TestCase.assertEqual(self,album_object.getAlbumDescription(),"Kanye's greatest accomplishment.", "Album "
                                                                                                         "description "
                                                                                                         "does not "
                                                                                                         "match string"
                                                                                                         " returned by"
                                                                                                         " getAlbumDes"
                                                                                                         "cription")

    def test_getAlbumYear(self):
        """Tests the method getAlbumYear() of the Album class. Test fails if album release year integer used in
        constructor does not match integer returned by method."""

        album_object = DataSource.Album('Yeezus (album)',"Kanye's greatest accomplishment.",'yeezus.jpg',2013,
                                        'Kanye West','NONE')
        TestCase.assertEqual(self,album_object.getAlbumYear(),2013, "Year value does not match int returned by "
                                                                    "getAlbumName")

    def test_getAlbumImage(self):
        """Tests the method getAlbumImage() of the Album class. Test fails if image link used in constructor does not
        match string returned by method."""

        album_object = DataSource.Album('Yeezus (album)',"Kanye's greatest accomplishment.",'yeezus.jpg','2013',
                                        'Kanye West','NONE')
        TestCase.assertEqual(self,album_object.getAlbumImage(),'yeezus.jpg', "Album image string does not match string"
                                                                             " returned by getAlbumImage")

    def test_getAlbumArtist(self):
        album_object = DataSource.Album('Yeezus (album)',"Kanye's greatest accomplishment.",'yeezus.jpg','2013',
                                        'Kanye West','NONE')
        TestCase.assertEqual(self,album_object.getAlbumArtist(),'Kanye West', "Artist string does not match string"
                                                                              " returned by getAlbumArtist")

if __name__ == '__main__':
    unittest.main()