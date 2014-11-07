import unittest
from playlist import Playlist
from song import Song


class PlaylistTest(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Title1", "Artist1", "Album1", 2, 192, 128)
        self.song2 = Song("Title2", "Artist2", "Album2", 2, 183, 1024)
        self.playlist = Playlist("PlaylistTitle")
        self.playlist.songs.append(self.song1)
        self.playlist.songs.append(self.song2)

    def test_init(self):
        self.assertEqual(self.playlist.name, "PlaylistTitle")
        self.assertEqual(self.playlist.songs, [self.song1, self.song2])

    def test_add_song(self):
        self.song3 = Song("Title3", "Artist3", "Album3", 2, 201, 128)
        self.playlist.add_song(self.song3)
        self.assertEqual(
            self.playlist.songs, [self.song1, self.song2, self.song3])

    def test_remove_song(self):
        self.song3 = Song("Title3", "Artist3", "Album3", 4, 194, 1024)
        self.playlist.add_song(self.song3)
        self.playlist.remove_song("Title3")
        self.assertEqual(self.playlist.songs, [self.song1, self.song2])

    def test_total_length(self):
        self.assertEqual(self.playlist.total_length(), 375)

    def test_remove_disrated(self):
        self.song3 = Song("Title3", "Artist3", "Album3", 4, 206, 1024)
        self.playlist.add_song(self.song3)
        self.playlist.remove_disrated(3)
        self.assertEqual(self.playlist.songs, [self.song3])

    def test_remove_bad_quality(self):
        self.song3 = Song("Title3", "Artist3", "Album3", 4, 206, 1024)
        self.playlist.add_song(self.song3)
        self.playlist.remove_bad_quality(1000)
        self.assertEqual(self.playlist.songs, [self.song2, self.song3])

    def test_show_artists(self):
        self.song3 = Song("Title3", "Artist2", "Album3", 4, 206, 1024)
        self.playlist.add_song(self.song3)
        self.assertEqual(self.playlist.show_artists(), ["Artist1", "Artist2"])

    # def test_str(self):
    #     test = self.playlist.str()
    #     self.assertEqual(
    #         "Artist1 Title1 - 3:12\nArtist2 Title2 - 3:03\n", test)

    def test_save(self):
        self.playlist.save("pesho.txt")

    def test_load(self):
        self.playlist.load("pesho.txt")
if __name__ == '__main__':
    unittest.main()
