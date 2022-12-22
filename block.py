class Block:
	
	def __init__(self, dimensions):
		self.dimensions = dimensions
		self.width = dimensions[0]
		self.length = dimensions[1]
		self.height = dimensions[2]

	def get_width(self):
		return self.width

	def get_length(self):
		return self.length

	def get_height(self):
		return self.height

	def get_volume(self):
		return self.length*self.width*self.height

	def get_surface_area(self):
		return (self.height*self.width)*6