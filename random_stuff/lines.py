class lines:
	def __init__(self, length, x_coordinate, y_coordinate):
		self.length = length
		self.x_coordinate = x_coordinate
		self.y_coordiante = y_coordinate

	def draw(self):
		print("drawing....")

	def display(self):
		print("displaying....")

line1 = lines(2, 3, 3)
print(line1.length)