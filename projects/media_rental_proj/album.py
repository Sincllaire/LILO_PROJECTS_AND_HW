from media import Media

class Album(Media):
    """
    Album class with artist and songs information.
    """
    
    def __init__(self, title: str, copies_available: int, artist: str, songs: str):
        """
        Initialize an album.
        
        Args:
            title: Album title
            copies_available: Number of copies available
            artist: Artist name
            songs: Comma-separated list of song titles
        """
        # TODO: Call parent constructor
        # TODO: Store artist and songs
        super().__init__(title, copies_available)
        self.artist = artist
        self.songs = songs
        pass
    
    def get_artist(self) -> str:
        """Get the artist name."""
        # TODO: Return artist
        return self.artist
        pass
    
    def get_songs(self) -> str:
        """Get the songs list."""
        # TODO: Return songs
        return self.songs
        pass
    
    def __str__(self) -> str:
        """String representation including artist and songs."""
        # TODO: Return parent's string + ", Artist: [artist], Songs: [songs]"
        return f"Title: {self.title}, Copies Available: {self.copies_available}, Artist: {self.artist}, Songs: {self.songs}"
        pass
"""
**Expected Output When Working:**
```python
album = Album("Abbey Road", 1, "The Beatles", "Come Together,Something")
print(album)  # Should print: Title: Abbey Road, Copies Available: 1, Artist: The Beatles, Songs: Come Together,Something
```
"""

album = Album("Abbey Road", 1, "The Beatles", "Come Together,Something")
print(album)  # Should print: Title: Abbey Road, Copies Available: 1, Artist: The Beatles, Songs: Come Together,Something