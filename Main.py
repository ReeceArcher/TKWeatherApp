import tkinter as tk
import ttkbootstrap as ttk
from Weather import get_weather_data, output_weather_data


#
# Python on script that is used to build a GUI
# to display data from a weather API
# Built on 12/22/23 @2030
#


# Function to handle button click
def on_submit():
    city = entry.get()  # Gets the city name entered by user
    weather_data = get_weather_data(city)  # Gets the weather data from entered city
    display_weather_data(weather_data)  # Displays the weather data in TKinter GUI


# Function to display weather data in TKiner GUI
def display_weather_data(data):
    weather_info = output_weather_data(data)  # Gets the formatted weather data

    # Checks for errors
    if "Error" in weather_info:
        # Display error message if one is found
        output_label.config(text="Error something is wrong. Check city name or API key")  #todo would like it to display error if something is missing
    else:
        output_label.config(text="\n".join(weather_info.values()))  # Updates the TKinter label with weather data


# Window set up
window = ttk.Window()
window.title("Weather App")
window.geometry("550x500")
window.config(bg="light steel blue")
window.resizable(width=False, height=False)


# Window title
title_label = tk.Label(master=window, text="Enter a City", font="Calibri 20 ")
title_label.config(bg="light steel blue", pady=0)
title_label.pack()

# Input Field
input_frame = tk.Frame(master=window)
input_frame.config(bg="light steel blue")
input_frame.pack()

entry_string = tk.StringVar(master=input_frame)
entry = tk.Entry(master=input_frame, textvariable=entry_string)
entry.pack(side="top", pady=7)

# Button
button = ttk.Button(master=input_frame, text="Submit", command=on_submit)
button.pack(side="top")

# Output
# todo use the information from weather API for output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text="",
    font="Calibri 20",
    background="light steel blue")
output_label.pack()

# Run
window.mainloop()
