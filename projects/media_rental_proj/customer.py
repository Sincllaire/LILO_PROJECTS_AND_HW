from typing import List
from functools import total_ordering

@total_ordering
class Customer:
    """
    Customer with rental plan and queue management.
    """
    
    def __init__(self, name: str, address: str, plan: str):
        """
        Initialize a customer.
        
        Args:
            name: Customer name
            address: Customer address
            plan: "LIMITED" or "UNLIMITED"
        """
        # TODO: Store name, address, plan
        # TODO: Initialize empty lists for rented_stuff and want_queue
        self.name = name
        self.address = address
        self.plan = plan
        self.rented_stuff = []
        self.want_queue = []
        pass
    
    def get_name(self) -> str:
        # TODO: Return name
        return self.name
        pass
    
    def get_address(self) -> str:
        # TODO: Return address
        return self.address
        pass
    
    def get_plan(self) -> str:
        # TODO: Return plan
        return self.plan
        pass
    
    def get_rented_stuff(self) -> List[str]:
        """Get list of currently rented media titles."""
        # TODO: Return rented_stuff list
        return self.rented_stuff
        pass
    
    def get_want_queue(self) -> List[str]:
        """Get list of media titles customer wants to rent."""
        # TODO: Return want_queue list
        return self.want_queue
        pass
    
    def __eq__(self, other):
        """Customers are equal if they have the same name."""
        # TODO: Compare names
        return self.name == other.name
        pass
    
    def __lt__(self, other):
        """Compare customers by name for sorting."""
        # TODO: Compare names alphabetically
        return self.name < other.name
        pass
    
    def __str__(self) -> str:
        """String representation showing rental status."""
        # TODO: Return multi-line string with name, address, plan, rented items, and queue
        return f"Name: {self.name}, Address: {self.address}, Plan: {self.plan}, Rented Items: {self.rented_stuff}, Queue: {self.want_queue}"
        pass
"""
```

**Expected Output When Working:**
```python
customer = Customer("Smith, John", "123 Main St", "LIMITED")
print(customer.get_name())  # Should print: Smith, John
customer.get_want_queue().append("Jaws")  # Add to queue
customer.get_rented_stuff().append("Rocky")  # Add to rented
print(customer)
# Should print:
# Name: Smith, John, Address: 123 Main St, Plan: LIMITED
# Rented: ['Rocky']
# Queue: ['Jaws']
```
"""
customer = Customer("Smith, John", "123 Main St", "LIMITED")
print(customer.get_name())  # Should print: Smith, John
customer.get_want_queue().append("Jaws")  # Add to queue
customer.get_rented_stuff().append("Rocky")  # Add to rented
print(customer)
# Should print:
# Name: Smith, John, Address: 123 Main St, Plan: LIMITED
# Rented: ['Rocky']
# Queue: ['Jaws']