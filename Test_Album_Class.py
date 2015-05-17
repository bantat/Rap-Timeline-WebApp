import unittest
from unittest import TestCase
import DataSource

__author__ = 'Tore Banta & Charlie Sarano'


class TestAlbum(TestCase):
    def test_getAlbumName(self):
        album_object = DataSource.Album('Yeezus (album)',"Kanye's greatest accomplishment.",'yeezus.jpg',2013,
                                        'Kanye West','NONE')
        TestCase.assertEqual(self,album_object.getAlbumName(),'Yeezus (album)', "Album name does not match string "
                                                                                "returned by getAlbumName")

    def test_getAlbumString(self):
        album_object = DataSource.Album('Yeezus (album)',"Kanye's greatest accomplishment.",'yeezus.jpg',2013,
                                        'Kanye West','NONE')
        TestCase.assertEqual(self,album_object.getAlbumString(),'Yeezus', "Album string representation does not match "
                                                                          "string returned by getAlbumName")

    def test_getAlbumDescription(self):
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
        album_object = DataSource.Album('Yeezus (album)',"Kanye's greatest accomplishment.",'yeezus.jpg',2013,
                                        'Kanye West','NONE')
        TestCase.assertEqual(self,album_object.getAlbumYear(),2013, "Year value does not match int returned by "
                                                                    "getAlbumName")

    def test_getAlbumImage(self):
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