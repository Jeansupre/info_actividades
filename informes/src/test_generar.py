import yaml
import os
import subprocess
from jinja2 import Environment, FileSystemLoader
import shutil

import os

def obtener_imagenes(ruta, output_dir):
    extensiones = (".png", ".jpg", ".jpeg")
    imagenes = []
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
    TEMPLATES_DIR = os.path.join(BASE_DIR, "informes/templates")
    OUTPUT_DIR = os.path.join(BASE_DIR, "informes/output")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template("informe.typ.j2")

    # Cargar YAML
    with open(f"informes/data/{nombre_yaml}.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    #Añadir imágenes de anexos al contexto
    anexos = data.get("anexos", [])
    for anexo in anexos:
        ruta = anexo.get("ubicacion")
        if ruta:
            anexo["imagenes"] = obtener_imagenes(ruta, OUTPUT_DIR)

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
        typ_path,
        os.path.join(OUTPUT_DIR, f"{nombre_yaml}.pdf")
    ])

    print("✅ PDF generado con Typst")