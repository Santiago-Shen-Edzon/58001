class DistanceConversion:
    def __init__(self, meter):
        self.__meter = meter

    def meters_to_cm(self):
        return (self.__meter * 100)

    def meters_to_km(self):
        return (self.__meter / 1000)

    def meters_to_inch(self):
        return (self.__meter * 39.37)

    def display(self):
        print("Meters to Centimeters =", self.meters_to_cm(), "cm")
        print("Meters to Kilometers =", self.meters_to_km(), "km")
        print("Meters to Inches =", self.meters_to_inch(), "inch")


Meters = float(input("Enter No. of Meters: "))

convert = DistanceConversion(Meters)
convert.meter = 1354354753354735473543573543
convert.display()