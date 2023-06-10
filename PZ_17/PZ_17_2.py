# Создайте класс "Животное", который содержит информацию о виде и возрасте
# животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
# "Животное" и содержат информацию о породе. На питоне

class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age

class Dog(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

class Cat(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

dog = Dog("собака", 5, "Корги")
print(dog.species)  # dog
print(dog.age)      # 3
print(dog.breed)    # Labrador

cat = Cat("кошка", 1, "Русская голубая")
print(cat.species)  # cat
print(cat.age)      # 2
print(cat.breed)    # Persian
