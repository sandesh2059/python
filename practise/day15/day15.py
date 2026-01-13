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