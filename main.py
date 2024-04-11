import pytesseract
from PIL import ImageGrab
import tkinter as tk

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Create a function to perform OCR on the screenshot
def perform_ocr():
    # Capture the screen
    screenshot = ImageGrab.grab()

    # Convert the screenshot to grayscale
    screenshot = screenshot.convert('L')

    # Perform OCR on the screenshot
    text = pytesseract.image_to_string(screenshot)

    # Update the text in the GUI
    text_label.config(text=text)

# Create the GUI window
window = tk.Tk()
window.title("OCRder")

# Create a button to trigger OCR
ocr_button = tk.Button(window, text="Perform OCR", command=perform_ocr)
ocr_button.pack()

# Create a label to display the extracted text
text_label = tk.Label(window, text="")
text_label.pack()

# Start the GUI event loop
window.mainloop()