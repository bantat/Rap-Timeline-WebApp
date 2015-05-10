import unittest
from unittest import TestCase
import DataSource

__author__ = 'Tore Banta & Charlie Sarano'


class TestAlbum(TestCase):
    def test_getAlbumName(self):
        album_object = DataSource.Album('Yeezus (album)',"Kanye's greatest accomplishment.",'yeezus.jpg','2013',
                                        'Kanye West')
        TestCase.assertEqual(self,album_object.getAlbumName(),'Yeezus (album)', "Album name does not match string "
                                                                                "returned by getAlbumName")

    def test_getAlbumString(self):
        album_object = DataSource.Album('Yeezus (album)',"Kanye's greatest accomplishment.",'yeezus.jpg','2013',
                                        'Kanye West')
        TestCase.assertEqual(self,album_object.getAlbumString(),'Yeezus', "Album string representation does not match "
                                                                          "string returned by getAlbumName")

    def test_getAlbumDescription(self):
        self.fail()

    def test_getAlbumYear(self):
        self.fail()

    def test_getAlbumImage(self):
        self.fail()

    def test_getAlbumArtist(self):
        self.fail()

if __name__ == '__main__':
    unittest.main()