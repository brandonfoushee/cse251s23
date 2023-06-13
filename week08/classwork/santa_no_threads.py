import random
import string
import time


class FlightPath:
    
    def __init__(self, house):
        self.houses = houses
        self.my_house = 'Q'
    
    def atEnd(self, house):
        return house == self.my_house
    
    def get_start_house(self):
        return self.houses[0]

    def move(self):
        if(len(self.houses) > 0):
            moveTo = self.houses.pop(random.randrange(len(self.houses)))
            time.sleep(0.1)
            return moveTo
        return None
    


def deliver_presents_recursively(flightPath: FlightPath, house, path):
    
    if flightPath.atEnd(house):
        print('We found my house')
        return True

    path.append(house)
    
    nextHouse = flightPath.move()
    
    deliver_presents_recursively(flightPath, nextHouse, path)


if __name__ == '__main__':
    houses = list(string.ascii_lowercase + string.ascii_uppercase);
    print(f'{houses=}')
    
    path = []
    
    flightPath = FlightPath(houses)
    
    deliver_presents_recursively(flightPath, flightPath.get_start_house(), path)
    
    print(f'{path=}')
    