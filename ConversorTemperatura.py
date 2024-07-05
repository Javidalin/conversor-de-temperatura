import tkinter as tk

def show_conversion_interface(conversion_type):
    # Limpiar la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    if conversion_type == "Celsius to Fahrenheit":
        label = tk.Label(root, text="Ingresa la temperatura en Celsius:")
    else:
        label = tk.Label(root, text="Ingresa la temperatura en Fahrenheit:")
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=5)

    result_label = tk.Label(root, text="", fg="blue")
    result_label.pack(pady=10)

    def convert():
        try:
            temp = float(entry.get())
            if conversion_type == "Celsius to Fahrenheit":
                result = (temp * 9/5) + 32
                result_text = f"{temp}°C es igual a {result:.2f}°F"
            else:
                result = (temp - 32) * 5/9
                result_text = f"{temp}°F es igual a {result:.2f}°C"
            result_label.config(text=result_text)
        except ValueError:
            result_label.config(text="Por favor ingresa un número válido.", fg="red")

    convert_button = tk.Button(root, text="Convertir", command=convert)
    convert_button.pack(pady=10)

    back_button = tk.Button(root, text="Volver", command=show_main_interface)
    back_button.pack(pady=5)

def show_main_interface():
    # Limpiar la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Selecciona el tipo de conversión:")
    label.pack(pady=20)

    c_to_f_button = tk.Button(root, text="Celsius a Fahrenheit", command=lambda: show_conversion_interface("Celsius to Fahrenheit"))
    c_to_f_button.pack(pady=10)

    f_to_c_button = tk.Button(root, text="Fahrenheit a Celsius", command=lambda: show_conversion_interface("Fahrenheit to Celsius"))
    f_to_c_button.pack(pady=10)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Conversor de Temperaturas")

show_main_interface()

root.mainloop()
