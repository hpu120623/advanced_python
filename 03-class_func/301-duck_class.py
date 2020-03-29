# Python的鸭子模型:所有的类、对象实现了共同的方法，这个方法名一样，可以同时调用该方法
class Cat:
    def say(self):
        print("I'm a cat")


class Dog:
    def say(self):
        print("I'm a dog")


class Duck:
    def say(self):
        print("I'm a duck")


animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()
