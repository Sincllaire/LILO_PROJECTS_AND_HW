from media import Media

class Movie(Media):
    """
    Movie class with rating information.
    """
    
    def __init__(self, title: str, copies_available: int, rating: str):
        """
        Initialize a movie.
        
        Args:
            title: Movie title
            copies_available: Number of copies available
            rating: Movie rating (e.g., "PG", "R", "NR")
        """
        # TODO: Call parent constructor with title and copies_available
        # TODO: Store rating as instance variable
        # we call these both to inherit the functions from the other script so that it can act the same and have the same functions here as well. 
        super().__init__(title, copies_available)# the parent constructor that we defined in the media script
        self.rating = rating
        pass

    
    def get_rating(self) -> str:
        """Get the movie rating."""
        # TODO: Return the rating
        return self.rating
        pass
    
    def __str__(self) -> str:
        """String representation including rating."""
        # TODO: Return parent's string + ", Rating: [rating]"
        return f"Title: {self.title} , Copies Available: {self.copies_available}, Rating: {self.rating}"
        pass
"""

**Expected Output When Working:**
```python
movie = Movie("Jaws", 2, "PG")
print(movie)  # Should print: Title: Jaws, Copies Available: 2, Rating: PG
print(movie.get_title())  # Should print: Jaws
print(movie.get_rating()) # Should print: PG
```
"""
movie = Movie("Jaws", 2, "PG")
print(movie)  # Should print: Title: Jaws, Copies Available: 2, Rating: PG
print(movie.get_title())  # Should print: Jaws
print(movie.get_rating()) # Should print: PG