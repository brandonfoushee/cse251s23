import random
import string
import time
import threading


class FlightPath:
    
    def __init__(self, house):
        self.houses = houses
        self.my_house = 'Q'
    
    def atEnd(self, house):
        return house == self.my_house
    
    def get_start_house(self):
        return self.houses[0]

    def move(self):
        moveTo = []
        if(len(self.houses) > 0):
            moveTo.append(self.houses.pop(random.randrange(len(self.houses))))
            moveTo.append(self.houses.pop(random.randrange(len(self.houses))))
            time.sleep(0.1)
        return moveTo

def deliver_presents_recursively(flightPath: FlightPath, house, path):
    
    if flightPath.atEnd(house):
        print('We found my house')
        return

    path.append(house)
    
    nextHouses = flightPath.move()
    
    threads = []
    for nextHouse in nextHouses:
        t = threading.Thread(target=deliver_presents_recursively, args=(flightPath, nextHouse, path))
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()

if __name__ == '__main__':
    houses = list(string.ascii_lowercase + string.ascii_uppercase);
    print(f'{houses=}')
    
    path = []
    
    flightPath = FlightPath(houses)
    
    deliver_presents_recursively(flightPath, flightPath.get_start_house(), path)
    
    print(f'{path=}')
    