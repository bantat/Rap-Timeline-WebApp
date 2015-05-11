import unittest
from unittest import TestCase
import DataSource

__author__ = 'Tore Banta & Charlie Sarano'


class TestDataSource(TestCase):
    def test_getArtist(self):
        data = DataSource.DataSource()
        artist = data.getArtist("Kanye West")
        image = artist.getArtistImage()
        TestCase.assertEqual(image,'http://upload.wikimedia.org/wikipedia/commons/c/cd/'
                                         'Kanye_West_Lollapalooza_Chile_2011_2.jpg',"Image path string does not match "
                                                                                    "string returned by getArtistImage")

    def test_getAlbum(self):
        data = DataSource.DataSource()
        album = data.getAlbum("Yeezus")
        image = album.getAlbumImage()
        TestCase.assertEqual(image,'http://upload.wikimedia.org/wikipedia/en/8/83/Yeezus_Kanye_West.jpg',
                             "Image path string does not match string returned by getArtistImage")

    def test_getYearsOnTimeline(self):
        data = DataSource.DataSource()
        years = [2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,1999,1998,1997,1996,
                 1995,1994,1993,1992,1991,1990,1988]
        TestCase.assertEqual(data.getYearsOnTimeline(),years,"Year list does not match list returned by "
                                                             "getYearsOnTimeline")

    def test_getYear(self):
        data = DataSource.DataSource()
        year = data.getYear(2015)
        albums = ['To Pimp a Butterfly','B4.Da.$$','Tetsuo & Youth']
        TestCase.assertEqual(year.getAlbumsForYear(),albums,"Albums list does not match list returned by "
                                                            "getAlbumsForYear")

if __name__ == '__main__':
    unittest.main()