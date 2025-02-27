import tkinter as tk
from tkinter import messagebox

# Clase que maneja la lógica de las reservas de asientos
class Vuelo:
    def __init__(self):
        # Diccionario que almacena los asientos disponibles para cada clase
        self.asientos = {"Ejecutiva": [[None] * 4 for _ in range(2)], "Economica": [[None] * 6 for _ in range(7)]}
        self.reservas = []

    # Método para reservar un asiento
    def reservar_asiento(self, nombre, identificacion, clase, fila, columna):
        if self.asientos[clase][fila][columna] is None:
            self.asientos[clase][fila][columna] = (nombre, identificacion)
            self.reservas.append({"nombre": nombre, "id": identificacion, "clase": clase, "fila": fila, "columna": columna})
            return True
        return False
    
    # Método para cancelar una reserva
    def cancelar_reserva(self, clase, fila, columna):
        self.asientos[clase][fila][columna] = None
        self.reservas = [r for r in self.reservas if not (r["clase"] == clase and r["fila"] == fila and r["columna"] == columna)]
    
    # Obtiene la lista de reservas en formato de texto
    def obtener_reservas(self):
        return "\n".join([f"Nombre: {r['nombre']}, ID: {r['id']}, Clase: {r['clase']}, Asiento: {r['fila']}-{r['columna']}" for r in self.reservas])

# Clase que maneja la interfaz gráfica
class Interfaz:
    def __init__(self, root, vuelo):
        self.root = root
        self.vuelo = vuelo
        self.clase = "Ejecutiva"
        self.crear_interfaz()
    
    # Validación de entrada para el nombre (solo letras)
    def validar_nombre(self, texto):
        return texto.isalpha() or texto == ""
    
    # Validación de entrada para la identificación (solo números)
    def validar_identificacion(self, texto):
        return texto.isdigit() or texto == ""

    # Crea la interfaz gráfica
    def crear_interfaz(self):
        self.root.title("Sistema de Reservas de Vuelo")
        tk.Label(self.root, text="Nombre:").grid(row=0, column=0)
        self.entry_nombre = tk.Entry(self.root, validate="key", validatecommand=(self.root.register(self.validar_nombre), "%P"))
        self.entry_nombre.grid(row=0, column=1)
        
        tk.Label(self.root, text="Identificación:").grid(row=1, column=0)
        self.entry_id = tk.Entry(self.root, validate="key", validatecommand=(self.root.register(self.validar_identificacion), "%P"))
        self.entry_id.grid(row=1, column=1)
        
        # Botones para seleccionar la clase y ver reservas
        tk.Button(self.root, text="Clase Ejecutiva", command=lambda: self.mostrar_asientos("Ejecutiva")).grid(row=2, column=0)
        tk.Button(self.root, text="Clase Económica", command=lambda: self.mostrar_asientos("Economica")).grid(row=2, column=1)
        tk.Button(self.root, text="Ver Reservas", command=self.mostrar_reservas).grid(row=2, column=2)
        
        self.frame_asientos = tk.Frame(self.root)
        self.frame_asientos.grid(row=3, column=0, columnspan=3, pady=10)
        
        # Leyenda de colores
        self.frame_leyenda = tk.Frame(self.root)
        self.frame_leyenda.grid(row=4, column=0, columnspan=3, pady=10)
        tk.Label(self.frame_leyenda, text="Rojo: Ventana").grid(row=0, column=0)
        tk.Label(self.frame_leyenda, text="Verde: Pasillo").grid(row=0, column=1)
        tk.Label(self.frame_leyenda, text="Azul: Centro").grid(row=0, column=2)
    
    # Muestra los asientos según la clase seleccionada
    def mostrar_asientos(self, clase):
        self.clase = clase
        for widget in self.frame_asientos.winfo_children():
            widget.destroy()
        
        filas, columnas = (2, 4) if clase == "Ejecutiva" else (7, 6)
        colores = {0: "red", 1: "green", 2: "blue"}  # Ventana, Pasillo, Centro
        
        for i in range(filas):
            for j in range(columnas):
                color = colores[j % 3]
                btn = tk.Button(self.frame_asientos, text=f"{i}-{j}", bg=color, width=8, height=2, command=lambda f=i, c=j: self.reservar(f, c))
                btn.grid(row=i, column=j, padx=5, pady=5)
    
    # Función para realizar una reserva
    def reservar(self, fila, columna):
        nombre = self.entry_nombre.get()
        identificacion = self.entry_id.get()
        
        if not nombre or not identificacion:
            messagebox.showerror("Error", "Debe ingresar nombre e identificación")
            return
        
        if self.vuelo.reservar_asiento(nombre, identificacion, self.clase, fila, columna):
            messagebox.showinfo("Éxito", "Asiento reservado")
            self.mostrar_asientos(self.clase)
        else:
            messagebox.showerror("Error", "Asiento ya ocupado")
    
    # Muestra las reservas realizadas en una ventana emergente
    def mostrar_reservas(self):
        reservas_texto = self.vuelo.obtener_reservas()
        if reservas_texto:
            messagebox.showinfo("Reservas", reservas_texto)
        else:
            messagebox.showinfo("Reservas", "No hay reservas registradas")
    
# Bloque principal para ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    vuelo = Vuelo()
    interfaz = Interfaz(root, vuelo)
    root.mainloop()
