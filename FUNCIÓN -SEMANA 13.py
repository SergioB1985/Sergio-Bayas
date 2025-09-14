profundidad = 0   # Inicialización de las variables utilizadas en el programa
fila = 0
prom = 0
def promedio_temp (profundidad, fila):      # Función que calcula el promedio de una ciudad y semana especifica
    suma = 0
    j = 0
    for dia in temperatuta_ciudad[profundidad][fila]:
        suma = suma + dia['temp']
        j = j + 1
    promedio = suma/j
    return promedio

temperatuta_ciudad = [    # Matriz 3D de las Temperaturas
        [
            [#"quito", "semana1",
            {"day": "Lunes", "temp": 78},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 82},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 92}
        ],
        [  #"quito", "semana2",
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 93}
        ],
        [   #"quito", "semana3",
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 91},
            {"day": "Domingo", "temp": 95}
        ],
        [   #"quito", "semana4",
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 91}
        ]
    ],
    [   # Ciudad 2
        [   #"Guayaquil", "semana1",
            {"day": "Lunes", "temp": 62},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 79}
        ],
        [   #"Guayaquil", "semana2",
            {"day": "Lunes", "temp": 63},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 81}
        ],
        [   #"Guayaquil", "semana3",
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 80}
        ],
        [   #"Guayaquil", "semana4",
            {"day1": "Lunes", "temp": 64},
            {"day2": "Martes", "temp": 67},
            {"day3": "Miércoles", "temp": 69},
            {"day4": "Jueves", "temp": 71},
            {"day5": "Viernes", "temp": 74},
            {"day6": "Sábado", "temp": 77},
            {"day7": "Domingo", "temp": 80}
        ]
    ],
    [   # Ciudad 3
        [  # "Cuenca", "semana1",
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 94},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 82}
        ],
        [   #"Cuenca", "semana2",
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 91},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 81}
        ],
        [   #"Cuenca", "semana3",
            {"day": "Lunes", "temp": 91},
            {"day": "Martes", "temp": 93},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 83}
        ],
        [   #"Cuenca", "semana4",
            {"day": "Lunes", "temp": 88},
            {"day": "Martes", "temp": 90},
            {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 89},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 80}
        ]
    ]
]
ciudades = ["Quito", "Guayaquil", "Cuenca"]   # Lista con las Ciudades de la Matriz 3D
semanas = ["Primera", "Segunda", "Tercera", "Cuarta"]      # Lista para las 4 semanas
print("PROGRAMA QUE CALULA EL PROMEDIO POR SEMANA DE LAS CIUDADES DE QUITO GUAYAQUIL Y CUENCA")
profundidad = int(input(print ("Ingrese la ciudad que desea calcular, considerando 0 al 2 respectivamente")))
fila = int(input(print("Por favor escoger la semana a calcular, consideración 0 al 3")))
prom = promedio_temp(profundidad, fila)
print("UNIVERSIDAD ESTATAL AMAZÓNICA")
print("Programa que calcula el promedio de la temperatura")
print(f"El promedio de la temperatura de la ciudad de {ciudades[profundidad]} de la {semanas[fila]} semana es: {prom:.2f}\N{DEGREE SIGN}C")
print("REALIZADOR POR: SERGIO BAYAS")
