from selenium import webdriver

def get_ownership_info(pin):
    # Create a webdriver object and navigate to the website
    driver = webdriver.Chrome()
    driver.get('https://example.com/')

    # Find the input field for the PIN and enter the PIN
    pin_input = driver.find_element_by_id('pin-input')
    pin_input.send_keys(pin)

    # Find the submit button and click it
    submit_button = driver.find_element_by_id('submit-button')
    submit_button.click()

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Find the element containing the ownership information
    ownership_info_element = driver.find_element_by_id('ownership-info')

    # Extract the ownership information from the element
    ownership_info = ownership_info_element.text

    # Close the webdriver
    driver.close()

    return ownership_info

class ParcelInfoGUI:
    def __init__(self):
        # Create the main window
        self.window = QWidget()
        self.window.setWindowTitle('Parcel Ownership Information')

        # Create input fields for the user to enter the PIN and other relevant information
        self.pin_label = QLabel('Enter the PIN:', self.window)
        self.pin_input = QLineEdit(self.window)

        # Create a button for the user to submit the request
        self.submit_button = QPushButton('Submit', self.window)
        self.submit_button.clicked.connect(self.get_ownership_info)

        # Create a label to display the ownership information
        self.ownership_info_label = QLabel('', self.window)

        # Show the window
        self.window.show()

    def get_ownership_info(self):
        # Get the PIN from the user input
        pin = self.pin_input.text()

        # Call the function to get the ownership information using Selenium
        ownership_info = get_ownership_info(pin)

        # Update the label with the ownership information
        self.ownership_info_label.setText(ownership_info)

app = QApplication([])
gui = ParcelInfoGUI()
app.exec_()