import yaml
import os
import subprocess
from jinja2 import Environment, FileSystemLoader
import shutil

import os

def formato_pesos(valor):
    if valor is None or valor == "":
        return ""

    if isinstance(valor, str):
        valor = (
            valor
            .replace("$", "")
            .replace(".", "")
            .replace(",", "")
            .strip()
        )

    valor = int(float(valor))

    return f"{valor:,}".replace(",", ".")

def obtener_imagenes(ruta, output_dir):
    extensiones = (".png", ".jpg", ".jpeg")
    imagenes = []
    print(f"Buscando imágenes en: {ruta}")
    for f in os.listdir(ruta):
        if f.lower().endswith(extensiones):
            try:
                abs_path = os.path.abspath(os.path.join(ruta, f)) ## ruta absoluta de la imagen
                rel_path = os.path.relpath(abs_path, output_dir) ## ruta relativa desde el output_dir
                imagenes.append(rel_path.replace("\\", "/")) 
            except Exception as e:
                print(f"Error al procesar la imagen {f}: {e}")
    return imagenes

def generar_informe(nombre_yaml: str):
    if not shutil.which("typst"):
        raise Exception("❌ Typst no está instalado o no está en el PATH")

    BASE_DIR = os.path.abspath(".")
    FONT_PATH = os.path.join(BASE_DIR, "informes/assets/fuentes")
    TEMPLATES_DIR = os.path.join(BASE_DIR, "informes/templates")
    OUTPUT_DIR = os.path.join(BASE_DIR, "informes/output")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    env.filters["pesos"] = formato_pesos
    template = env.get_template("informe_fco76.typ.j2")

    # Cargar YAML
    with open(f"informes/data/formato_fco76/{nombre_yaml}.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    #Añadir imágenes de anexos al contexto
    anexos = data.get("anexos", {})
    ruta = anexos["ubicacion"]
    if ruta:
        anexos["imagenes"] = obtener_imagenes(ruta, OUTPUT_DIR)

    # Renderizar Typst
    typ_content = template.render(data)

    # Guardar .typ
    typ_path = os.path.join(OUTPUT_DIR, f"{nombre_yaml}.typ")
    with open(typ_path, "w", encoding="utf-8") as f:
        f.write(typ_content)

    # Generar PDF
    subprocess.run([
        "typst",
        "compile",
        "--root",
        BASE_DIR,
        "--font-path",
        FONT_PATH,
        typ_path,
        os.path.join(OUTPUT_DIR, f"{nombre_yaml}.pdf")
    ])

    print("✅ PDF generado con Typst")