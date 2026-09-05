# Objetivo

Este proyecto genera PDFs a partir de archivos YAML.

## Flujo

### pre requisitos

- Estar en la carpeta raíz del proyecto.
- Iniciar el entorno virtual con `source .venv/bin/activate` (Linux/Mac) o `.venv\Scripts\activate` (Windows).

1. Crear un YAML usando:
   python main.py nuevo 0003_Anexo2_Informe_Actividades<número_informe>

2. Completar el YAML usando:
   - schema.json
   - ejemplos existentes
   - actividades del usuario correspondiente al periodo del informe (consultar con el usuario o revisar el registro correspondiente en la carpeta actividades_periodo).

3. Generar PDF usando:
   python main.py generar <nombre_archivo>

### Reglas importantes

- Nunca inventar información.
- Si un dato no existe en el informe, preguntar al usuario.
- Revisar que los datos del contrato estén creados, estos se encuentran en la carpeta informes\data\datos_contrato\contrato.2026.yaml.
- Utilizar los datos del contrato para completar el YAML, si no existen, preguntar al usuario.
- Preguntar al usuario sobre las actividades principales del contratista si ya no fueron especificadas. Estas actividades, las cuales están en el contrato, deben tenerse encuenta para este y futuros informes.
- Respetar exactamente la estructura del YAML.
- Los campos deben cumplir con el schema.json.
- Mantener fechas en formato DD-MM-YYYY.
- Los resúmenes deben ser técnicos.
- En la tabla de trazabilidad, en la columna de Actividad Contratual, debes poner la actividad contractual que mejor describa la actividad específica desarrollada.
- En la tabla de trazabilidad no tengas encuenta los feats sueltos que no estén asociados a una HU o a un merge request, aunque hayan sido parte de las actividades del periodo.
- En la tabla de trazabilidad debes poner todas las HUs indicadas en el informe.
- En la tabla de trazabilidad, si un item no tiene link de trazabilidad no se debe poner nada en la columna de Trazabilidad.
- Si en la propiedad "anexos"."ubicacion" se indica una ruta, se debe corroborar que la ruta exista y contenga los anexos. Se debe informar al usuario si la ruta no existe o no contiene anexos, para que el usuario pueda corregirlo.

## Relación informe -> campos

Los campos están documentados en schema.json, seguir las indicaciones allí dadas para cada campo o preguntar si hay alguna duda.

## Ejemplo correcto

general:
  numero_informe: 1
  numero_contrato: 18-2026000001
  nombre_contratista: Pepito Perez
  objeto_contrato: Objetivo contrato
  valor_por_pagar: 1000000
  porcentaje_pago_ejecutado: "10%"
  inicio_periodo: 01/01/2026
  fin_periodo: 02/02/2026
  fecha_elaboracion:
    dia: "07"
    mes: "09"
    anio: "2026"
evidencias:

- actividad_contractual: Módulo de pagos PSE - integración
  actividad_especifica_desarrollada: Se implementó la integración del módulo de pagos PSE, permitiendo a los usuarios realizar transacciones de manera segura y eficiente. Se realizaron pruebas unitarias y de integración para garantizar la correcta funcionalidad del sistema.
  trazabilidad: Link taiga
- actividad_contractual: Módulo de pagos PSE - integración
  actividad_especifica_desarrollada: Se implementó la integración del módulo de pagos PSE, permitiendo a los usuarios realizar transacciones de manera segura y eficiente. Se realizaron pruebas unitarias y de integración para garantizar la correcta funcionalidad del sistema.
  trazabilidad: Link taiga
seguridad_social:
  planillas:
  - meses_cotizados: Agosto 2026
    ibc_cotizado: 1000000
    numero_planilla: 123456789
    fecha_pago: 30/08/2026
    valor_pagado: 100000
firmas:
  numero_documento_nit_contratista: 10000000
  nombre_supervisor: Ing. Juan Perez
  cargo_supervisor: Lider de equipo de desarrollo
anexos:
  ubicacion: informes\assets\anexos
