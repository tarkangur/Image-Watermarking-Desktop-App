import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

window = tk.Tk()
window.config(padx=50, pady=50, bg="white")
window.title("Image Watermarking App")
window.geometry("3000x900")
img = None


def UploadAction():
    global img
    file_types = [("Jpg Files", "*.jpg"), ("PNG Files", "*.png")]
    filename = filedialog.askopenfilename(filetypes=file_types)
    if filename:
        img = Image.open(filename)
        if img.height >= window.winfo_height() or img.width >= window.winfo_width():
            width = window.winfo_width() - 100
            height = window.winfo_height() - 100
            img = img.resize((width, height))

        img = ImageTk.PhotoImage(img)
        window.bind("<Configure>")
        label_photo.config(image=img)
        label_photo.image = img


def AddWatermark():
    watermark_window = tk.Toplevel(window)
    watermark_window.title("Add Watermark")

    tk.Label(watermark_window, text="Enter Watermark Text:").pack(pady=10)
    watermark_text = tk.Entry(watermark_window, width=30)
    watermark_text.pack(pady=10)

    tk.Label(watermark_window, text="Set Font Size:").pack(pady=10)
    font_size = tk.Scale(watermark_window, from_=10, to=100, orient=tk.HORIZONTAL)
    font_size.pack(pady=10)


menu = tk.Menu(window)
window.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='Menu', menu=filemenu)

filemenu.add_command(label='Open Picture', command=UploadAction)
filemenu.add_command(label='Add Watermark', command=AddWatermark)
filemenu.add_command(label='Save')

filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)


label_photo = tk.Label(window, bg="white")
label_photo.pack()


window.mainloop()
