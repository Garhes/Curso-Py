import tkinter as tk #importar la librería tkinter para crear la interfaz gráfica tkinter
from tkinter import messagebox #importar la librería messagebox para mostrar mensajes emergentes

# Definición de la estructura del avión
FILAS_EJECUTIVAS = 2
COLUMNAS_EJECUTIVAS = 4
FILAS_ECONOMICAS = 7
COLUMNAS_ECONOMICAS = 6

# Crear la matriz de asientos
asientos = {}
for fila in range(1, FILAS_EJECUTIVAS + 1):
    for col in range(1, COLUMNAS_EJECUTIVAS + 1):
        tipo = 'Ejecutiva'
        ubicacion = 'Ventana' if col in [1, 4] else 'Pasillo'
        asientos[(fila, col)] = {'tipo': tipo, 'ubicacion': ubicacion, 'ocupado': False, 'pasajero': None}

for fila in range(3, 3 + FILAS_ECONOMICAS):
    for col in range(1, COLUMNAS_ECONOMICAS + 1):
        tipo = 'Económica'
        if col in [1, 6]:
            ubicacion = 'Ventana'
        elif col in [2, 5]:
            ubicacion = 'Pasillo'
        else:
            ubicacion = 'Centro'
        asientos[(fila, col)] = {'tipo': tipo, 'ubicacion': ubicacion, 'ocupado': False, 'pasajero': None}

# Función para reservar un asiento
def reservar_asiento():
    nombre = entry_nombre.get()
    cedula = entry_cedula.get()
    preferencia = opcion_ubicacion.get()
    clase = opcion_clase.get()
    
    if not nombre or not cedula:
        messagebox.showerror("Error", "Por favor, ingrese todos los datos del pasajero.")
        return
    
    for (fila, col), asiento in asientos.items():
        if not asiento['ocupado'] and asiento['tipo'] == clase and asiento['ubicacion'] == preferencia:
            asiento['ocupado'] = True
            asiento['pasajero'] = {'nombre': nombre, 'cedula': cedula}
            actualizar_interfaz()
            return
    
    messagebox.showwarning("Aviso", "No hay asientos disponibles según su preferencia.")

# Función para actualizar la interfaz
def actualizar_interfaz():
    for widget in frame_avion.winfo_children():
        widget.destroy()
    
    for (fila, col), asiento in asientos.items():
        color = "red" if asiento['ocupado'] else "green"
        btn = tk.Button(frame_avion, text=f"{fila}-{col}", bg=color, width=5, height=2)
        btn.grid(row=fila, column=col, padx=5, pady=5)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Reserva de vuelos")

frame_datos = tk.Frame(root)
frame_datos.pack()

tk.Label(frame_datos, text="Nombre:").grid(row=0, column=0)
entry_nombre = tk.Entry(frame_datos)
entry_nombre.grid(row=0, column=1)

tk.Label(frame_datos, text="Cédula:").grid(row=1, column=0)
entry_cedula = tk.Entry(frame_datos)
entry_cedula.grid(row=1, column=1)

opcion_clase = tk.StringVar(value="Ejecutiva")
tk.Label(frame_datos, text="Clase:").grid(row=2, column=0)
tk.OptionMenu(frame_datos, opcion_clase, "Ejecutiva", "Económica").grid(row=2, column=1)

opcion_ubicacion = tk.StringVar(value="Ventana")
tk.Label(frame_datos, text="Ubicación:").grid(row=3, column=0)
tk.OptionMenu(frame_datos, opcion_ubicacion, "Ventana", "Pasillo", "Centro").grid(row=3, column=1)

tk.Button(frame_datos, text="Reservar", command=reservar_asiento).grid(row=4, column=0, columnspan=2)

frame_avion = tk.Frame(root)
frame_avion.pack()

actualizar_interfaz()
root.mainloop() #root que es la ventana principal, se mantiene en espera de eventos
#como el click en el boton de reservar, el cierre de la ventana, etc.
#cuando se cierra la ventana, se termina el programa.