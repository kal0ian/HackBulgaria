import unittest
from song import Song


class SongTest(unittest.TestCase):

    def setUp(self):
        self.song = Song("Title", "Artist", "Album", 2, 3.82, 64)

    def test_init(self):
        self.assertEqual(self.song.title, "Title")
        self.assertEqual(self.song.artist, "Artist")
        self.assertEqual(self.song.album, "Album")
        self.assertEqual(self.song.rating, 2)
        self.assertEqual(self.song.length, 3.82)
        self.assertEqual(self.song.bitrate, 64)

    def test_rate(self):
        self.song.rate(2)
        self.assertEqual(self.song.rating, 2)
        with self.assertRaises(ValueError):
            self.song.rate(self)


if __name__ == '__main__':
    unittest.main()
