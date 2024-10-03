""""Se importa la libreria tkinter para crear la interfaz de login"""
import tkinter as tk
from tkinter import messagebox
from tkinter import font
import time
import mysql.connector
from vista.votar import Votar
from busqueda_binaria import busqueda_binaria
from config import DB_CONFIG


class SesionManager:
    def __init__(self):
        self.conexion = None
        self.cursor = None

    def __enter__(self):
        self.conexion = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conexion.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()


class Login:
    def __init__(self):
        # Crear la ventana
        self.ventana = tk.Tk()

        # Configurar propiedades de la ventana
        self.ventana.title("Inicio de sesión")
        self.ventana.geometry("300x200")  # Tamaño de la ventana en píxeles

        # Etiqueta y campo de entrada para el DNI
        self.label_easyvote = tk.Label(self.ventana, text="EasyVote")
        # Configurar opciones de formato
        fuente = font.Font(weight="bold", size=16)
        self.label_easyvote.configure(font=fuente)
        self.label_easyvote.pack(pady=15)

        # Etiqueta y campo de entrada para el DNI
        self.label_dni = tk.Label(self.ventana, text="Ingrese su DNI:")
        self.label_dni.pack(pady=10)

        self.entry_dni = tk.Entry(self.ventana)
        self.entry_dni.pack(pady=10)

        # Botón de inicio de sesión
        self.boton_iniciar = tk.Button(
            self.ventana, text="Iniciar sesión", command=self.iniciar_sesion)
        self.boton_iniciar.pack(pady=10)

    # Función para validar el inicio de sesión
    def iniciar_sesion(self):
        dni = self.entry_dni.get()

    with SesionManager() as sesion:
        # Consultar la columna deseada
        consulta = "SELECT dni FROM votantes"
        sesion.cursor.execute(consulta)
        columna = [fila[0] for fila in sesion.cursor]

        start_time = time.perf_counter()
        resultado = busqueda_binaria(columna, dni)
        end_time = time.perf_counter()
        tiempo_transcurrido = end_time - start_time
        print(f"Tiempo transcurrido: {tiempo_transcurrido:.6f} segundos")

        if resultado:
            messagebox.showinfo("Bienvenido", "Inicio de sesión exitoso")
            self.ventana.destroy()
            votar = Votar(dni)
            votar.iniciar_ventana()
        else:
            messagebox.showinfo("Alerta", "El DNI no es válido")

    # Ejecutar el bucle principal de la aplicación
    def iniciar(self):
        self.ventana.mainloop()


# Ejemplo de uso de la clase Login
if __name__ == "__main__":
    login = Login()
    login.iniciar()
