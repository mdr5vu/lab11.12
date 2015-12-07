class Cat:
    #constructor - name, age
    #data -- name, age
    #functions - eat, prints out a thank you message

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + " thanks you!")

    def birthday(self):
        self.age = self.age + 1

    def toString(self):
        print(self.name + " is " + str(self.age) + " years old!")

nifty = Cat("Nifty",6)
sparkle = Cat("Sparkle",5)

nifty.toString()
sparkle.toString()

#nifty is the parameter than im passing to eat
#can pass nifty as an argument, in eat function how to i refer to the
#value of the argument that got passed in? self
#within the eat function, how do i refer to the value that got passed
#in it

#eat(nifty)
#eat(sparkle)

#write it because eat is a member function of this class, write it how
#we do below
#if you see something with stuff in the parenthesis, you have to call
#that function
nifty.eat()
sparkle.eat()

#adding member function to a class that changes the state of the
#object. the way we define is type is with a class and we have two
#different functions we can apply to objects of that type. getters get
#the value out of a field and does something with it. here the setter
#operates on a class, gets the data out of that class, does something
#with it, and updates the value of that. object oriented program-
#model objects in your domains as classes. objects send messages back
#and forth to eachother
nifty.birthday()
nifty.toString()
