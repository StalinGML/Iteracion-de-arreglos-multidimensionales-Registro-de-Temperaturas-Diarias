# Iteración de arreglos multidimensionales con bucles anidados
# Tarea desarrollada por Stalin Mendieta

# Aplicación para rastrear temperaturas diarias en diferentes ciudades
# Matriz 3D: Primera[ciudades], Segunda [días de la semana], Tercera[semanas]
# Ejemplo: 3 ciudades, 7 días, 4 semanas
temperaturas = [
    [  # Ciudad 1: Guayaquil
        [  # Semana 1
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 24}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 23}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 23}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 31}
        ]
    ],
    [  # Ciudad 2: Quininde
        [  # Semana 1
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 33}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 30}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 27}
        ]
    ],
    [  # Ciudad 3: Cuenca
        [  # Semana 1
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 23}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 24}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 30}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 24}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
print("------PROMEDIO DE TEMPERATURAS------")
ciudades = ["Ciudad 1 - Guayaquil", "Ciudad 2 - Quininde", "Ciudad 3 - Cuenca"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    # Imprimir el nombre de la ciudad solo una vez
    print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}:")
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"  Semana {semana_idx + 1}: {promedio:.2f}°C")
    print()  # Línea en blanco entre ciudades para mayor legibilidad

# Calcular el promedio de temperaturas para cada ciudad y semana