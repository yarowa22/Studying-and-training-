class Song:
    def __init__(self, title, artist, duration_seconds):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds
    def show_details(self):
        return f"Song Title : {self.title}, Self Artist : {self.artist}, Duration : {self.duration_seconds}, Song : {self.song_object}"
class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        
        self.songs = []
    def add_song(self, song_object):
        self.songs.append(song_object)
    def list_of_songs(self):
        for song in self.songs:
            print(song.show_details())
    def remove_song(self, title):
        for song in self.songs:
            if song.title == title:
                self.songs.remove(song)


    