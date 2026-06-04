#Main Logic

import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox

# Numbers storage
numbers = []

# GUI widgets placeholders
entry_real = None
entry_imag = None
listbox_numbers = None
lbl_result = None
entry_angle = None
entry_scale = None

#Functions

#Adding a number to the list
def add_number():
    try:
        re = float(entry_real.get())
        im = float(entry_imag.get())
        z = re + im*1j
        numbers.append(z)
        listbox_numbers.insert("end", f"  {len(numbers)}.  {z}")
        entry_real.delete(0, "end")
        entry_imag.delete(0, "end")
    except ValueError:
        messagebox.showerror("Input Error", "Enter valid numbers for Real and Imaginary parts.")

#Resetting
def clear_all():
    if messagebox.askyesno("Reset", "Are you sure you want to clear all data?"):
        numbers.clear()
        listbox_numbers.delete(0, "end")
        lbl_result.config(text="Result: (Waiting...)")

#Plotter
def show_plot():
    if not numbers:
        messagebox.showwarning("No Data", "Add numbers to visualize!")
        return

    plt.figure(figsize=(6, 6))
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    original_plotted = False
    rotated_plotted = False

    for i, z in enumerate(numbers):
        if "rotated" in listbox_numbers.get(i):
            color = 'green'
            label = "Rotated Vector"
            if not rotated_plotted:
                plt.quiver(0, 0, z.real, z.imag, angles='xy', scale_units='xy', scale=1, color=color, width=0.008, label=label)
                rotated_plotted = True
            else:
                plt.quiver(0, 0, z.real, z.imag, angles='xy', scale_units='xy', scale=1, color=color, width=0.008)
        else:
            color = 'blue'
            label = "Original Vector"
            if not original_plotted:
                plt.quiver(0, 0, z.real, z.imag, angles='xy', scale_units='xy', scale=1, color=color, width=0.008, label=label)
                original_plotted = True
            else:
                plt.quiver(0, 0, z.real, z.imag, angles='xy', scale_units='xy', scale=1, color=color, width=0.008)
        plt.scatter(z.real, z.imag, color=color)

    limit = max(max(abs(z.real) for z in numbers), max(abs(z.imag) for z in numbers), 5) + 1
    plt.xlim(-limit, limit)
    plt.ylim(-limit, limit)

    plt.title("ArgandX – Rotation/Scaling Visualization", fontsize=14, fontweight='bold')
    plt.xlabel("Real Axis")
    plt.ylabel("Imaginary Axis")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()

#Rotation
def rotate_selected():
    if not numbers:
        messagebox.showwarning("No Data", "Add a complex number first.")
        return

    angle_text = entry_angle.get().strip()
    if angle_text == "":
        messagebox.showerror("Input Error", "Please enter a rotation angle.")
        return

    try:
        angle_deg = float(angle_text)
    except ValueError:
        messagebox.showerror("Input Error", "Angle must be a number (e.g., 45)")
        return

    z = numbers[-1]
    theta = np.radians(angle_deg)
    z_rot = z * (np.cos(theta) + 1j * np.sin(theta))

    numbers.append(z_rot)
    listbox_numbers.insert("end", f"{len(numbers)}. {z_rot} (rotated)")
    lbl_result.config(text=f"Rotation Result\nOriginal: {z}\nAngle: {angle_deg}°\nRotated: {round(z_rot.real,2)} + {round(z_rot.imag,2)}i")

#Scaling
def scale_selected():
    if not numbers:
        messagebox.showwarning("No Data", "Add a complex number first.")
        return

    scale_text = entry_scale.get().strip()
    if scale_text == "":
        messagebox.showerror("Input Error", "Please enter a scale factor.")
        return

    try:
        k = float(scale_text)
    except ValueError:
        messagebox.showerror("Input Error", "Scale factor must be a number.")
        return

    z = numbers[-1]
    z_scaled = k * z

    numbers.append(z_scaled)
    listbox_numbers.insert("end", f"{len(numbers)}. {z_scaled} (scaled)")
    lbl_result.config(text=f"Scaling Result\nOriginal: {z}\nScale Factor: {k}\nScaled: {round(z_scaled.real,2)} + {round(z_scaled.imag,2)}i")

#Arithmetic operations
def perform_op(op_type):
    if not numbers:
        return
    if len(numbers) < 2 and op_type in ['add', 'sub', 'mul', 'div']:
        messagebox.showwarning("Need More Data", "Please add at least 2 numbers.")
        return

    if op_type == 'add':
        res = sum(numbers)
    elif op_type == 'sub':
        res = numbers[0]
        for z in numbers[1:]:
            res -= z
    elif op_type == 'mul':
        res = np.prod(numbers)
    elif op_type == 'div':
        try:
            res = numbers[0]
            for z in numbers[1:]:
                res /= z
        except ZeroDivisionError:
            res = "Cannot divide by zero!"
    elif op_type == 'mod':
        res = [round(abs(z), 2) for z in numbers]
    elif op_type == 'arg':
        res = [round(np.degrees(np.angle(z)) % 360, 2) for z in numbers]
    elif op_type == 'conj':
        res = [z.conjugate() for z in numbers]

    lbl_result.config(text=f"Result: {res}")