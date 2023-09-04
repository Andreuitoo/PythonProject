import random
import csv

# Llibreries per construir es cocho
brands_models = {'Ford': ['EscortRs', 'MustangGT500'], 
                 'Renault': ['clioRs', 'meganeRs'], 
                 'Toyota': ['SupraMK4', 'Rav4'], 
                 'Nissan': ['180sx', '200sx'], 
                 'Honda': ['CivicTypeR', 'Nsx'], 
                 'Audi': ['A4', 'A3'], 
                 'Mercedes': ['claseC', 'amg'], 
                 'Chevrolet': ['Corvette', 'Camaro']
                }
h_powers = {90, 110, 150, 190, 220, 250, 280, 300, 330, 370, 420, 500}
combustions = {'Diesel', 'Gasoline', 'Hybrid', 'Electric'}
gears = {'Manual', 'Automatic'}

class Car:

    def __init__(self, brand, model, h_power, combustion, gear):
        self.brand = brand
        self.model = model
        self.h_power = h_power
        self.combustion = combustion
        self.gear = gear

    def __str__(self):
        return 'tu coche es un: ' + self.brand + ' ' + self.model + ' ' + str(self.h_power)+ 'cv' + ' ' + self.combustion + ' ' + self.gear
    

class CarsCreator:

    def __init__(self):
        self.all_cars = []

        for brand, brand_models in brands_models.items():
            for model in brand_models:
                h_power = random.choice(list(h_powers))
                combustion = random.choice(list(combustions))
                gear = random.choice(list(gears))
                create_car = Car(brand, model, h_power, combustion, gear)
                self.all_cars.append(create_car)

        self.player1_cars = self.all_cars[:len(self.all_cars) // 2]
        self.player2_cars = self.all_cars[len(self.all_cars) // 2:]

    def shuflle_cars(self):
        random.shuffle(self.all_cars)


    def select_two_cars(self):
        player1_cars = random.sample(self.player1_cars, 2)
        player2_cars = random.sample(self.player2_cars, 2)
        return player1_cars, player2_cars


    def __str__(self):
        car_comp = ''
        for car in self.all_cars:
            car_comp += '\n' + car.__str__()
        return "Coches disponibles: " + car_comp
    

def simulate_race(player1_cars, player2_cars):
    # Aquí puedes implementar la lógica de la carrera
    # Por ejemplo, comparar las características de los coches para determinar el ganador
    pass


cars = CarsCreator()
cars.shuflle_cars()


# Cada jugador selecciona dos coches aleatoriamente
player1_cars, player2_cars = cars.select_two_cars()
print("Jugador 1:")
for car in player1_cars:
    print(car)

print("Jugador 2:")
for car in player2_cars:
    print(car)

# Simular la carrera
simulate_race(player1_cars, player2_cars)