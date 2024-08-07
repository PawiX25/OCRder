import pytesseract
from PIL import ImageGrab
import customtkinter as ctk
from customtkinter import filedialog
import keyboard
import time
import os
import sys
import logging
import pyperclip

# Initialize logging
logging.basicConfig(filename='ocrder.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# If running the bundled app, find the Tesseract OCR engine in the current directory
if getattr(sys, 'frozen', False):
    pytesseract.pytesseract.tesseract_cmd = os.path.join(sys._MEIPASS, 'Tesseract-OCR', 'tesseract.exe')
# If running the script directly, find the Tesseract OCR engine in the specified directory
else:
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Set the appearance mode and color theme
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Create a function to perform OCR on the screenshot
def perform_ocr(bbox):
    start_time = time.time()  # Record the start time
    try:
        # Capture the screen
        screenshot = ImageGrab.grab(bbox)

        # Convert the screenshot to grayscale
        screenshot = screenshot.convert('L')

        # Perform OCR on the screenshot
        text = pytesseract.image_to_string(screenshot)

        # Update the text in the GUI
        text_label.configure(text=text)

        # Copy text to clipboard
        pyperclip.copy(text)

        # Show the "Save" button
        save_button.pack()
    except Exception as e:
        # Handle the OCR error
        logging.error("OCR Error: " + str(e))
        text_label.configure(text="OCR Error: " + str(e))
    finally:
        end_time = time.time()  # Record the end time
        processing_time = end_time - start_time  # Calculate the processing time
        window.title(f"OCRder - Processing Time: {processing_time:.2f} seconds")  # Update the window title

# Create a function to select the area of the screen to capture
def select_area():
    try:
        # Create a new fullscreen and transparent window
        selection_window = ctk.CTkToplevel(window)
        selection_window.attributes('-fullscreen', True, '-alpha', 0.3)

        # Create a canvas to draw the selection rectangle
        canvas = ctk.CTkCanvas(selection_window)
        canvas.pack(fill='both', expand=True)

        # Initialize the starting coordinates
        start_x, start_y = None, None

        # Function to update the selection rectangle
        def update_rectangle(event):
            nonlocal start_x, start_y
            # Set the starting coordinates when the mouse is first clicked
            if start_x is None and start_y is None:
                start_x, start_y = event.x, event.y
            # Update the rectangle
            canvas.coords(rectangle, start_x, start_y, event.x, event.y)

        # Function to end the selection
        def end_selection(event):
            try:
                # Get the bounding box coordinates
                left, upper, right, lower = start_x, start_y, event.x, event.y

                # Ensure 'right' is greater than 'left' and 'lower' is greater than 'upper'
                if right < left:
                    left, right = right, left
                if lower < upper:
                    upper, lower = lower, upper

                bbox = (left, upper, right, lower)

                # Perform OCR on the selected area
                perform_ocr(bbox)

                # Close the selection window
                selection_window.destroy()
            except Exception as e:
                # Handle the selection error
                logging.error("Selection Error: " + str(e))
                text_label.configure(text="Selection Error: " + str(e))

        # Create an invisible rectangle
        rectangle = canvas.create_rectangle(0, 0, 0, 0)

        # Bind the mouse events
        canvas.bind('<B1-Motion>', update_rectangle)
        canvas.bind('<ButtonRelease-1>', end_selection)
    except Exception as e:
        # Handle the selection window creation error
        logging.error("Selection Window Error: " + str(e))
        text_label.configure(text="Selection Window Error: " + str(e))

def save_to_file():
    # Ask the user where to save the file
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    if filename:
        try:
            # Open the file in write mode and write the contents of text_label to it
            with open(filename, 'w') as file:
                file.write(text_label.cget("text"))
        except Exception as e:
            # Handle file saving error
            logging.error("File Saving Error: " + str(e))
            text_label.configure(text="File Saving Error: " + str(e))

# Create the GUI window
window = ctk.CTk()
window.title("OCRder")

# Create a button to trigger OCR
ocr_button = ctk.CTkButton(window, text="Perform OCR", command=select_area)
ocr_button.pack()

# Create a button to save the OCR results
save_button = ctk.CTkButton(window, text="Save", command=save_to_file)
save_button.pack()
save_button.pack_forget()  # Hide the button initially

# Create a label to display the extracted text
text_label = ctk.CTkLabel(window, text="")
text_label.pack()

# Bind the hotkey to the select_area function
keyboard.add_hotkey('windows+shift+x', select_area)

# Start the GUI event loop
window.mainloop()