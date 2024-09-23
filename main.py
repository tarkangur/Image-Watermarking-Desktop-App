import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

window = tk.Tk()
window.config(padx=50, pady=50, bg="white")
window.title("Image Watermarking App")
window.geometry("3000x900")
img = None
original_img = None


def UploadAction():
    global img, original_img
    file_types = [("Jpg Files", "*.jpg"), ("PNG Files", "*.png")]
    filename = filedialog.askopenfilename(filetypes=file_types)
    if filename:
        original_img = Image.open(filename)
        if original_img.height >= window.winfo_height() or original_img.width >= window.winfo_width():
            width = window.winfo_width() - 100
            height = window.winfo_height() - 100
            original_img = original_img.resize((width, height))

        img = ImageTk.PhotoImage(original_img)
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

    def apply_watermark():
        global img, original_img
        if original_img:
            draw = ImageDraw.Draw(original_img)
            text = watermark_text.get()
            size = font_size.get()

            font = ImageFont.truetype("arial.ttf", size)

            text_position = (original_img.width // 2, original_img.height // 2)
            draw.text(text_position, text, font=font, fill=(255, 255, 255, 128))

            img = ImageTk.PhotoImage(original_img)
            label_photo.config(image=img)
            label_photo.image = img

            watermark_window.destroy()

    apply_button = tk.Button(watermark_window, text="Apply Watermark", command=apply_watermark)
    apply_button.pack(pady=10)


def SaveFile():
    global original_img
    file_types = [("Jpg Files", "*.jpg"), ("PNG Files", "*.png")]
    if original_img:
        path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=file_types)
        if path:
            original_img.save(path)


menu = tk.Menu(window)
window.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='Menu', menu=filemenu)

filemenu.add_command(label='Open Picture', command=UploadAction)
filemenu.add_command(label='Add Watermark', command=AddWatermark)
filemenu.add_command(label='Save', command=SaveFile)

filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)


label_photo = tk.Label(window, bg="white")
label_photo.pack()


window.mainloop()
