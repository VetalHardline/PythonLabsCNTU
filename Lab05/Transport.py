class Transport:
    def __init__(self):
        self.value
        self.speed
        self.year
        self.coord

    def setval(self, input):
        if isinstance(input, float) or isinstance(input, int):
            self.value = input

    def setspeed(self, input):
        if isinstance(input, int):
            self.speed = input

    def setyear(self, input):
        if isinstance(input, int):
            self.year = input

    def setcoord(self, input):
        if isinstance(input, str):
            self.coord = input

class Car (Transport):
    def __init__(self):
        self.value = 0
        self.speed = 0
        self.year = 0
        self.coord = ""

    def showCar(self):
        print("\nCar characteristics\n"
              + "Value: " + str(self.value)
              + "\nSpeed: " + str(self.speed)
              + "\nYear: " + str(self.year)
              + "\nCoordinates: " + self.coord)


class Plane (Transport):
    def __init__(self):
        self.value
        self.speed
        self.year
        self.height
        self.passengers
        self.coord

    def _setheight(self, input):
        if isinstance(input, int):
            self.height = input

    def setpassengers(self, input):
        if isinstance(input, int):
            self.passengers = input

    def showPlane(self):
        print("\nPlane characteristics\n"
              + "Value: " + str(self.value)
              + "\nSpeed: " + str(self.speed)
              + "\nYear: " + str(self.year)
              + "\nCoordinates: " + self.coord
              + "\nHeight: " + str(self.height)
              + "\nPassengers: " + str(self.passengers))


class Ship (Plane):
    def __init__(self):
        self.value
        self.speed
        self.year
        self.port
        self.passangers
        self.coord

    def setport(self, input):
        if isinstance(input, str):
            self.port = input

    def showShip(self):
        print("\nShip characteristics\n"
              + "Value: " + str(self.value)
              + "\nSpeed: " + str(self.speed)
              + "\nYear: " + str(self.year)
              + "\nCoordinates: " + self.coord
              + "\nPort: " + self.port
              + "\nPassengers: " + str(self.passengers))