class CARPARK:
    def __init__(self):
        self.total_cars = 0
        self.total_money_collected = 0.0
        
    def pavingCar(self):
        self.total_cars += 1
        self.total_money_collected += 0.50
        
    def nopayCar(self):
        self.total_cars += 1
        
    def displayStats(self):
        print("Total cash collected:", self.total_money_collected)
        print("Total cars:", self.total_cars)

carpark = CARPARK()

carpark.pavingCar()
carpark.pavingCar()
carpark.nopayCar()

carpark.displayStats()
