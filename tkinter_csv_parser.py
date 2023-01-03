import tkinter as tk
import csv

# Read data from the .csv file
data = []
with open('./data/parcel_ownership_noheader.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

# Get the column headers from the first row of the .csv file
# Hard-code the column headers
headers = ['PParcNum', 'OwnerFirst', 'OwnerLast', 'OwnerAddress1', 'OwnerAddress2', 'OwnerCity', 'OwnerState', 
    'OwnerZipCode', 'OwnerCountry', 'TrackingGUID', 'NewParcel', 'NewFirst', 'NewLast', 'NewAddr1', 'NewAddr2', 
    'NewCity', 'NewState', 'NewZipCode', 'NewCountry', 'NewGUID']

# Create the main window
window = tk.Tk()
window.title("Parcel Ownership Information")

# Add a label and a scrollbar
label = tk.Label(window, text="Parcel Ownership Information")
label.pack()
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Add a listbox and set its yscrollcommand to the scrollbar
listbox = tk.Listbox(window, yscrollcommand=scrollbar.set)
for row in data:
    listbox.insert(tk.END, row[0])
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox.yview)

# Add a frame to hold the labels and the selected values
selected_frame = tk.Frame(window)
selected_frame.pack()

# Add a label for each column
labels = []
for i in range(len(headers)):
    label = tk.Label(selected_frame, text=headers[i], anchor=tk.W)
    label.grid(row=i, column=0, sticky=tk.W)
    labels.append(label)

# Define a function to update the selected labels when the selection changes
def on_select(event):
    selection = event.widget.curselection()
    if len(selection) > 0:
        # Clear the previous data
        for i in range(len(headers)):
            labels[i].config(text=headers[i] + ": ")
        for widget in selected_frame.winfo_children():
            widget.destroy()

        # Display the newly selected data
        selected_index = selection[0]
        selected_row = data[selected_index]
        for i in range(len(selected_row)):
            label = tk.Label(selected_frame, text=headers[i] + ": ", anchor=tk.W)
            label.grid(row=i, column=0, sticky=tk.W)
            labels[i] = label
            tk.Label(selected_frame, text=selected_row[i], anchor=tk.W).grid(row=i, column=1, sticky=tk.W)

# Set the listbox's selectmode and bind the on_select function to the listbox's "<<ListboxSelect>>" event
listbox.config(selectmode=tk.SINGLE, exportselection=False)
listbox.bind("<<ListboxSelect>>", on_select)

# Run the main loop
window.mainloop()

# Things I need to figure out:
# 1. Why are we comparing data in the table to the assessor website when we just got the data from the assessor?
#    1a. Is it simply because there was a delay in receiving data from the assessor and when that data is to be
#        put into mailing materials so we want to ensure it is as up to date as possible?
#        - if so then this would need some kind of web scraping mechanism to check for accuracy at processing time
#        - otherwise this should be able to eventually compare old group data to newly received data just fine
#        - even if it can't process all of the county, a decent percentage of parcels have not changed hands and
#          could be bypassed
# 2. How to get old and new information into separate columns?
# 3. I want it to be both automated and have human eye visually apparent checks - like highlight row green if old
#    and new names match