# 📄 Generador de Informes de Actividades

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Typst](https://img.shields.io/badge/Typst-Required-orange)
![Status](https://img.shields.io/badge/status-en%20desarrollo-yellow)
![Version](https://img.shields.io/badge/version-1.0.0-green)

Herramienta CLI para generar informes mensuales en PDF a partir de archivos YAML, utilizando plantillas en Typst.

---

## 🚀 Descripción

Esta herramienta permite automatizar la creación de informes de actividades:

* 📥 Entrada: archivo YAML
* 🎨 Plantilla: Typst + Jinja2
* 📄 Salida: PDF listo para firmar

Evita el uso manual de Word y reduce errores en la elaboración de informes.

---

## 🧱 Tecnologías utilizadas

* Python 3
* Typst
* Jinja2
* PyYAML

---

## 📁 Estructura del proyecto

```bash
info_actividades/
│
├── informes/
│   ├── data/          # Archivos YAML
│   ├── templates/     # Plantillas Typst (.typ.j2)
│   ├── output/        # PDFs generados
│   ├── assets/        # Imágenes y anexos
│   └── src/           # Lógica en Python
│
├── main.py            # Punto de entrada CLI
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd info_actividades
```

---

### 2. Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
```

Activar:

* Windows:

```bash
venv\Scripts\activate
```

* Linux / macOS:

```bash
source venv/bin/activate
```

---

### 3. Instalar dependencias

```p
pip install -r requirements.txt
```

---

### 4. Instalar Typst

Instalar Typst según tu sistema:

#### 🪟 Windows

```bash
winget install typst
```

#### 🐧 Linux

```bash
sudo apt install typst
```

#### 🍎 macOS

```bash
brew install typst
```

Verificar instalación:

```bash
typst --version
```

---

## 🧪 Uso

### 📄 Crear un nuevo archivo YAML

```bash
python main.py nuevo <nombre-del-informe>
```

Esto generará:

```bash
informes/data/<nombre-del-informe>.yaml
```

---

### 📄 Generar PDF

```cli
python main.py generar <nombre-del-informe>
```

Salida:

```bash
informes/output/<nombre-del-informe>.pdf
```

---

## 📝 Estructura del YAML

Ejemplo:

```yaml
encabezado:
  numero_informe: 1
  numero_contrato: 18-2026000001
  nombre_contratista: Juan Pérez
  inicio_periodo: 01/01/2026
  fin_periodo: 31/01/2026

evidencias:
  - id: HU-001
    tipo: Historia
    requerimiento: Implementación módulo X
    estado: Done
    trazabilidad: Link

anexos:
  - ubicacion: informes/assets/anexos
```

---

## 🖼️ Manejo de anexos

* Puedes usar:

  * 📁 Carpetas con imágenes
  * 🖼️ Archivos individuales

Ejemplo:

```yaml
anexos:
  - ubicacion: informes/assets/anexos/informe1
```

Las imágenes serán insertadas automáticamente en el PDF.

---

## ⚠️ Requisitos importantes

* Typst debe estar instalado y disponible en el PATH
* Las rutas de imágenes deben existir
* Las imágenes deben estar dentro del proyecto o accesibles desde el root

---

## 🐛 Solución de problemas

### ❌ Typst no reconocido

```bash
typst: command not found
```

👉 Solución:

* Reinstalar Typst
* Reiniciar la terminal
* Verificar PATH

---

### ❌ Error con imágenes

```bash
file not found
```

👉 Verificar:

* Ruta correcta
* Ubicación dentro del proyecto
* Permisos

---

## 🧠 Buenas prácticas

* Usar rutas relativas dentro del proyecto
* Mantener imágenes en `assets/` o `anexos/`
* Validar YAML antes de generar

---

## 👨‍💻 Autor

Jean Carlo Rodriguez Sanchez. Desarrollado como herramienta interna para automatización de informes.

---

## 📄 Licencia

Uso interno / personalizable según necesidad
