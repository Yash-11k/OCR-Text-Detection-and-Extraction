import cv2
import pytesseract

# Tell Python where Tesseract is installed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image_path):
    """
    Reads an image and extracts text using Tesseract OCR.
    """

    # Read image using OpenCV
    image = cv2.imread(image_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extract text
    text = pytesseract.image_to_string(gray)

    return text


# Test OCR directly
if __name__ == "__main__":

    result = extract_text("uploads/sample.jpg")

    print(result)