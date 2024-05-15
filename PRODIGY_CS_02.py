from PIL import Image

def encrypt_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    encrypted_pixels = []

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            # Example of a simple mathematical operation
            encrypted_pixel = tuple((p + 50) % 256 for p in pixel)
            encrypted_pixels.append(encrypted_pixel)

    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    decrypted_pixels = []

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            # Example of reversing the mathematical operation for decryption
            decrypted_pixel = tuple((p - 50) % 256 for p in pixel)
            decrypted_pixels.append(decrypted_pixel)

    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully!")

def main():
    image_path = input("Enter the path to the image file: ")
    choice = input("Enter 'E' to encrypt or 'D' to decrypt the image: ").upper()

    if choice == 'E':
        encrypt_image(image_path)
    elif choice == 'D':
        decrypt_image(image_path)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
