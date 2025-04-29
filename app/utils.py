import pytesseract
import cv2
import re

def extract_lab_tests(image_path):
    
    img = cv2.imread(image_path)

    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    
    text = pytesseract.image_to_string(thresh)

    
    lab_tests = []

    for line in text.split('\n'):
        
        match = re.match(r"(.+?)\s+([\d.]+)\s+([\d.-]+\s*-\s*[\d.-]+)", line)
        if match:
            name, value, ref_range = match.groups()
            min_val, max_val = [float(x.strip()) for x in ref_range.split('-')]

            
            lab_test_out_of_range = not (min_val <= float(value) <= max_val)

            lab_tests.append({
                "lab_test_name": name.strip(),
                "lab_test_value": value,
                "bio_reference_range": ref_range,
                "lab_test_out_of_range": lab_test_out_of_range
            })

    return lab_tests

