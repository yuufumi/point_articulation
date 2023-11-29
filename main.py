import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

# Create a label for the image
image_label = tk.Label(root)

# Load the image
image = Image.open("test.gz.pdf")
resized_image = image.resize((200, 200), Image.ANTIALIAS)
photo_image = ImageTk.PhotoImage(resized_image)

# Set the image as the label's image
image_label.config(image=photo_image)

# Create a text field
text_field = tk.Entry(root)

# Create a button
button = tk.Button(root, text="Submit")

# Layout the widgets
image_label.pack(side=tk.TOP)
text_field.pack(side=tk.LEFT)
button.pack(side=tk.RIGHT)

# Start the main loop
root.mainloop()