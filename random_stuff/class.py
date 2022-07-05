#our_dog = {"name": "bruno", "colour": "brown"}

#print(our_dog["name"])

class Dog:
	def __init__(self, name, colour):
		self.name = name
		self.colour = colour
		self.energy = 1


	def describe(self):
		return f"{self.name} is {self.colour}"


our_dog = Dog("Bruno", "brown")

other_dog = Dog("cheena", "black")

#print(our_dog.name + " is " + our_dog.colour)
#print(other_dog.name + " is " + other_dog.colour)

print(other_dog.describe())
print(other_dog.energy, our_dog.energy)


raise RuntimeError(f"brun is tired .")
