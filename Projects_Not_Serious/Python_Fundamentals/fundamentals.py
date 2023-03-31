class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def say_hello(self):
        print(f'Hello my name is {self.name}')

stephanie = Person('Stephanie', 29, 'Female')
print(stephanie.age)
