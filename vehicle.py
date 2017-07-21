class Vehicle:
    def __init__(self, name):
        self.name = name
        self.wheels = 0
        self.ingition = False
        self.passengers = []

    def num_wheels(self, newwheels):
        self.wheels = newwheels

    def ignition(self, key):
        self.ingition = key

    def add_passenger(self, newPassenger):
        self.passengers.append(newPassenger)

def main():
    myCar = Vehicle("Corolla")
    myCar.num_wheels(4)
    myCar.add_passenger("Favour")
    print(myCar.name, myCar.wheels, myCar.passengers)

if __name__ == '__main__':
    main()
