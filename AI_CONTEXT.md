# AI Context - CLI Commands

Este proyecto contiene comandos CLI ejecutables desde main.py.

## Comandos

### nuevo

- Descripción: Crea un nuevo archivo YAML con estructura básica
- Entrada: Nombre del archivo
- Salida: Archivo YAML
- Uso típico: iniciar un nuevo proyecto de documentación
- Ejemplo: `python main.py nuevo <nombre_archivo.yaml>`

### generar

- Descripción: Genera un reporte PDF a partir de un archivo YAML
- Entrada: YAML
- Salida: PDF
- Uso típico: generar documentación automática
- Ejemplo: `python main.py generar <nombre_archivo.yaml>`

## Flujo típico

1. Usuario crea YAML utilizando el comando `nuevo` o editando un archivo existente.
2. Se llena el YAML con la información, siguiendo la estructura definida y la documentación que está en el esquema JSON ubicadon en `informes\schema\informe.schema.json`.
3. Usuario ejecuta el comando `generar` para crear un PDF con la información del YAML.

## Notas

- Usa Jinja2 para templates
- Usa Typst para PDF
