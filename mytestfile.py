import sys

print(f'length: {len(sys.argv)}')

if len(sys.argv) == 2:
    name = sys.argv[1]
else:
    name = 'stranger'
print(f'Hi there, {name}')

# alles is een object in python en een object kan methoden hebben.
print(name.replace('Q', 'k'))

# class is a blueprint of an object.


class Car:
    speed = 0
    started = False

    def start(self):
        self.started = True
        print("Car started, let ride!!")

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vroom')
        else:
            print('you need to start the car first')

    def stop(self):
        self.speed = 0
        print('Halting')


car = Car()

car.increase_speed(10)
car.start()
car.increase_speed(20)
car.stop()

print(id(car))

print(dir(car))
