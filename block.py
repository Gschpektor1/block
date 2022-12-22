class Block:
	
	def __init__(self, dimensions):
		self.dimensions = dimensions
		self.width = dimensions[0]
		self.length = dimensions[1]
		self.height = dimensions[2]

	def get_width():
		return self.width

	def get_length():
		return self.length

	def get_height():
		return self.height

	def get_volume():
		return self.length*self.width*self.height

	def get_surface_area():
		return (self.height*self.width)*6