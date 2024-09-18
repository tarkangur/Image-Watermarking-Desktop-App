import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

window = tk.Tk()
window.config(padx=50, pady=50, bg="white")
window.title("Image Watermarking App")
img = None


def UploadAction():
    global img
    file_types = [("Jpg Files", "*.jpg"), ("PNG Files", "*.png")]
    filename = filedialog.askopenfilename(filetypes=file_types)
    if filename:
        img = Image.open(filename)
        img = ImageTk.PhotoImage(img)

        window.bind("<Configure>")
        label_photo.config(image=img)
        label_photo.image = img


upload_button = tk.Button(window, text="Upload Image", command=UploadAction)
upload_button.pack(side=tk.BOTTOM)

label_photo = tk.Label(window)
label_photo.pack()


window.mainloop()




