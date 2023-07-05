class Bus:
    def __init__(self, addList):
        self.capacity = 40
        self.passengers_list = list()
        self.address_list = addList

    def addPas(self, passenger):
        if len(self.passengers_list) == self.capacity:
            print(f"avtobusda bo'sh joy mavjud emas")
        elif passenger.get_address() in self.address_list and passenger.fromAddress in self.address_list:
            self.passengers_list.append(passenger)

    def outPas(self):
        outList = list()
        for address in self.address_list:
            for passenger in self.passengers_list:
                if passenger.get_fromAddress() == address:
                    outList.append(passenger)

            for outPassenger in outList:
                if outPassenger.get_address() == address:
                    print(f"{outPassenger.get_name()}\t\t\t{outPassenger.get_fromAddress()}\t\t\t{address}")
                    self.passengers_list.remove(outPassenger)
                    outList.remove(outPassenger)

        for address in reversed(self.address_list):
            for outPassenger in outList:
                if outPassenger.get_address() == address:
                    print(f"{outPassenger.get_name()}\t\t\t{outPassenger.get_fromAddress()}\t\t\t{address}")
                    self.passengers_list.remove(outPassenger)
                    outList.remove(outPassenger)

    def getCountPas(self):
        return len(self.passengers_list)

    def getEmptyCount(self):
        return self.capacity - len(self.passengers_list)


class Passenger:
    def __init__(self, name, fromAddress, address):
        self.name = name
        self.fromAddress = fromAddress
        self.address = address

    def get_address(self):
        return self.address

    def get_fromAddress(self):
        return self.fromAddress

    def get_name(self):
        return self.name

l = ["Chilonzor", "Olmazor  ", "Bektemir", "Yakkasaroy"]
b = Bus(l)
print(l)
p1 = Passenger("p1", "Olmazor  ", "Chilonzor")
p2 = Passenger("p2", "Chilonzor", "Bektemir")
p3 = Passenger("p3", "Chilonzor", "Olmazor  ")
p4 = Passenger("p4", "Olmazor  ", "Yakkasaroy")
p5 = Passenger("p5", "Yakkasaroy", "Chilonzor")
p6 = Passenger("p6", "Bektemir", "Olmazor  ")
p7 = Passenger("p7", "Chilonzor", "Yakkasaroy")
p8 = Passenger("p8", "Yakkasaroy", "Olmazor  ")
p9 = Passenger("p9", "Bektemir", "Chilonzor")
p10 = Passenger("p10", "Bektemir", "Yakkasaroy")
p11 = Passenger("p11", "Mirobod", "Yakkasaroy")
b.addPas(p1)
b.addPas(p2)
b.addPas(p3)
b.addPas(p4)
b.addPas(p5)
b.addPas(p6)
b.addPas(p7)
b.addPas(p8)
b.addPas(p9)
b.addPas(p10)
b.addPas(p11)
print(b.getCountPas())
b.outPas()
