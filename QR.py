import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Function to generate a QR code (Encoder)
def generate_qr_code(data, file_name="qrcode.png"):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Size of each box in the QR code
        border=4,  # Thickness of the border
    )
    
    # Add the data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image of the QR code
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the QR code as an image
    img.save(file_name)
    print(f"QR Code saved as {file_name}")

# Function to decode a QR code (Decoder)
def decode_qr_code(file_name):
    # Open the image file
    img = Image.open(file_name)
    
    # Decode the QR code
    decoded_objects = decode(img)
    
    # If no QR code is found, return None
    if not decoded_objects:
        print("No QR code found in the image.")
        return None
    
    # Extract and print the decoded data from the QR code
    for obj in decoded_objects:
        print(f"Decoded data: {obj.data.decode('utf-8')}")
        return obj.data.decode('utf-8')

# Main function to run the encoder and decoder
def main():
    # Encoder
    data_to_encode = input("Enter the data to encode into a QR code: ")
    generate_qr_code(data_to_encode)
    
    # Decoder
    file_name = input("Enter the file name of the QR code to decode (e.g., qrcode.png): ")
    decoded_data = decode_qr_code(file_name)
    
    if decoded_data:
        print(f"Decoded QR code data: {decoded_data}")
    else:
        print("No data decoded.")

# Run the program
if __name__ == "__main__":
    main()
