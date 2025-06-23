from abc import ABC, abstractmethod
from typing import List

class MediaRentalManagerInterface(ABC):
    """
    Main rental management system implementation.
    """  
    @abstractmethod
    def add_customer(self, name: str, address: str, plan: str) -> None:
        """Add a customer to the database."""
        pass
    
    @abstractmethod
    def add_movie(self, title: str, copies_available: int, rating: str) -> None:
        """Add a movie to the database."""
        pass
    
    @abstractmethod
    def add_album(self, title: str, copies_available: int, artist: str, songs: str) -> None:
        """Add an album to the database."""
        pass
    
    @abstractmethod
    def set_limited_plan_limit(self, value: int) -> None:
        """Set the rental limit for LIMITED plan customers."""
        pass
    
    @abstractmethod
    def get_all_customers_info(self) -> str:
        """Get formatted info about all customers, sorted by name."""
        pass
    
    @abstractmethod
    def get_all_media_info(self) -> str:
        """Get formatted info about all media, sorted by title."""
        pass
    
    @abstractmethod
    def add_to_queue(self, customer_name: str, media_title: str) -> bool:
        """Add media to customer's want queue. Returns False if already queued/rented."""
        pass
    
    @abstractmethod
    def remove_from_queue(self, customer_name: str, media_title: str) -> bool:
        """Remove media from customer's queue."""
        pass
    
    @abstractmethod
    def process_requests(self) -> str:
        """Process all customer queues. Returns string of rental confirmations."""
        pass
    
    @abstractmethod
    def return_media(self, customer_name: str, media_title: str) -> bool:
        """Process a media return."""
        pass
    
    @abstractmethod
    def search_media(self, title: str = None, rating: str = None, 
                    artist: str = None, songs: str = None) -> List[str]:
        """Search media by criteria. Returns sorted list of matching titles."""
        pass