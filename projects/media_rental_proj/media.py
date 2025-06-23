from abc import ABC
from functools import total_ordering

@total_ordering  # This gives you all comparison operators from __eq__ and __lt__
class Media(ABC):
    """
    Abstract base class for all media types.
    """
    
    def __init__(self, title: str, copies_available: int):
        """
        Initialize a media item.
        
        Args:
            title: The title of the media
            copies_available: Number of copies available for rent
        """
        # TODO: Store title and copies_available as instance variables
        self.title = title
        self.copies_available = copies_available
        pass
    
    def decrease(self):
        """Decrease available copies by 1 (when someone rents it)."""
        # TODO: Subtract 1 from copies_available
        self.copies_available -= 1
        pass
    
    def increase(self):
        """Increase available copies by 1 (when someone returns it)."""
        # TODO: Add 1 to copies_available
        self.copies_available += 1
        pass
    
    def get_title(self) -> str:
        """Get the title."""
        # TODO: Return the title
        return self.title
        pass
    
    def get_copies_available(self) -> int:
        """Get number of available copies."""
        # TODO: Return copies_available
        return self.copies_available 
        pass
    
    def __eq__(self, other):
        """Two media items are equal if they have the same title."""
        # TODO: Check if other is a Media object and compare titles
        return self.title == other.title 
        pass
    
    def __lt__(self, other):
        """Compare media by title for sorting."""
        # TODO: Compare titles alphabetically
        return self.title < other.title
        pass
    
    def __str__(self) -> str:
        """String representation."""
        # TODO: Return "Title: [title], Copies Available: [count]"
        return f"Title: {self.title}, Copies Available: {self.count}"
        pass
"""

**Test your Media class:**
```python
# Quick test - you should be able to run this
from media_rental_manager.models.media import Media


# This won't work yet (abstract class), but should be importable
"""
#from media_rental_manager.models.media import Media
