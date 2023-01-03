import requests
from bs4 import BeautifulSoup
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

class ParcelInfoGUI:
    def __init__(self):
        # Create the main window
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle('Parcel Ownership Information')

        # Create a vertical layout to hold the widgets
        self.layout = QtWidgets.QVBoxLayout(self.window)

        # Set the layout's margin to 10 pixels
        self.layout.setContentsMargins(10, 10, 10, 10)

        # Create input fields for the user to enter the PIN and other relevant information
        self.pin_label = QtWidgets.QLabel('Enter the PIN:', self.window)
        self.pin_input = QtWidgets.QLineEdit(self.window)

        # Add the widgets to the layout
        self.layout.addWidget(self.pin_label)
        self.layout.addWidget(self.pin_input)

        # Create a button for the user to submit the request
        self.submit_button = QtWidgets.QPushButton('Submit', self.window)
        self.submit_button.clicked.connect(self.get_ownership_info)
        self.layout.addWidget(self.submit_button)

        # Create a label to display the ownership information
        self.ownership_info_label = QtWidgets.QLabel('', self.window)
        self.layout.addWidget(self.ownership_info_label)

        # Show the window
        self.window.show()

    def get_ownership_info(self):
        # Get the PIN from the user input
        pin = self.pin_input.text()

        # Send an HTTP request to the API or scrape the data from the website
        # using the PIN as a query parameter
        url = 'https://www.mohave.gov/ContentPage.aspx?id=111&cid=1402&parcel=' + pin
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Parse the response to get the ownership information
        ownership_name = soup.find('h5', {'id': 'parcelOwnerResult'}).text
        ownership_address = soup.find('h5', {'id': 'parcelMailingAddressResult'}).text

        # Update the label with the ownership information
        self.ownership_info_label.setText(ownership_name + ', ' + ownership_address)

app = QApplication([])
gui = ParcelInfoGUI()
app.exec_()