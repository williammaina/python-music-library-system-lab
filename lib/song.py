class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.add_to_genre_count(self)
        Song.add_to_artists_count(self)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, song):
        if song.genre not in cls.genres:
            cls.genres.append(song.genre)

    @classmethod
    def add_to_artists(cls, song):
        if song.artist not in cls.artists:
            cls.artists.append(song.artist)

    @classmethod
    def add_to_genre_count(cls, song):
        cls.genre_count[song.genre] = cls.genre_count.get(song.genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, song):
        cls.artists_count[song.artist] = cls.artists_count.get(song.artist, 0) + 1