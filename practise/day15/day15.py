class Stadium:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.events = {}

    def add_event(self, event_id, event_name, date, price):
        if event_id in self.events:
            print("Event ID already exists.")
            return
        self.events[event_id] = {
            "name": event_name,
            "date": date,
            "price": price,
            "booked_seats": 0
        }
        print("Event added successfully.")
    
    def show_events(self):
        if not self.events:
            print("No events available.")
            return
        print("\nAvailable Events:")
        for eid, event in self.events.items():
            print(f"ID: {eid}, Name: {event['name']}, Date: {event['date']}, "
                  f"Price: {event['price']}, Booked: {event['booked_seats']}")
    
    def book_ticket(self, event_id, seats):
        if event_id not in self.events:
            print("Event not found.")
            return
        event = self.events[event_id]
        if event["booked_seats"] + seats > self.capacity:
            print("Not enough seats available.")
            return
        event["booked_seats"] += seats
        total_cost = seats * event["price"]
        print(f"Tickets booked successfully. Total cost: {total_cost}")
    def cancel_ticket(self, event_id, seats):
        if event_id not in self.events:
            print("Event not found.")
            return
        event = self.events[event_id]
        if seats > event["booked_seats"]:
            print("Invalid cancellation.")
            return
        event["booked_seats"] -= seats
        print("Ticket cancelled successfully.")
    def available_seats(self, event_id):
        if event_id not in self.events:
            print("Event not found.")
            return
        event = self.events[event_id]
        print("Available seats:",
              self.capacity - event["booked_seats"])

stadium = Stadium("National Stadium", 50000)

while True:
    print("\n--- Stadium Management System ---")
    print("1. Add Event")
    print("2. Show Events")
    print("3. Book Ticket")
    print("4. Cancel Ticket")
    print("5. Check Available Seats")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        eid = input("Event ID: ")
        name = input("Event Name: ")
        date = input("Event Date: ")
        price = int(input("Ticket Price: "))
        stadium.add_event(eid, name, date, price)