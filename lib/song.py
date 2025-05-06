class Song:
    # Class attributes
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        """
        Initialize a Song object with name, artist, and genre
        
        Args:
            name (str): Name of the song
            artist (str): Artist of the song
            genre (str): Genre of the song
        """
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Call class methods to update class attributes
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)
    
    @classmethod
    def add_song_to_count(cls):
        """
        Increments the count of songs by 1
        """
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        """
        Adds a genre to the set of genres if it doesn't exist
        
        Args:
            genre (str): Genre to add
        """
        cls.genres.add(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        """
        Adds an artist to the set of artists if it doesn't exist
        
        Args:
            artist (str): Artist to add
        """
        cls.artists.add(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        """
        Updates the count of songs for a genre
        
        Args:
            genre (str): Genre to update count for
        """
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        """
        Updates the count of songs for an artist
        
        Args:
            artist (str): Artist to update count for
        """
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1