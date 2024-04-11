import pytesseract
from PIL import ImageGrab

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Capture the screen
screenshot = ImageGrab.grab()

# Convert the screenshot to grayscale
screenshot = screenshot.convert('L')

# Perform OCR on the screenshot
text = pytesseract.image_to_string(screenshot)

# Print the extracted text
print(text)