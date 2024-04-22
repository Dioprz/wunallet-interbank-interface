# import tkinter as tk
from Wunallet.inicio import Inicio
from Wunallet.capaLogica.baseDatos.deserializador import Deserializador

# from Wunallet.capaLogica.baseDatos.deserializado import deserializar


def main():
    app = Inicio()

    app.mainloop()

    return 0


if __name__ == "__main__":
    Deserializador.deserializarTodo()
    # deserializar()
    main()
