class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment count
        Song.add_song_to_count()

        # Add genre to genres list
        Song.add_to_genres(genre)

        # Add artist to artists list
        Song.add_to_artists(artist)

        # Update genre count
        Song.add_to_genre_count(genre)

        # Update artist count
        Song.add_to_artist_count(artist)
