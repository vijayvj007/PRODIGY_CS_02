# #Simple Image Encryption Tool

This project is a simple image encryption tool that utilizes pixel manipulation techniques to encrypt and decrypt images. Users can perform operations such as swapping pixel values or applying basic mathematical operations to each pixel to achieve encryption.

## Features

- Encrypt images by manipulating pixel values.
- Decrypt images by reversing the pixel manipulation process.
- Supports common image formats such as PNG and JPEG.
- Easy-to-use command-line interface.

## Requirements

- Python 3.x
- `Pillow` library for image processing

## Installation

1. Clone the repository or download the script to your local machine.

2. Install the required dependencies using pip:

   ```bash
   pip install pillow
   ```

## Usage

1. Run the script using Python:

   ```bash
   python image_encryption.py
   ```

2. Follow the on-screen prompts to select an image, choose an operation (encrypt or decrypt), and provide any necessary parameters (e.g., a key for encryption).

## Example

### Encryption

```
Enter the path to the image: example.png
Enter the encryption key (an integer): 1234

Encrypted image saved as: encrypted_example.png
```

### Decryption

```
Enter the path to the encrypted image: encrypted_example.png
Enter the decryption key (an integer): 1234

Decrypted image saved as: decrypted_example.png
```

## Code

Here's the Python code for the image encryption tool:

```python
from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)
    
    np.random.seed(key)
    encrypted_pixels = pixels.copy()
    np.random.shuffle(encrypted_pixels.flat)
    
    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save('encrypted_' + image_path)
    print(f'Encrypted image saved as: encrypted_{image_path}')

def decrypt_image(encrypted_image_path, key):
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_pixels = np.array(encrypted_image)
    
    np.random.seed(key)
    index_array = np.arange(encrypted_pixels.size)
    np.random.shuffle(index_array)
    
    decrypted_pixels = np.empty_like(encrypted_pixels.flat)
    decrypted_pixels[index_array] = encrypted_pixels.flat
    decrypted_pixels = decrypted_pixels.reshape(encrypted_pixels.shape)
    
    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save('decrypted_' + encrypted_image_path)
    print(f'Decrypted image saved as: decrypted_{encrypted_image_path}')

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? (e/d): ").lower()
        if choice in ['e', 'd']:
            image_path = input("Enter the path to the image: ")
            key = int(input("Enter the key (an integer): "))
            if choice == 'e':
                encrypt_image(image_path, key)
            else:
                decrypt_image(image_path, key)
        else:
            print("Invalid choice. Please select 'e' to encrypt or 'd' to decrypt.")
        
        another = input("Do you want to encrypt/decrypt another image? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This tool is inspired by basic principles of image processing and encryption techniques. Special thanks to the developers of the `Pillow` library for making image manipulation in Python straightforward and efficient.
