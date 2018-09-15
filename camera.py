import os
from subprocess import call
import v4l2 

class Camera:
	def __init__(self):
		pass

	def capture(self, resolution, name, format):
		call(["fswebcam", "-r", resolution, "--no-banner", "../../images/" + name + "." + format])

	def remove(self, file):
		if os.path.isfile(file):
			os.remove(file)
			return 0
		else:
			return -1

	def teste(self):
		return 