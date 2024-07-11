class Offer:
    def __init__(self, deptime, arrtime, ori, dest, cst, line):
        self.departure_time = deptime
        self.arrival_time = arrtime
        self.origin = ori
        self.destination = dest
        self.cost = cst
        self.airline = line


    def display(self):
        return f"Offer by {self.airline} \nFrom: {self.origin} To: {self.destination} ({self.departure_time}-{self.arrival_time}) \nCost: {self.cost}\n"