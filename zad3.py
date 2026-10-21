class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
    def __str__(self):
        return f"Nieruchomość o powierzchni {self.area} m², liczba pokoi: {self.rooms}, cena: {self.price} zł, adres: {self.address}"

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot
    def __str__(self):
        return f"Dom: {super().__str__()}, powierzchnia działki: {self.plot} m²"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor
    def __str__(self):
        return f"Mieszkanie: {super().__str__()}, piętro: {self.floor}"

house1 = House(area=150, rooms=5, price=850000, address="ul. Słoneczna 12, Warszawa", plot=600)

flat1 = Flat(area=55, rooms=2, price=450000, address="ul. Kwiatowa 5/14, Kraków", floor=3)

print(house1)
print(flat1)