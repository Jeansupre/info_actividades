import yaml
import os
import subprocess
from jinja2 import Environment, FileSystemLoader
import shutil

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