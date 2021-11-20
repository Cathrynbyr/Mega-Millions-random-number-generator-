""" 
Program: Megamillions.py
Author: Cathryn Byrnes 11-19-21

*** Note: the files "breezypythongui.py" and "mega.jpg" MUST be in the same directory as the file in order for the application to work.***
"""

from breezypythongui import EasyFrame
import random
from tkinter.font import Font
from PIL import ImageTk

class MegaMillion(EasyFrame):


	def __init__(self):
		"""Sets up the window and the labels."""
		EasyFrame.__init__(self, title = "Mega Millions App", width = 420, height = 440, background = "blue", resizable = False)

		# Load the image and associate it with the image label
		imageLabel = self.addLabel(text = "", sticky = "NSEW", background  = "blue", row = 0, column = 0, columnspan = 5)
		self.image = ImageTk.PhotoImage(file = "mega.jpg")
		imageLabel["image"] = self.image

		# Title and logo
		titleFont = Font(family = "Arial", size = 16, weight = "bold")
		megaFont = Font(family = "Arial", size = 14, weight = "bold")
		self.titleLabel = self.addLabel(text = "NY STATE LOTTERY\nMEGA MILLIONS JACKPOT!", row = 1, column = 0, columnspan = 5, sticky = "NSEW", font = titleFont, background = "blue", foreground = "yellow")
		self.numField1 = self.addIntegerField(value = 0, row = 2, column = 0, sticky = "NSEW", state = "readonly")
		self.numField2 = self.addIntegerField(value = 0, row = 2, column = 1, sticky = "NSEW", state = "readonly")
		self.numField3 = self.addIntegerField(value = 0, row = 2, column = 2, sticky = "NSEW", state = "readonly")
		self.numField4 = self.addIntegerField(value = 0, row = 2, column = 3, sticky = "NSEW", state = "readonly")
		self.numField5 = self.addIntegerField(value = 0, row = 2, column = 4, sticky = "NSEW", state = "readonly")
		self.titleLabel = self.addLabel(text = "WINNING NUMBERS!", row = 3, column = 0, columnspan = 5, sticky = "NSEW", font = megaFont, background = "blue", foreground = "yellow")
		self.numField6 = self.addIntegerField(value = 0, row = 4, column = 2, sticky = "NSEW", state = "readonly")
		self.titleLabel = self.addLabel(text = "MEGA BALL!", row = 5, column = 0, columnspan = 5, sticky = "NSEW", font = megaFont, background = "blue", foreground = "yellow")

		# Command Button
		self.playButton = self.addButton(text = "Play Game!", row = 6, column = 0, columnspan = 5, command = self.play)
		self.playButton["background"] = "yellow"

	#Event Handling Method
	def play(self):
		# Variables and constants
		num1 = random.randint(1, 70)
		num2 = random.randint(1, 70)
		num3 = random.randint(1, 70)
		num4 = random.randint(1, 70)
		num5 = random.randint(1, 70)
		num6 = random.randint(1, 25)

		# Output phase
		self.numField1.setNumber(num1)
		self.numField2.setNumber(num2)
		self.numField3.setNumber(num3)
		self.numField4.setNumber(num4)
		self.numField5.setNumber(num5)
		self.numField6.setNumber(num6)

#definition of the main()function for program entry
def main():
	"""Instantiation and pops up the window."""
	MegaMillion().mainloop()

# global call to trigger the main()function
if __name__	== "__main__":
	main()

