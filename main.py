import person
import ride
import random
import threading
import time
import utils

SPEED = 10

rides = []
ridesThreads = []
clients = []

def createRides():
    rides.append(ride.Ride("Boomerang", 20, 2, 3))
    rides.append(ride.Ride("Black Hole", 40, 2, 1))
    rides.append(ride.Ride("Rapidos", 15, 2, 1))
    rides.append(ride.Ride("Hydro Racer", 30, 4, 2))
    rides.append(ride.Ride("Speed Race", 20, 4, 2))
    rides.append(ride.Ride("Zig-Zag", 40, 2, 2))
    rides.append(ride.Ride("Minis", 20, 3, 1))
    rides.append(ride.Ride("Kamikaze", 10, 2, 3))

def openRides():
    for r in rides:
        t = threading.Thread(target=ride.Ride.start, args=(r,))
        t.start()
        ridesThreads.append(t)
    

def createClients(n):
    for i in range(n):
        clients.append(person.Person.getRandomPerson())

def updateClients():
    while True:
        for c in clients:
            if(c.location == None):
                while True:
                    n = random.randint(0, 500)
                    if n < 8:
                        if (decision(c, rides[n])):
                            c.location = rides[n]
                            rides[n].addClient(c)
                    else: break
        time.sleep(5 / SPEED)

def decision(client, ride):
    if ride.intensity > client.brave:
        return False
    
    if client.vip: return True
    n = random.randint(0, round(ride.getQueueTime() / 30) ** 2)

    if n >= 50: return False

    return True


def printClientsInfo():
    for c in clients:
        print(f"Name: {c.name}, Age: {c.age}, Sex: {c.sex}, Height: {c.height}, Weight: {c.weight}, Brave: {c.brave}, Vip: {c.vip}")

def printRidesInfo():
    for r in rides:
        print(f"Name: {r.name}, QueueLength: {len(r.queue)}, VipQueueLength: {len(r.vipqueue)}")

def whereClientsAre():
    for c in clients:
        loc = c.location
        
        if loc != None: print(c.location.name)
        else: print("None")

if __name__ == "__main__":
    utils.loadFromFile()
    createRides()
    openRides()
    createClients(3000)

    threading.Thread(target=updateClients).start()
  

    while True:
        printRidesInfo()
        #whereClientsAre()
        time.sleep(0.1)
        
        for i in range(8): print ("\033[A                             \033[A")