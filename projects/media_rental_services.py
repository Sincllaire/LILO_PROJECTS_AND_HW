from typing import List
from .media_rental_manager_interface import MediaRentalManagerInterface
from ..models.customer import Customer
from ..models.media import Media
from ..models.movie import Movie
from ..models.album import Album

class MediaRentalManager(MediaRentalManagerInterface):
    """
    Main rental management system implementation.
    """
    
    def __init__(self):
        """Initialize with empty databases."""
        self.media_limit = 2  # Default limit for LIMITED plans
        self.customer_database: List[Customer] = []
        self.media_database: List[Media] = []
    
    def add_customer(self, name: str, address: str, plan: str) -> None:
        """Add a customer to the database."""
        # TODO: Create Customer object and add to customer_database
        customer = Customer(name, address, plan)
        self.customer_database.append(customer)
        pass
    
    def add_movie(self, title: str, copies_available: int, rating: str) -> None:
        """Add a movie to the database."""
        # TODO: Create Movie object and add to media_database
        movie = Movie(title, copies_available,rating)
        self.media_database.append(movie)
        pass
    
    def add_album(self, title: str, copies_available: int, artist: str, songs: str) -> None:
        """Add an album to the database."""
        # TODO: Create Album object and add to media_database
        album = Album(title, copies_available,artist, songs)
        self.media_database.append(album)
        pass
    
    def set_limited_plan_limit(self, value: int) -> None:
        """Set the rental limit for LIMITED plan customers."""
        # TODO: Update self.media_limit
        if self.media_limit == "LIMITED":
            self.value = 2
        pass
    
    def get_all_customers_info(self) -> str:
        """Get formatted information about all customers, sorted by name."""
        # TODO: Return formatted string starting with "***** Customers' Information *****\n"
        info = "***** Customers' Information *****\n"
       
        #Name: Brown, Bob, Address: 789 Pine Rd, Plan: LIMITED
        for customer in sorted(self.customer_database):
            info += f"Name: {customer.name}, Address: {customer.address} Plan:  {customer.plan} \n"
            info += f"rented: {customer.rented_stuff} \n"
            info += f"queue: {customer.want_queue} \n"
        return info
        pass
    
    def get_all_media_info(self) -> str:
        """Get formatted information about all media, sorted by title."""
        #Title: Abbey Road, Copies Available: 2, Artist: The Beatles, Songs: Come Together,Something,Maxwell's Silver Hammer
        #Title: Casablanca, Copies Available: 3, Rating: NR
        # TODO: Return formatted string starting with "***** Media Information *****\n"
        info = "***** Media Information *****\n"
        for media in sorted(self.media_database):
            if isinstance(media, Movie):
                info += f"Title: {media.title} Copies Available: {media.copies_available} Artist: {media.artist} Songs: {media.songs}\n"
            if (media, Album):
                info += f"Title: {media.title} Copies Available: {media.copies_available} Rating: {media.rating}\n"
        return info
        pass
    
    def add_to_queue(self, customer_name: str, media_title: str) -> bool:
        """Add media to customer's queue if not already rented or queued."""
        # TODO: Find customer and add media to their want_queue if not already there
        #search for customer
        #if there is nothing in their want queue, add something there
        for customer in self.customer_database:
            if customer.name == customer.name:
                if media_title in customer.want_queue or media_title in customer.rented_stuff:
                    return False
                customer.want_queue.append(media_title)
                return True
        return False
        pass
    
    def remove_from_queue(self, customer_name: str, media_title: str) -> bool:
        """Remove media from customer's queue."""
        # TODO: Find customer and remove media from their want_queue

        for customer in self.customer_database:
            if customer.name == customer.name:
                if media_title in customer.want_queue or media_title in customer.rented_stuff:
                    customer.want_queue.append(media_title)
                    return True
        return False
        pass
    
    def process_requests(self) -> str:
        """Process all customer requests."""
        #if the customer not in database, skip
        # if customer is at the max of titles that they can have in rented stuff, or they have a limited plan, skip
        #you need a next title variable. kind of like pointers next, and it needs to equal to the want queue having nothing in it
        #for the media within the database
        #you have to take a media copy
        #add it to rented stuff
        #and remove it from the want list
        #send out process message
        #return output
        # TODO: This is the complex method - study the expected output below!
        for customer in self.customer_database:
            if not customer.want_queue:
                continue
            if customer.plan == "LIMITED" and len(customer.rented_stuff) >= self.media_limit:
                continue
            next.title = customer.want_queue[0]
            for media in self.media_database:
                if media.title == next.title and media.copies_available > 0:
                    media.copies_available -= 1
                    customer.rented_stuff.append(next.title)
                    customer.want_queue.remove(next.title)
                    output += f" Sending {media.title} to {customer.name}"
        return output
        pass
    
    def return_media(self, customer_name: str, media_title: str) -> bool:
        """Process a media return."""
        # TODO: Remove from customer's rented list and increase media availability
        # for customer in the database 
        #if customer.name == customer_name:
        # if media title in rented stuff lise
        # customer.rented-stuff remove(media.title)
        # for the media title in the media database:
        #if media title == media_title(one is the name of the media and one is the space in the database)
        # the copy available in the media database is added 
        # return for true 
        for customer in self.customer_database:
            if customer.name == customer_name:
              if media_title in customer.rented_stuff:
                  customer.rented_stuff.remove(media_title)
                  for media in self.customer_database:
                      if media.title == media_title:
                          media.copies_available += 1
                          return True
        return False
        pass
    
    def search_media(self, title: str = None, rating: str = None, 
                    artist: str = None, songs: str = None) -> List[str]:
        """Search for media matching criteria.
        # need a results list
        # for the media in the media database 
        if the media is not the media title database, continue
        if the movie, rating and the media database rating of the media doesnt match continue
        if the album, artist and the media database artist dont match contine
        if the songs, song of the media not in the media database of songs continue
        you need to append the media title found to the results list 
        return the sorted list of results 
        """
        # TODO: Return sorted list of matching media titles
        results = []
        for media in self.media_database:
            if title and title.lower() not in media.title.lower():
                continue
            if isinstance(media, Movie) and rating and media.rating != rating:
                continue
            if isinstance(media, Album):
                if artist and media.artist != artist:
                    continue
                if songs and songs not in str(media.songs):
                    continue
            results.append(media.title)
        return sorted(results)
        pass
