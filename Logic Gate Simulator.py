#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:57:12 2024

@author: smehta
"""

import tkinter as tk
from tkinter import ttk, messagebox


def calculate_output():
    try:

        selected_gate = gate_var.get()

        
        if selected_gate == "NOT":
            input1 = int(input1_var.get())
            if input1 not in (0, 1):
                raise ValueError("Invalid input for Input 1")
            output = 1 if input1 == 0 else 0
        
        else:
            
            input1 = int(input1_var.get())
            input2 = int(input2_var.get())
            
            if input1 not in (0, 1) or input2 not in (0, 1):
                raise ValueError("Please enter valid binary inputs (0 or 1)")

            
            if selected_gate == "AND":
                output = input1 & input2
            elif selected_gate == "OR":
                output = input1 | input2
            elif selected_gate == "NAND":
                output = 1 if not (input1 & input2) else 0
            elif selected_gate == "NOR":
                output = 1 if not (input1 | input2) else 0
            elif selected_gate == "XOR":
                output = input1 ^ input2
            elif selected_gate == "XNOR":
                output = 1 if input1 == input2 else 0
            else:
                output = "Invalid"

        
        output_var.set(f"Output: {output}")

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))


def update_inputs(event):
    selected_gate = gate_var.get()
    
    
    if selected_gate == "NOT":
        input2_entry.config(state="disabled")
        input2_var.set("") 
    else:
        input2_entry.config(state="normal")


root = tk.Tk()
root.title("Logic Gate Simulator")
root.geometry("300x300")


input1_var = tk.StringVar()
input2_var = tk.StringVar()
gate_var = tk.StringVar()
output_var = tk.StringVar(value="Output: ")


tk.Label(root, text="Input 1 (0 or 1):").pack(pady=5)
input1_entry = ttk.Entry(root, textvariable=input1_var)
input1_entry.pack()

tk.Label(root, text="Input 2 (0 or 1):").pack(pady=5)
input2_entry = ttk.Entry(root, textvariable=input2_var)
input2_entry.pack()


tk.Label(root, text="Select Logic Gate:").pack(pady=5)
gate_menu = ttk.Combobox(root, textvariable=gate_var,state="readonly")
gate_menu['values'] = ("AND", "OR", "NOT", "NAND", "NOR", "XOR", "XNOR")
gate_menu.current(0)
gate_menu.pack()


gate_menu.bind("<<ComboboxSelected>>", update_inputs)


calculate_button = ttk.Button(root, text="Calculate", command=calculate_output)
calculate_button.pack(pady=10)


output_label = ttk.Label(root, textvariable=output_var, font=("Helvetica", 12))
output_label.pack(pady=10)


root.mainloop()
