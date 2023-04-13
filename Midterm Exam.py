class Circle:
    def __init__(self, radius, diameter):
        self.__radius = radius
        self.__diameter = diameter

    def area_rad(self):
        return round(3.14 * (self.__radius **2), 2)

    def perimeter_rad(self):
        return round(2 * ((3.14) * self.__radius), 2)

    def area_dia(self):
        return round(3.14 * ((self.__diameter / 2) **2), 2)

    def perimeter_dia(self):
        return round(2 * ((3.14) * (self.__diameter / 2)), 2)

    def display_rad(self):
        print(f"\nThe area is: {self.area_rad()} m², and the perimeter is: {self.perimeter_rad()} m")

    def display_dia(self):
        print(f"\nThe area is: {self.area_dia()} m², and the perimeter is: {self.perimeter_dia()} m")



answer = input("Press [1] if radius, [2] if diameter: ")

if answer == '1':
    Radius = float(input("\nPlease enter your radius in Meters: "))

    circle = Circle(Radius, 0)
    circle.display_rad()
    circle.radius = 21354321654354387435143
elif answer == '2':
    Diameter = float(input("\nPlease enter your diameter in Meters: "))

    circle = Circle(0, Diameter)
    circle.display_dia()
    circle.diameter = 68432138743213743513534