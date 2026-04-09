import argparse
import platform
import shutil
import os
import subprocess

TEMPLATE_PATH = "informes/templates/default.yaml"
DATA_FOLDER = "informes/data"

def crear_yaml(nombre: str):
    """
    Crea un nuevo archivo YAML basado en una plantilla. Si el archivo ya existe, muestra un mensaje de error.
    """

    # Asegurar extensión
    if not nombre.endswith(".yaml"):
        nombre += ".yaml"

    destino = os.path.join(DATA_FOLDER, nombre)

    # Validar existencia
    if os.path.exists(destino):
        print(f"❌ El archivo ya existe: {destino}")
        return

    # Crear carpeta si no existe
    os.makedirs(DATA_FOLDER, exist_ok=True)

    # Copiar template
    shutil.copy(TEMPLATE_PATH, destino)

    #Abrir archivo
    abrir_archivo(destino)

    print(f"✅ YAML creado: {destino}")


def abrir_archivo(ruta: str):
    """
    Intenta abrir el archivo con la aplicación predeterminada del sistema.
    Si falla, muestra la ruta para que el usuario lo abra manualmente.
    """
    sistema = platform.system()

    try:
        if sistema == "Windows":
            os.startfile(ruta)

        elif sistema == "Darwin":  # macOS
            subprocess.run(["open", ruta])

        elif sistema == "Linux":
            subprocess.run(["xdg-open", ruta])

        else:
            print(f"⚠️ Sistema no soportado: {sistema}")
            print(f"Archivo creado en: {ruta}")

    except Exception as e:
        print(f"⚠️ No se pudo abrir automáticamente: {e}")
        print(f"📂 Ruta del archivo: {ruta}")

def build_parser() -> argparse.ArgumentParser:
    """Construye el parser de argumentos para la CLI."""
    parser = argparse.ArgumentParser(
        description="Generador de informes de actividades"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Comando nuevo
    nuevo_parser = subparsers.add_parser("nuevo", help="Crear nuevo archivo YAML")
    nuevo_parser.add_argument("nombre", help="Nombre del archivo (ej: 2026-04)")

    return parser

def run():
    """Punto de entrada para la CLI."""
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "nuevo":
        crear_yaml(args.nombre)
    else:
        parser.print_help()