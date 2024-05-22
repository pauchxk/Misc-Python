class SmartPlug:
    def __init__(self, consumption_rate):
        self.consumption_rate = consumption_rate

    def getConsump(self):
        return self.consumption_rate

class SmartHome:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def get_devices(self):
        return self.devices

def setUpHome():
    smart_home = SmartHome()
    for _ in range(5):
        consumption_rate = input("C Rate: ")
        smart_plug = SmartPlug(consumption_rate)
        smart_home.add_device(smart_plug)
    print(smart_home.get_devices())
    print(smart_plug.getConsump())
    print(smart_home.devices[2].getConsump)

setUpHome()

#THE NAME DOESN'T MATTER, YOU REFERENCE THE OBJECT BY THE INDEX OF THE LIST!!!!!#