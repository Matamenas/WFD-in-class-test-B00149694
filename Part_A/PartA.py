import unittest

# A2
class Phone:
    def __init__(self, brand, model, year, price, colour):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.colour = colour

    # A3
    def display(self):
        print("Brand: {}".format(self.brand))
        print("Model: {}".format(self.model))
        print("Year: {}".format(self.year))
        print("Price: {}".format(self.price))
        print("Colour: {}".format(self.colour))

    # A4
    def updateBrand(self, brand):
        self.brand = brand

    def updateModel(self, model):
        self.model = model

    def updateYear(self, year):
        self.year = year

    def updatePrice(self, price):
        self.price = price

    def updateColour(self, colour):
        self.colour = colour

# B5
class test_Updates(unittest.TestCase):
    def testUpdateBrand(Phone):
        brand = "Brand"
    def testUpdateModel(Phone):
        model = "Model"
    def testUpdateYear(Phone):
        year = "Year"
    def testUpdatePrice(Phone):
        price = "Price"
    def testUpdateColour(Phone):
        colour = "Colour"

# B5
if __name__ == "__main__":
    unittest.main()

# A5
class androidPhone(Phone):
    def __init__(self, chargingPort, brand, model, year, price, colour):
        super().__init__(brand, model, year, price, colour)
        self.chargingPort = chargingPort
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.colour = colour

    # A6
    def display(self):
        print("Charging Port: {}".format(self.chargingPort))
        print("Brand: {}".format(self.brand))
        print("Model: {}".format(self.model))
        print("Year: {}".format(self.year))
        print("Price: {}".format(self.price))
        print("Colour: {}".format(self.colour))

    # A7
    def updateChargingPort(self, chargingPort):
        self.chargingPort = chargingPort

    def updateBrand(self, brand):
        self.brand = brand

    def updateModel(self, model):
        self.model = model

    def updateYear(self, year):
        self.year = year

    def updatePrice(self, price):
        self.price = price

    def updateColour(self, colour):
        self.colour = colour

# A8
Phone1 = Phone("IPhone", "15 XR", "2016", "699.99", "Silver")
Phone2 = androidPhone("Type-C","Samsung", "Galaxy 7", "2018", "800.00", "Red")

# A9
print("initial Phones: ")
print("\nPhone 1")
Phone1.display()
print("\nPhone 2")
Phone2.display()

Phone1.updateModel("16 XE")
Phone1.updateYear("2018")

Phone2.updateChargingPort("Micro-Usb")
Phone2.updatePrice("500.00")

print("\nAfter updating:\n ")
print("\nPhone 1")
Phone1.display()
print("\nPhone 2")
Phone2.display()




