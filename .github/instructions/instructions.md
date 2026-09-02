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
- Respetar exactamente la estructura del YAML.
- Los campos deben cumplir schema.json.
- Mantener fechas en formato DD-MM-YYYY.
- Los resúmenes deben ser técnicos.
- Los números que acompañan los prefiejos, según el tipo de evidencia, en la columna ID deben ser los mismos que el número de la HU o del merge request correspondiente.
- En la tabla de trazabilidad no tengas encuenta los feats sueltos que no estén asociados a una HU o a un merge request, aunque hayan sido parte de las actividades del periodo.
- En la tabla de trazabilidad debes poner todas las HUs indicadas en el informe.
- Si en la propiedad "anexos"."ubicacion" se indica una ruta, se debe corroborar que la ruta exista y contenga los anexos. Se debe informar al usuario si la ruta no existe o no contiene anexos, para que el usuario pueda corregirlo.

## Relación informe -> campos

Los campos están documentados en schema.json, seguir las indicaciones allí para cada campo o preguntar si hay alguna duda.

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
objetivos:
  descripcion: Descripción de los actividades realizadas durante el periodo, incluyendo la implementación de nuevas funcionalidades, corrección de errores y soporte a usuarios. Se detallan las evidencias de trabajo completadas, así como la gestión de incidencias y bloqueos enfrentados.
evidencias:

- id: HU-042
  tipo: Historia
  requerimiento: Módulo de pagos PSE - integración
  actividad_especifica_desarrollada: Se implementó la integración del módulo de pagos PSE, permitiendo a los usuarios realizar transacciones de manera segura y eficiente. Se realizaron pruebas unitarias y de integración para garantizar la correcta funcionalidad del sistema.
  estado: Done
  trazabilidad: Link taiga
- id: BUG-017
  tipo: Bug
  requerimiento: Error en validación de NIT
  actividad_especifica_desarrollada: Se corrigió un error en la validación del NIT que impedía el registro de ciertos usuarios. Se realizaron pruebas para asegurar que la validación funcione correctamente en todos los casos.
  estado: Done
  trazabilidad: Link Gitlab
- id: SOP-004
  tipo: Soporte
  requerimiento: Capacitación equipo financiero
  actividad_especifica_desarrollada: Se brindó capacitación al equipo financiero sobre el uso del nuevo módulo de pagos PSE, incluyendo procedimientos de registro y resolución de problemas comunes.
  estado: Done
  trazabilidad: Link taiga
- id: HU-666
  tipo: Historia
  requerimiento: Rediseño liquidador catedra
  actividad_especifica_desarrollada: Se llevó a cabo el rediseño del liquidador de cátedra, mejorando la interfaz de usuario y optimizando los cálculos de liquidación. Se realizaron pruebas de usuario para validar la experiencia y funcionalidad.
  estado: Done
  trazabilidad: Link taiga
- id: HU-123
  tipo: Historia
  requerimiento: Procesos en definitiva
  actividad_especifica_desarrollada: Se implementaron mejoras en los procesos de actualización de información en la Hoja de Vida, permitiendo a los usuarios realizar cambios de manera más eficiente y con mayor control sobre la información ingresada.
  estado: En curso
  trazabilidad: Link taiga
gestion:
  soportes_incidentes:
    descripcion: Descripción de los incidentes reportados y gestionados durante el periodo, incluyendo detalles sobre la naturaleza del incidente, las acciones tomadas para su resolución y el estado final del mismo. Se destacan los esfuerzos realizados para minimizar el impacto en los usuarios y garantizar la continuidad del servicio.
  deuda_refactorizacion:
    descripcion: Descripción de la deuda técnica identificada durante el periodo, incluyendo áreas del código que requieren refactorización, mejoras en la arquitectura y optimización de procesos. Se detallan las acciones planificadas para abordar esta deuda y mejorar la calidad del software a largo plazo.
  bloqueos:
    descripcion: Descripción de los bloqueos enfrentados durante el periodo, incluyendo problemas técnicos, dependencias externas y limitaciones de recursos. Se detallan las estrategias implementadas para superar estos bloqueos y asegurar la continuidad del desarrollo de las actividades.
participacion_ceremonias:
  descripcion: Descripción de la participación en ceremonias ágiles, incluyendo reuniones de planificación, revisiones de sprint y retrospectivas. Se destacan las contribuciones del equipo en la mejora continua de los procesos y la colaboración efectiva entre los miembros del equipo.
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
  ubicacion: "informes/assets/anexos/informe1"
