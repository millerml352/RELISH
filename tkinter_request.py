import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def get_ownership_info():
    parcel_id = parcel_id_entry.get()

    # Replace YOUR_DRIVER_PATH with the actual path to your webdriver
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(f'https://www.mohave.gov/ContentPage.aspx?id=111&cid=1402&parcel={parcel_id}')

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Find the element containing the ownership information
    ownership_info_element = driver.find_element_by_xpath('//*[@id="main-content"]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]')

    # Extract the text from the element and close the browser
    ownership_info = ownership_info_element.text
    driver.close()

    # Display the ownership information in a message box
    messagebox.showinfo('Ownership Information', ownership_info)

# Create the main window
root = tk.Tk()
root.title('Parcel Ownership Information Scraper')

# Add a label and text entry for the parcel ID
parcel_id_label = tk.Label(root, text='Enter the parcel ID:')
parcel_id_entry = tk.Entry(root)
parcel_id_label.pack()
parcel_id_entry.pack()

# Add a button to trigger the scraping
scrape_button = tk.Button(root, text='Scrape', command=get_ownership_info)
scrape_button.pack()

# Run the Tkinter event loop
root.mainloop()