# OCRder

OCRder is a Python application that performs Optical Character Recognition (OCR) on a selected area of the screen and displays the extracted text in a graphical user interface (GUI). The extracted text can also be saved to a file.

## Installation

1. Clone this repository.
2. Install the required Python libraries using pip:

```bash
pip install pytesseract pillow customtkinter keyboard
```

3. Download and install Tesseract OCR from [here](https://github.com/UB-Mannheim/tesseract/wiki). Make sure to add Tesseract to your system's PATH.

## Usage

1. Run the `main.py` file using Python.
2. The OCRder GUI window will appear.
3. Click the "Perform OCR" button or press the hotkey (Windows+Shift+X) to select an area of the screen to capture.
4. The selected area will be processed using OCR, and the extracted text will be displayed in the GUI.
5. Click the "Save" button to save the extracted text to a file. You will be prompted to choose a file location and enter a file name.

## Customization

- You can customize the appearance mode and color theme of the GUI by modifying the `set_appearance_mode` and `set_default_color_theme` functions.
- The default appearance mode is "System" and the default color theme is "blue".
- You can change the hotkey for selecting the area by modifying the `keyboard.add_hotkey` function.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- Thanks to the pytesseract library for making OCR in Python easy!

## Troubleshooting

If you encounter any issues while running OCRder, make sure you have all the dependencies installed correctly and that the Tesseract OCR path is set correctly.

If you have any questions or need further assistance, please feel free to open an issue on GitHub.

Happy OCRing!
