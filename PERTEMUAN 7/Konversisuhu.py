import tkinter as tk
from tkinter import Variable,Label,Entry,Button,W

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert():
    try:
        if var.get() == 1:  # Celsius to Fahrenheit
            celsius_value = float(entry.get())
            result = celsius_to_fahrenheit(celsius_value)
            result_label.config(text=f"{celsius_value} Celsius = {result:.2f} Fahrenheit")
        elif var.get() == 2:  # Fahrenheit to Celsius
            fahrenheit_value = float(entry.get())
            result = fahrenheit_to_celsius(fahrenheit_value)
            result_label.config(text=f"{fahrenheit_value} Fahrenheit = {result:.2f} Celsius")
        else:
            result_label.config(text="Pilih satuan konversi.")
    except ValueError:
        result_label.config(text="Masukkan angka yang valid.")

# Membuat GUI
root = tk.Tk()
root.title("Konversi Suhu")


# Membuat variabel untuk menyimpan pilihan pengguna
var = tk.IntVar()

# Membuat widget input dan label
entry_label = tk.Label(root, text="Masukkan Suhu:")
entry_label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

# Membuat radiobutton untuk memilih jenis konversi
c_to_f_button = tk.Radiobutton(root, text="Celsius ke Fahrenheit", variable=var, value=1)
c_to_f_button.pack()
f_to_c_button = tk.Radiobutton(root, text="Fahrenheit ke Celsius", variable=var, value=2)
f_to_c_button.pack()

# Membuat tombol konversi
convert_button = tk.Button(root, text="Konversi", command=convert)
convert_button.pack(pady=10)

# Membuat label untuk menampilkan hasil konversi
result_label = tk.Label(root, text="")
result_label.pack()

# Menjalankan aplikasi
root.mainloop()
