import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def UploadAction():
    file_types = [("Jpg Files", "*.jpg"), ("PNG Files", "*.png")]
    filename = filedialog.askopenfilename(filetypes=file_types)
    if filename:
        print("Selected file:", filename)
        img = Image.open(filename)
        img_width, img_height = img.size
        canvas.config(width=img_width, height=img_height)
        img = ImageTk.PhotoImage(img)
        canvas.create_image(img_width // 2, img_height // 2, image=img)
        canvas.image = img


window = tk.Tk()
window.config(padx=50, pady=50, bg="white")
window.title("Image Watermarking App")

upload_button = tk.Button(window, text="Upload Image", command=UploadAction)
upload_button.grid(column=1, row=1, pady=100)

canvas = tk.Canvas(window, bg="white", highlightthickness=0)
canvas.grid(column=1, row=0)


window.mainloop()
