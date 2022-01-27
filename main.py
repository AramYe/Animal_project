# Напишіть клас Animal, який при створенні екземпляру надає йому атрибут виду тварини species. Клас має містити метод, який виводить інформацію про вид тварини, і метод, який виводить характерний звук для даного виду тварини. Створіть два класи Dog і Cat, які успадковуються від класу Animal (є підкласами для Animal). У кожному з підкласів реалізуйте виклик конструктора надкласу з передачею йому назви виду тварини. Також, у підкласах реалізуйте методи, які перевизначають метод надкласу для відтворення характерного звуку для конкретного виду тварини. Визначте окрему функцію show_animal_info, яка приймає об’єкт (екземпляр класу) як аргумент і викликає його методи show_species і make_sound, якщо це тварина, а інакше - виводиться відповідне повідомлення як у вихідних даних.

# Write an Animal class that, when creating an instance, gives it the attribute of an animal species. The class must contain a method that outputs information about the animal species and a method that outputs a characteristic sound for that species. Create two classes, Dog and Cat, which are inherited from the Animal class (are subclasses for Animal). In each of the subclasses, implement the call of the superclass designer with the name of the animal species. Also, in subclasses, implement methods that override the superclass method to reproduce the characteristic sound for a particular animal species. Define a separate show_animal_info function that takes an object (instance of a class) as an argument and calls its show_species and make_sound methods if it is an animal, otherwise it displays the appropriate message as in the source data.

# Вхідні дані:
# Немає

# Вихідні дані:
# I'm an - ordinary animal
# Grrr!
# I'm an - dog
# Woof! Woof!
# I'm an - cat
# Meow!
# Book is not an animal!

from animal import Animal
from dog import Dog
from cat import Cat
from book import Book

animal = Animal("Basic")
dog = Dog("Shepherd")
cat = Cat("Egyptian")
book = Book()

animals = [animal, dog, cat, book]

def print_animal_info(some_animal: Animal):
    if isinstance(some_animal, Animal):
        some_animal.show_species()
        some_animal.make_sound()
    else:
        some_animal.show_info()

for current_animal in animals:
    print_animal_info(current_animal)