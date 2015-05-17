
"""Test module for the Timeline class and methods. IMPORTANT: Test module does not function unless DataSource.py is
modified to include a hardcoded PASSWORD variable in the constructor.
"""

__author__ = 'Tore Banta, Charlie Sarano'

from unittest import TestCase
import unittest
import DataSource


class TestTimeline(TestCase):

    def test_getYear(self):
        """Tests the method getYear() of the Timeline class. Test fails if value returned by method does not match the
        value used in the constructor."""
        data = DataSource.DataSource()
        year_object = data.getYear(1994)
        TestCase.assertEqual(self, year_object.getYear(), 1994, "Year value does not equal getYear return value")

    def test_getAlbumsForYear(self):
        """Tests the method getAlbumsForYear() of the Timeline class. Test fails if the album Illmatic is not in list of
        album objects for 1994 returned by method."""
        data = DataSource.DataSource()
        year_object = data.getYear(1994)
        album_objects = year_object.getAlbumsForYear()
        album_names = []
        for album_object in album_objects:
            album_names.append(album_object.getAlbumName())
        album_string = "Illmatic"
        TestCase.assertTrue(self,album_string in album_names,"Albums for year does not contain Illmatic.")

if __name__ == '__main__':
    unittest.main()