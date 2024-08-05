# Importa la función 'jugar' del módulo 'juego'
from juego import jugar

def main():
    # Llama a la función 'jugar' que se ha importado del módulo 'juego'
    jugar()

# Verifica si este archivo es el principal (el que se está ejecutando directamente)
if __name__ == "__main__":
    # Llama a la función 'main' si el archivo es el principal
    main()
