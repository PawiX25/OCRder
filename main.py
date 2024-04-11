import pytesseract
from PIL import ImageGrab
import customtkinter as ctk

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Set the appearance mode and color theme
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Create a function to perform OCR on the screenshot
def perform_ocr(bbox):
    # Capture the screen
    screenshot = ImageGrab.grab(bbox)

    # Convert the screenshot to grayscale
    screenshot = screenshot.convert('L')

    # Perform OCR on the screenshot
    text = pytesseract.image_to_string(screenshot)

    # Update the text in the GUI
    text_label.config(text=text)

# Create a function to select the area of the screen to capture
def select_area():
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

    # Create an invisible rectangle
    rectangle = canvas.create_rectangle(0, 0, 0, 0)

    # Bind the mouse events
    canvas.bind('<B1-Motion>', update_rectangle)
    canvas.bind('<ButtonRelease-1>', end_selection)

# Create the GUI window
window = ctk.CTk()
window.title("OCRder")

# Create a button to trigger OCR
ocr_button = ctk.CTkButton(window, text="Perform OCR", command=select_area)
ocr_button.pack()

# Create a label to display the extracted text
text_label = ctk.CTkLabel(window, text="")
text_label.pack()

# Start the GUI event loop
window.mainloop()