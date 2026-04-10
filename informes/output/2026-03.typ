#import table: cell, header

#set page("us-letter", margin: 2.54cm)
#set text(font: "Arial", size: 11pt)
#set heading(numbering: "1")

#show heading.where(level: 1): it => [
  #text(weight: "bold")[
    Sección #it.numbering: #it.body
  ]
]


#table(
  columns: (4.02cm, 4.06cm, 8.43cm),
  align: horizon,
  header(cell(colspan: 3)[
    #align(center)[
      #text(size: 18pt, weight: "bold")[
        INFORME DE ACTIVIDADES
      ]
      #linebreak()
      #text(weight: "bold")[
        DIVISIÓN DE TECNOLOGÍAS DE LA INFORMACIÓN Y LA COMUNICACIÓN - DTIC
      ]
    ] 
  ]),
  //fila 1
  cell(rowspan: 4)[
    #align(center)[#image("../assets/logo_uis.png")]
  ],
  [*Informe No.*],
  [1],
  
  //fila 2
  [*Contrato No.*],
  [18-2026000001],

  //fila 3
  [*Contratista:*],
  [Pepito Antonio Pérez Ocasio],

  //fila 4
  [*Período:*],
  [01/01/2026 al 02/02/2026],
)

= Objetivos y resultados
#line(length: 100%)

Durante el período reportado se habilitó la actualización autónoma de la información personal en la Hoja de Vida para empleados y profesores de cátedra, incluyendo variables socioeconómicas y demográficas. Esta mejora reduce la dependencia de procesos administrativos manuales y agiliza la disponibilidad de información actualizada para la toma de decisiones institucionales. Adicionalmente, se fortaleció la calidad y confiabilidad de los datos mediante validaciones según su estado y controles de acceso por rol, garantizando integridad en la edición. La solución incorpora una experiencia de usuario clara, con lenguaje incluyente y capacidades como gestión de imagen de perfil, mejorando la usabilidad y trazabilidad del sistema.