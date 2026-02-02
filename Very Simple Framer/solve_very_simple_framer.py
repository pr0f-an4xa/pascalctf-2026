from PIL import Image

def binary_to_message(binary_str):
    # Split the binary string into 8-bit chunks and convert to characters
    message = ""
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        if len(byte) < 8:
            break
        message += chr(int(byte, 2))
    return message

def extract_message(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    width, height = img.size

    # Reconstruct the clockwise border coordinates used in chal.py
    coords = []
    # Top edge
    for x in range(width):
        coords.append((x, 0))
    # Right edge
    for y in range(1, height-1):
        coords.append((width-1, y))
    # Bottom edge
    if height > 1:
        for x in range(width-1, -1, -1):
            coords.append((x, height-1))
    # Left edge
    if width > 1:
        for y in range(height-2, 0, -1):
            coords.append((0, y))

    # Extract bits: Black = '0', White = '1'
    binary_str = ""
    for coord in coords:
        pixel = img.getpixel(coord)
        # Check if the pixel is closer to white or black
        if pixel[0] > 128:
            binary_str += '1'
        else:
            binary_str += '0'
            
    return binary_to_message(binary_str)

# Usage
result = extract_message("output.jpg")
print(result)