#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __repr__(self):
        return f"{self.source}, {self.destination}"


def reconstruct_trip(tickets, given_length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    start = None
    end = None
    cache = {}
    # first I will need to find the beginning ticket
    for i in tickets:
        if i.source == "NONE":
            start = i
        # then find the ending ticket, you may need it
        if i.destination == "NONE":
            end = i
    # create the hashed keys and values in cache
    for i in tickets:
        cache[i.source] = i.destination

    # wherever the source is NONE, add that destination to the route,
    # after that, wherever that previous destination == source,
    # append that destination to route.
    # continue until destination == NONE

    if start not in route:
        route.append(start.destination)

    while (len(route)) < given_length:
        route.append(cache[route[len(route) - 1]])
    return route


# ticket_1 = Ticket("PIT", "ORD")
# ticket_2 = Ticket("XNA", "SAP")
# ticket_3 = Ticket("SFO", "BHM")
# ticket_4 = Ticket("FLG", "XNA")
# ticket_5 = Ticket("NONE", "LAX")
# ticket_6 = Ticket("LAX", "SFO")
# ticket_7 = Ticket("SAP", "SLC")
# ticket_8 = Ticket("ORD", "NONE")
# ticket_9 = Ticket("SLC", "PIT")
# ticket_10 = Ticket("BHM", "FLG")

# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
#            ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

# expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
#             "SLC", "PIT", "ORD", "NONE"]

# reconstruct_trip(tickets, 10)
