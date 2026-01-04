# # # 🧩 LEVEL 1: Core Python (Logic + Confidence)
# # # Task 1: Number Utility

# # # Create functions to:

# # # Reverse a number

# # # Check palindrome

# # # Count digits

# # # Sum of digits

# # # 👉 Rules

# # # No input inside logic functions

# # # Use return

# # # One menu function handles input/output

# # class NumberAnalyzer():

# #     def __init__(self, n):
# #         self.number = n

# #     def reverse(self):
# #         rev = 0
# #         n = self.number
# #         while n > 0:
# #             rev = rev * 10 + (n % 10)
# #             n //= 10
# #         return rev   

# #     def palindrome(self):
# #         if self.number == self.reverse():
# #             return True
# #         return False
# #     def count_digits(self):
# #         count = 0
# #         n = self.number
# #         while n > 0:
            
# #             count += 1
# #             n //= 10
            
# #         return count
# #     def sum_of_digits(self):
# #         total = 0
# #         n = self.number
# #         while n > 0:
            
# #             total += n % 10
# #             n //= 10
# #         return total
# # num1 = NumberAnalyzer(334433)
# # print(f"the reverse of {num1.number} is {num1.reverse()}")
# # print(f"palindrome: {num1.palindrome()}")
# # print(f"the total number of digits in {num1.number} is {num1.count_digits()}")
# # print(f"the sum of all digits in {num1.number} is {num1.sum_of_digits()}")
            

        













# # functions

# # 🧩 LEVEL 2: Strings + Collections (Real Logic)
# # Task 3: Username Cleaner

# # Input:

# # ["Jaaannne", "Maaarrk", "Alleeexx"]


# # Output:

# # ["Jane", "Mark", "Alex"]


# # 👉 Rules:

# # No set

# # Preserve order

# # Create a reusable function

# l = ['jaaannnee', 'mmmaaarrrkkk', 'aallleexxx']
# result = []

# def clean():
#     for word in l:
#         unique = ''
#         for ch in word:
#             if ch not in unique:
#                 unique += ch
#         result.append(unique)
#     return result
# print("the result is ", clean())






class Stadium:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.available_seats = capacity

    def book_seats(self, seats):
        if seats <= self.available_seats:
            self.available_seats -= seats
            return True
        return False
    
    def cancel_seats(self, seats):
        if self.available_seats + seats <= self.capacity:
            self.available_seats += seats
            return True
        return False
    
class Event:
    def __init__(self, event_name, stadium):
        self.event_name = event_name
        self.stadium = stadium
        self.bookings = []

class Booking:
    def __init__(self, customer_name, seats):
        self.customer_name = customer_name
        self.seats = seats

class StadiumService:
    def __init__(self):
        self.stadiums = []
        self.events = []

    def add_stadium(self, name, capacity):
        self.stadiums.append(Stadium(name, capacity))

    def add_event(self, event_name, stadium_name):
        for stadium in self.stadiums:
            if stadium.name == stadium_name:
                self.events.append(Event(event_name, stadium))
                return True
        return False

    def get_events(self):
        return self.events
    
    def book_ticket(self, event_name, customer_name, seats):
        for event in self.events:
            if event.event_name == event_name:
                if event.stadium.book_seats(seats):
                    event.bookings.append(Booking(customer_name, seats))
                    return True
                return False
        return None
    
    def cancel_ticket(self, event_name, customer_name):
        for event in self.events:
            if event.event_name == event_name:
                for booking in event.bookings:
                    if booking.customer_name == customer_name:
                        event.stadium.cancel_seats(booking.seats)
                        event.bookings.remove(booking)
                        return True
        return False