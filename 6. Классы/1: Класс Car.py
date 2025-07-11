class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.engine_started = False

    def start_engine(self):
        self.engine_started = True

    def stop_engine(self):
        self.engine_started = False

    def print_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Цвет: {self.color}")
        print(f"Двигатель запущен: {'Да' if self.engine_started else 'Нет'}")
        print()

car1 = Car("Toyota", "Camry", 2020, "черный")
car2 = Car("BMW", "X5", 2019, "белый")
car3 = Car("Audi", "A4", 2021, "синий")

print("Информация о car1:")
car1.print_info()
car1.start_engine()
print("После запуска двигателя:")
car1.print_info()
car1.stop_engine()
print("После остановки двигателя:")
car1.print_info()

print("\nИнформация о car2:")
car2.print_info()
car2.start_engine()
print("После запуска двигателя:")
car2.print_info()
car2.stop_engine()
print("После остановки двигателя:")
car2.print_info()

print("\nИнформация о car3:")
car3.print_info()
car3.start_engine()
print("После запуска двигателя:")
car3.print_info()
car3.stop_engine()
print("После остановки двигателя:")
car3.print_info()