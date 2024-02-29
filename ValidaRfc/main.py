import re
import pygraphviz as pgv
import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()

def validar_rfc(rfc):
    # Expresión regular para validar RFC de longitud 1 a 4
    patron_rfc = re.compile(r'^[a-zA-Z]{1,4}$')
    return bool(patron_rfc.match(rfc))

# ...

def generar_automata(cadena):
    automata = pgv.AGraph(directed=True, rankdir='LR')

    # Estado inicial "q0"
    automata.add_node("q0", shape="circle", color="red", style="bold")

    # Estado intermedio "M"
    automata.add_node("M", shape="circle", color="red", style="bold")
    automata.add_edge("q0", "M", label="M")

    # Expresión regular
    automata.add_node("regex", shape="rectangle", label="Regex", color="green", style="dashed")
    automata.add_edge("M", "regex", label="^[a-zA-Z]{1,4}")

    # Estados intermedios
    for i in range(len(cadena)):
        estado_actual = f"q{i}"
        estado_siguiente = f"q{i+1}"
        automata.add_node(estado_siguiente, shape="circle", color="red", style="bold")
        automata.add_edge(estado_actual, estado_siguiente, label=cadena[i])

    # Estado final
    automata.add_node(f"q{len(cadena)}", shape="doublecircle", color="blue", style="bold")

    return automata


    return automata

def mostrar_automata(automata, ruta_imagen):
    automata.draw(ruta_imagen, format="png", prog="dot")

def mostrar_resultado(rfc):
    if validar_rfc(rfc):
        automata = generar_automata(rfc)
        ruta_imagen = "./automata_rfc.png"
        mostrar_automata(automata, ruta_imagen)
        if automata:
            print("Imagen generada")
            mostrar_imagen(ruta_imagen)
    else:
        print("Cadena no válida. Intente nuevamente.")

def mostrar_imagen(ruta_imagen):
    img = PhotoImage(file=ruta_imagen)
    label = tk.Label(root, image=img)
    label.image = img  # Conservar una referencia a la imagen
    label.pack()

def interfaz():
    root.title("Validador de RFC")

    label_rfc = tk.Label(root, text="Ingrese las letras de su RFC:")
    label_rfc.pack()

    entry_rfc = tk.Entry(root)
    entry_rfc.pack()

    button_validar = tk.Button(root, text="Validar RFC", command=lambda: mostrar_resultado(entry_rfc.get().upper()))
    button_validar.pack()

    root.mainloop()

if __name__ == "__main__":
    interfaz()


