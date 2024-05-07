from tkinter import *
from tkinter import filedialog

root = Tk() #main window
root.geometry("300x200") #width X height
root.title("Image Encryptor/Decryptor") #title

def encrypt_image():
    perform_encryption(True) #wrapper

def decrypt_image():
    perform_encryption(False)

def perform_encryption(is_encrypt):
    file_path = filedialog.askopenfilename(filetypes=[('JPG files', '*.jpg')])
    if file_path:
        try:
            key = int(key_entry.get())
            with open(file_path, 'rb') as file:
                image_data = bytearray(file.read())
            # XOR operation for both encryption and decryption
            for index, value in enumerate(image_data):
                image_data[index] = value ^ key
            
            # Save the modified image
            with open(file_path, 'wb') as file:
                file.write(image_data)
            
            action = "Encrypted" if is_encrypt else "Decrypted"
            label_status.config(text=f"{action} Successfully")
        except ValueError:
            label_status.config(text="Invalid key. Please enter a number.")
        except Exception as e:
            label_status.config(text="Error: " + str(e))
        finally:
            # Clear the entry widget for the key after operation
            key_entry.delete(0, END)

label_key = Label(root, text="Enter Encryption Key (number):")
label_key.place(x=10, y=10)

key_entry = Entry(root)
key_entry.place(x=180, y=10)

encrypt_button = Button(root, text="Encrypt", command=encrypt_image)
encrypt_button.place(x=50, y=50)

decrypt_button = Button(root, text="Decrypt", command=decrypt_image)
decrypt_button.place(x=150, y=50)

label_status = Label(root, text="")
label_status.place(x=10, y=100)

root.mainloop()
