import tkinter as tk

root = tk.Tk()

photo = tk.PhotoImage(file='rocket_body.png')
canvas = tk.Canvas()
canvas.create_image(0, 0, image=photo)
canvas.image = photo
canvas.grid()

root.mainloop()