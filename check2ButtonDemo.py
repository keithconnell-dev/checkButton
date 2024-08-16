"""
check2ButtonDemo.py
**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

GUI-based app demonstrating the use of the checkbutton(checkbox) graphic component.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports can go here

# Class header (class name will change project to project)
class Check2ButtonDemo(EasyFrame):

	# Definition of our classes' constructor method
	def __init__(self):
		# Call to the Easy Frame class constructor
		EasyFrame.__init__(self, title = "Menu Options", width = 320, height = 200, resizable = False, background = "cadetblue1")

		#Add various components the window
		self.addLabel(text = "Today's Menu", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "cadetblue1", foreground = "darkviolet", font = Font(family = "Elephant", size = 28))

		#Add four check buttons
		self.chickCB = self.addCheckbutton(text = "Chicken", row = 1, column = 0)
		self.taterCB = self.addCheckbutton(text = "French Fries", row = 1, column = 1)
		self.beanCB = self.addCheckbutton(text = "Green Beans", row = 2, column = 0)
		self.sauceCB = self.addCheckbutton(text = "Applesauce", row = 2, column = 1)
		#Adjust the color of the checkbuttons
		self.chickCB["background"] = "cadetblue1"
		self.taterCB["background"] = "cadetblue1"
		self.beanCB["background"] = "cadetblue1"
		self.sauceCB["background"] = "cadetblue1"

		#Add the command button
		self.order = self.addButton(text = "Place Order", row = 3, column = 0, columnspan = 2,  command = self.placeOrder)
		self.order["background"] = "cyan"
		self.order["foreground"] = "purple"
		self.order["width"] = 24
		self.order["height"] = 2

	#Definition of the placeOrder() function
	def placeOrder(self):
		"""Display a message box with the order summary."""
		message = ""
		# Analyze each checkbutton to see if it has been selected
		if self.chickCB.isChecked():
			message += "Chicken\n\n"

		if self.taterCB.isChecked():
			message += "French Fries\n\n"

		if self.beanCB.isChecked():
			message += "Green Beans\n\n"

		if self.sauceCB.isChecked():
			message += "Applesauce\n\n"

		if message == "":
			message = "Sorry, no food was ordered!"

		#Now that we have looked at every checkbutton, let's push the message variable to a pop-up wondow
		self.messageBox(title = "Customer order", message = message)

# Global definition of the main() method
def main():
	# Instantiate an object from the class into mainloop()
	Check2ButtonDemo().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()