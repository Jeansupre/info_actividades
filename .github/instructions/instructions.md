# Objetivo

Este proyecto genera PDFs a partir de archivos YAML.

# Flujo

## pre requisitos
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

# Reglas importantes

- Nunca inventar información.
- Si un dato no existe en el informe, preguntar al usuario.
- Respetar exactamente la estructura del YAML.
- Los campos deben cumplir schema.json.
- Mantener fechas en formato DD-MM-YYYY.
- Los resúmenes deben ser técnicos.
- Los números que acompañan los prefiejos en la columna ID deben ser los mismos que el número de la HU o del merge request correspondiente.

# Relación informe -> campos

Los campos están documentados en schema.json, seguir las indicaciones allí para cada campo o preguntar si hay alguna duda.

# Ejemplo correcto
encabezado:
  numero_informe: 3
  numero_contrato: "18-2026123456"
  nombre_contratista: "Jean Carlo Rodriguez Sanchez"
  inicio_periodo: "06/04/2026"
  fin_periodo: "06/05/2026"
objetivos:
  descripcion: |
    Durante el presente periodo se llevaron a cabo optimizaciones y refactorizaciones en el mecanismo de control del contador de intentos fallidos asociados al proceso de autenticación mediante OTP (One-Time Password). Estas mejoras incluyeron la revisión y ajuste de la lógica de gestión de credenciales, en respuesta a los lineamientos y observaciones surgidas en las reuniones técnicas del equipo.
    
    Adicionalmente, se diseñaron e implementaron nuevos endpoints para Gestión de Credenciales, orientados a la consulta eficiente de entidades preexistentes en el sistema, empleando algoritmos de coincidencia sobre los datos suministrados por el usuario. Para garantizar la confidencialidad y seguridad de la información, se aplicaron técnicas de ofuscación sobre los datos sensibles retornados en las respuestas de dichos endpoints.
    
    Como parte de las medidas de seguridad, se incorporó un mecanismo de bloqueo automático basado en el umbral de intentos fallidos durante la validación de códigos OTP en los flujos de creación de nuevas personas o entidades, mitigando así posibles ataques de fuerza bruta o intentos de acceso no autorizado.
    
    Finalmente, se desarrolló un endpoint especializado para la detección y notificación de posibles desincronizaciones horarias entre el servidor de autenticación y los dispositivos generadores de códigos OTP. Esta funcionalidad permite identificar y gestionar discrepancias temporales que puedan afectar la validez de los códigos dinámicos durante el proceso de inicio de sesión, mejorando la experiencia de usuario y la robustez del sistema de autenticación.
evidencias:
  - id: HU-1474
    tipo: Historia
    requerimiento: Implementación de gestión de credenciales versionada con endpoints, validaciones y vistas frontend Detalles
    estado: En curso
    trazabilidad: https://chaquen.uis.edu.co/project/dgomezs-general-hu-transversales/us/1474
  - id: HU-1496
    tipo: Historia
    requerimiento: Implementación de OTP para recuperación y validación de correo sin dependencia de identificadores internos
    estado: En curso
    trazabilidad: https://chaquen.uis.edu.co/project/dgomezs-general-hu-transversales/us/1496
  - id: HU-1463
    tipo: Historia
    requerimiento: Ajustes en autenticación con código dinámico para tolerancia a desincronización horaria y mejora de experiencia de usuario Detalles
    estado: Done
    trazabilidad: https://chaquen.uis.edu.co/project/dgomezs-general-hu-transversales/us/1463
  - id: HU-1469
    tipo: Historia
    requerimiento: Corrección de bugs backend en cambio de correo y carga de archivos (MDA) en producción
    estado: Done
    trazabilidad: https://chaquen.uis.edu.co/project/dgomezs-general-hu-transversales/us/1469
  - id: TEST-1904
    tipo: Devtest
    requerimiento: Devtest merge request enhance translations for better clarity in user messages
    estado: Done
    trazabilidad: https://gitlab.uis.edu.co/rsi/core/core-frontend/-/merge_requests/1904
  - id: BUG-466
    tipo: Bug
    requerimiento: Corrección de conteo de intentos fallidos en autenticación OTP
    estado: Done
    trazabilidad: https://gitlab.uis.edu.co/rsi/seguridad/seg-backend/-/merge_requests/466
  - id: REF-467
    tipo: Refactor
    requerimiento: Reorganizar la lógica de autenticación para mejorar el flujo de verificación de usuario y manejo de errores
    estado: Done
    trazabilidad: https://gitlab.uis.edu.co/rsi/seguridad/seg-backend/-/merge_requests/467
gestion:
  soportes_incidentes:
    descripcion: |
      Se brindó soporte a los reportes relacionados con el inicio de sesión utilizando códigos dinámicos (OTP).
  deuda_refactorizacion:
    descripcion: |
      Se abordó la reducción de la deuda técnica acumulada en el módulo de autorregistro, realizando tareas de refactorización sobre componentes críticos previamente implementados en la gestión de credenciales. Estas acciones incluyeron la optimización de estructuras de código, la mejora de la mantenibilidad y la alineación con las mejores prácticas de desarrollo seguro y escalable.
  bloqueos:
    descripcion: "Durante el periodo evaluado no se identificaron bloqueos técnicos ni administrativos que afectaran el desarrollo o la entrega de los compromisos establecidos, permitiendo así el avance continuo de las actividades planificadas."
participacion_ceremonias:
  descripcion: |
    Se mantuvo una participación activa y constante en todas las ceremonias ágiles programadas, incluyendo las reuniones diarias (dailies) y sesiones extraordinarias convocadas para la resolución colaborativa de incidencias e imprevistos. Esta dinámica facilitó la comunicación efectiva, la toma de decisiones en tiempo real y el seguimiento oportuno de los objetivos del equipo.
firmas:
  numero_documento_contratista: 1005322413
  firma_contratista: ""
  nombre_supervisor_contrato: "Ing. Danny Felipe Vergel Paba"
anexos: []