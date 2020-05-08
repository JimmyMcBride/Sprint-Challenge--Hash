#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    my_list = []
    cache = {}

    for ticket in tickets:
        # print(ticket.source, ticket.destination)
        if ticket.source not in cache:
            cache[ticket.source] = ticket.destination
        if ticket.source == "NONE":
            my_list.append(ticket.destination)

    for i in range(length - 1):
        my_list.append(cache[my_list[i]])

    # print(cache["NONE"], cache[f"{cache["NONE"]}")

    return my_list


tickets = [
    Ticket("PIT", "ORD"),
    Ticket("XNA", "CID"),
    Ticket("SFO", "BHM"),
    Ticket("FLG", "XNA"),
    Ticket("NONE", "LAX"),
    Ticket("LAX", "SFO"),
    Ticket("CID", "SLC"),
    Ticket("ORD", "NONE"),
    Ticket("SLC", "PIT"),
    Ticket("BHM", "FLG"),
]

print(reconstruct_trip(tickets, len(tickets)))
