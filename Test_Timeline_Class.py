from unittest import TestCase
import unittest
import DataSource

__author__ = 'Tore Banta & Charlie Sarano'


class TestTimeline(TestCase):

    def test_getYear(self):
        data = DataSource.DataSource()
        year_object = data.getYear(1994)
        TestCase.assertEqual(self,year_object.getYear(),1994,"Year value does not equal getYear return value")


    def test_getAlbumsForYear(self):
        data = DataSource.DataSource()
        year_object = data.getYear(1994)
        album_object = year_object.getAlbumsForYear()[0]
        album_str = album_object.getAlbumName()
        l = ['Illmatic','Ready to Die','Doggystyle','Southernplayalisticadillacmuzik']
        TestCase.assertEqual(self,album_str,l[0],"Album string does not equal getAlbumsForYear return string")

if __name__ == '__main__':
    unittest.main()