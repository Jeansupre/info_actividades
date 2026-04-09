import yaml
import os
from jinja2 import Environment, FileSystemLoader
import pdfkit

# 1. Configurar rutas
BASE_DIR = os.path.abspath(".")
TEMPLATES_DIR = os.path.join(BASE_DIR, "informes/templates")

# 2. Cargar template
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
template = env.get_template("informe.html")

# 3. Cargar YAML
with open("informes/data/2026-03.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# 4. Renderizar HTML
html_renderizado = template.render(data)

# (Opcional) guardar HTML para debug
with open("informes/output/debug.html", "w", encoding="utf-8") as f:
    f.write(html_renderizado)

# 5. Generar PDF
pdfkit.from_string(html_renderizado, "informes/output/reporte.pdf")

print("✅ PDF generado en informes/output/reporte.pdf")