#GUI

import tkinter as tk
from tkinter import font
import main

# Colors
BG_COLOR        = "#233d4d"
FRAME_COLOR     = "#233d4d"
TEXT_COLOR      = "#F0EDE5"
ACCENT_COLOR    = "#fe7f2d"

#Header
root = tk.Tk()
root.title("ArgandX - Your Complex Plane Plotter")
root.geometry("520x700")
root.configure(bg=BG_COLOR)
main_font = font.Font(family="Segoe UI", size=10)

#Canvas and Scroll bar
canvas = tk.Canvas(root, bg=BG_COLOR, highlightthickness=0, bd=0)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

scrollable_frame = tk.Frame(canvas, bg=BG_COLOR)
window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

def resize_frame(event):
    canvas.itemconfig(window, width=event.width)

canvas.bind("<Configure>", resize_frame)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# GUI elements
tk.Label(scrollable_frame, text="ArgandX", font=("Segoe UI", 22, "bold"), bg=BG_COLOR, fg=ACCENT_COLOR).pack(pady=20)

input_frame = tk.LabelFrame(scrollable_frame, text=" Input Complex Number ", bg=FRAME_COLOR, fg=TEXT_COLOR, font=main_font, padx=15, pady=10)
input_frame.pack(padx=20, pady=10, fill="x")

tk.Label(input_frame, text="Real Part:", bg=FRAME_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, sticky="w")
entry_real = tk.Entry(input_frame, width=15, font=main_font)
entry_real.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Imaginary Part:", bg=FRAME_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, sticky="w")
entry_imag = tk.Entry(input_frame, width=15, font=main_font)
entry_imag.grid(row=1, column=1, padx=5, pady=5)

tk.Button(input_frame, text="Add Number", command=main.add_number,
          bg="#fe7f2d", fg="white",
          font=("Segoe UI", 9, "bold"), width=15).grid(row=0, column=2, rowspan=2, padx=10)

list_frame = tk.Frame(scrollable_frame, bg=BG_COLOR)
list_frame.pack(padx=20, pady=10, fill="both")
tk.Label(list_frame, text="Stored Numbers List:", bg=BG_COLOR, fg=TEXT_COLOR).pack(anchor="w")
listbox_numbers = tk.Listbox(list_frame, height=5, font=("Consolas", 10),
                             bg="#2c3e50", fg="#34e7e4",
                             borderwidth=0, highlightthickness=1)
listbox_numbers.pack(fill="both", pady=5)

ops_frame = tk.LabelFrame(scrollable_frame, text=" Operations ", bg=FRAME_COLOR, fg=TEXT_COLOR, font=main_font, padx=10, pady=10)
ops_frame.pack(padx=20, pady=10, fill="x")

btn_configs = [('Addition', 'add'), ('Subtraction', 'sub'), ('Multiplication', 'mul'),
               ('Division', 'div'), ('Modulus', 'mod'), ('Argument', 'arg'), ('Conjugate', 'conj')]

for i, (text, mode) in enumerate(btn_configs):
    tk.Button(ops_frame, text=text, width=12,
              command=lambda m=mode: main.perform_op(m),
              bg="#fe7f2d", fg="white",
              activebackground="#f4a261",
              activeforeground="white",
              font=("Segoe UI", 9, "bold"),
              relief="flat").grid(row=i//3, column=i%3, padx=5, pady=5)

rot_frame = tk.LabelFrame(scrollable_frame, text=" Rotation ", bg=FRAME_COLOR, fg=TEXT_COLOR, font=main_font, padx=10, pady=10)
rot_frame.pack(padx=20, pady=10, fill="x")
tk.Label(rot_frame, text="Angle (degrees):", bg=FRAME_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, sticky="w")
entry_angle = tk.Entry(rot_frame, width=15, font=main_font)
entry_angle.grid(row=0, column=1, padx=5)
tk.Button(rot_frame, text="Rotate Last Number", command=main.rotate_selected,
          bg="#fe7f2d", fg="white", font=("Segoe UI", 9, "bold")).grid(row=0, column=2, padx=10)

scale_frame = tk.LabelFrame(scrollable_frame, text=" Scaling ", bg=FRAME_COLOR, fg=TEXT_COLOR, font=main_font, padx=10, pady=10)
scale_frame.pack(padx=20, pady=10, fill="x")
tk.Label(scale_frame, text="Scale Factor (k):", bg=FRAME_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, sticky="w")
entry_scale = tk.Entry(scale_frame, width=15, font=main_font)
entry_scale.grid(row=0, column=1, padx=5)
tk.Button(scale_frame, text="Scale Last Number", command=main.scale_selected,
          bg="#fe7f2d", fg="white", font=("Segoe UI", 9, "bold")).grid(row=0, column=2, padx=10)

lbl_result = tk.Label(scrollable_frame, text="Result: (Waiting...)", font=("Segoe UI", 11, "bold"), bg=BG_COLOR, fg="#f1c40f", wraplength=400)
lbl_result.pack(pady=15)

tk.Button(scrollable_frame, text="DISPLAY ARGAND PLOT", command=main.show_plot,
          bg="#fe7f2d", fg="black",
          activebackground="#f4a261", activeforeground="black",
          font=("Segoe UI", 11, "bold"), height=2, relief="flat").pack(fill="x", padx=40, pady=5)

tk.Button(scrollable_frame, text="RESET ALL DATA", command=main.clear_all,
          bg="#fe7f2d", fg="black",
          activebackground="#f4a261", activeforeground="black",
          font=("Segoe UI", 9, "bold"), relief="flat", width=20).pack(pady=10)

# Connect GUI widgets to logic
main.entry_real = entry_real
main.entry_imag = entry_imag
main.listbox_numbers = listbox_numbers
main.lbl_result = lbl_result
main.entry_angle = entry_angle
main.entry_scale = entry_scale

root.mainloop()