import queue
import time
import person
import logging
from main import SPEED

class Ride:

    def __init__(self, name, duration, capacity, intensity, minheight=120):
        self.name = name
        self.duration = duration
        self.capacity = capacity
        self.intensity = intensity
        self.frecuency = 0
        self.queue = []
        self.vipqueue = []

    def addClient(self, person):
        if person.vip: self.vipqueue.append(person)
        else: self.queue.append(person)

        person.location = self

    def getQueueTime(self):
        people = len(self.queue) + len(self.vipqueue)
        return (people / self.capacity) * self.duration

    def go(self):

        peopleGoing = []

        for i in range(self.capacity):
            if len(self.vipqueue) != 0 and (len(self.queue) == 0 or self.frecuency >= 2):
                peopleGoing.append(self.vipqueue.pop(0))
                self.frecuency = 0

            elif len(self.queue) != 0:
                peopleGoing.append(self.queue.pop(0))
                self.frecuency += 1
            
            else: break

        return peopleGoing

    
    def start(self):
        logging.debug(self.name + " STARTED!")
        while True:
            clients = self.go()
            time.sleep(self.duration / SPEED)

            for c in clients:
                c.location = None
