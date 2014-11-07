import json
from song import Song


class Playlist(object):

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, newSong):
        self.songs.append(newSong)

    def remove_song(self, song_name):
        buff = []
        for i in self.songs:
            if i.title != song_name:
                buff.append(i)
        self.songs = []
        self.songs = buff

    def total_length(self):
        sum = 0
        for i in self.songs:
            sum += i.length
        return sum

    def remove_disrated(self, rating):
        if rating > 5 or rating < 0:
            raise ValueError
        else:
            buff = []
            for i in self.songs:
                if i.rating >= rating:
                    buff.append(i)
            self.songs = []
            self.songs = buff

    def remove_bad_quality(self, minBitRate):
        buff = []
        for i in self.songs:
            if i.bitrate >= minBitRate:
                buff.append(i)
        self.songs = []
        self.songs = buff

    def show_artists(self):
        artists = []
        for i in self.songs:
            if i.artist not in artists:
                artists.append(i.artist)
        return artists

    def __str__(self):
        info = ""
        for i in self.songs:
            minute = i.length // 60
            second = i.length % 60
            if second < 10:
                info += "{} {} - {}:0{}\n".format(i.artist,
                                                  i.title, minute, second)
            else:
                info += "{} {} - {}:{}\n".format(i.artist,
                                                 i.title, minute, second)

        return info

    def save(self, filename):
        save_data = {'name': self.name, 'songs': []}
        for song in self.songs:
            save_data['songs'].append(song.__dict__)
        file = open(filename, "w")
        file.write(json.dumps(save_data))
        file.close()

    def load(self, filename):
        with open(filename, 'r') as load_file:
            load_data = json.load(load_file)
            loaded_playlist = Playlist(load_data['name'])
            for song_data in load_data['songs']:
                song = Song(song_data['title'], song_data['artist'], song_data['album'], song_data['rating'], song_data['length'], song_data['bitrate'])
                loaded_playlist.add_song(song)
        return loaded_playlist

song1 = Song("Title1", "Artist1", "Album1", 2, 192, 128)
song2 = Song("Title2", "Artist2", "Album2", 2, 183, 1024)
playlist = Playlist("PlaylistTitle")
playlist.songs.append(song1)
playlist.songs.append(song2)
print (playlist.load("pesho.txt"))