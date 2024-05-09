# Image Encryption Decryption  

<p align="center">
  <img width=50% height=40% src="enc.gif" />  
  Image : Pen & Paper: Jocelyn Tsaih

</p>

This project is an image encryption/decryption application developed using Python and the Tkinter library for creating graphical user interfaces (GUIs). The application allows users to encrypt and decrypt image files (specifically JPG files) using a simple XOR encryption algorithm with a user-provided numerical key.

## Relevance of the Project

- **Image security**: Image encryption is an essential aspect of data security, ensuring that sensitive or confidential image data remains protected from unauthorized access.
- **Practical implementation**: This project provides a practical implementation of image encryption/decryption techniques, useful in various scenarios such as secure image transfer, privacy protection, or demonstrating encryption concepts.
- **Learning resource**: The project serves as a learning resource for understanding GUI development with Tkinter and implementing encryption algorithms in Python.

### Relevance

- This project demonstrates basic file handling, encryption/decryption techniques, and GUI development using Tkinter.
- It provides a practical application of encryption concepts, albeit in a simplified form, which can be educational for beginners.

## Individual Roles

- **Functionality development**: The main role within this project is to develop the functionality for encrypting and decrypting images.
- **GUI Design**: Designing the graphical user interface (GUI) elements such as buttons, labels, and entry widgets is crucial for user interaction.
- **Error handling and feedback**: Ensuring error handling and user feedback mechanisms are also part of the responsibilities.

## Innovation/Contribution

- **Advanced encryption algorithms**: One potential innovation could be the implementation of more advanced encryption algorithms beyond simple XOR, such as AES (Advanced Encryption Standard) or RSA (Rivest-Shamir-Adleman).
- **Enhanced GUI features**: Additionally, enhancing the GUI with more features like progress bars, image preview, or batch processing options could improve user experience.
- **Better error handling**: Implementing better error handling and validation mechanisms to handle various edge cases more gracefully can also be considered.

## Future Scope

- **Robust encryption algorithms**: Integration of more robust encryption algorithms for enhanced security.
- **Support for different image formats**: Adding support for different image formats beyond just JPG.
- **Password protection**: Implementing features like password protection for encrypted images.
- **Secure key generation and management**: Incorporating a feature to generate and manage encryption keys securely.
- **Batch processing**: Providing options for batch processing multiple images at once.
- **GUI enhancements**: Enhancing the GUI with more intuitive controls and visual feedback.

<!-- Here's a breakdown of the code:

1. `from tkinter import *`: This line imports all the available classes, functions, and constants from the Tkinter library. It's a common practice to import everything from Tkinter when working with GUIs.

2. `from tkinter import filedialog`: This line specifically imports the `filedialog` module from Tkinter. This module provides functions for creating file dialog boxes, which allow the user to select files or directories from their file system.

3. `root = Tk()`: This line creates the main window of the application. `Tk()` is a class in Tkinter that represents the main window.

4. `root.geometry("300x200")`: This line sets the initial size of the main window to 300 pixels wide and 200 pixels tall.

5. `root.title("Image Encryptor/Decryptor")`: This line sets the title of the main window to "Image Encryptor/Decryptor".

6. `def encrypt_image()`: This function is responsible for encrypting an image. However, it doesn't contain the actual encryption logic. Instead, it calls the `perform_encryption()` function with the argument True.

7. `def decrypt_image()`: This function is responsible for decrypting an image. Similar to the `encrypt_image()` function, it doesn't contain the actual decryption logic. Instead, it calls the `perform_encryption()` function with the argument False.

8. `file_path = filedialog.askopenfilename(filetypes=[('JPG files', '*.jpg')])`: This line opens a file dialog box that allows the user to select a JPG image file from their file system. The selected file path is stored in the `file_path` variable.

9. `if file_path:`: This checks if a file path was selected. If a file path was selected, the code inside the `try` block will execute.

10. `key = int(key_entry.get())`: This line retrieves the encryption/decryption key entered by the user in an entry widget (likely a text box) called `key_entry`. The key is converted from a string to an integer using the `int` function.

11. `with open(file_path, 'rb') as file:`: This line opens the selected image file in binary read mode.

12. `image_data = bytearray(file.read())`: This line reads the contents of the image file and stores it in a bytearray called `image_data`.

13. `for index, value in enumerate(image_data)`: This loop iterates over each byte in the `image_data` bytearray, with `index` representing the index of the byte and `value` representing the byte value.

14. `image_data[index] = value ^ key`: This line performs the XOR operation between each byte in `image_data` and the encryption/decryption key. The result is stored back in `image_data` at the same index, effectively encrypting (or decrypting) the byte.

15. `with open(file_path, 'wb') as file:`: This line opens the same image file in binary write mode.

16. `file.write(image_data)`: This line writes the modified (encrypted or decrypted) `image_data` back to the image file, overwriting the original contents.

17. `action = "Encrypted" if is_encrypt else "Decrypted"`: This line sets the `action` variable to either "Encrypted" or "Decrypted" based on the value of the `is_encrypt` parameter passed to the function.

18. `label_status.config(text=f"{action} Successfully")`: This line updates a label widget called `label_status` with the text indicating whether the image was successfully encrypted or decrypted.

19. The `except` blocks handle different types of exceptions that may occur during the encryption/decryption process, such as an invalid key (non-numeric input) or other exceptions. The error messages are displayed in the `label_status` widget.

20. In the `finally` block, `key_entry.delete(0, END)` clears the contents of the `key_entry` widget after the operation is completed, allowing the user to enter a new key for the next operation.
 
Good job.  
You've breached it.  

-->
