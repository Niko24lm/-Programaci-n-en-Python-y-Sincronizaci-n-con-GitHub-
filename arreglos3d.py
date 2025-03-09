# Crea una matriz 3D
# Primera dimensión: Ciudades ["Pillaro", "Ambato", "Patate"]
# Segunda dimensión: Días de la semana ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
# Tercera dimensión: Semanas (3 semanas)

temperaturas = [
    # Ciudad: Pillaro
    [
        # Semana 1
        [
            {"dia": "lunes", "temp": 14},
            {"dia": "martes", "temp": 15},
            {"dia": "miercoles", "temp": 15},
            {"dia": "jueves", "temp": 14},
            {"dia": "viernes", "temp": 16},
            {"dia": "sabado", "temp": 16},
            {"dia": "domingo", "temp": 13}
        ],
        # Semana 2
        [
            {"dia": "lunes", "temp": 15},
            {"dia": "martes", "temp": 13},
            {"dia": "miercoles", "temp": 13},
            {"dia": "jueves", "temp": 14},
            {"dia": "viernes", "temp": 15},
            {"dia": "sabado", "temp": 16},
            {"dia": "domingo", "temp": 14}
        ],
        # Semana 3 
        [
            {"dia": "lunes", "temp": 16},
            {"dia": "martes", "temp": 17},
            {"dia": "miercoles", "temp": 16},
            {"dia": "jueves", "temp": 15},
            {"dia": "viernes", "temp": 18},
            {"dia": "sabado", "temp": 17},
            {"dia": "domingo", "temp": 15}
        ]
    ],
    # Ciudad: Ambato
    [
        # Semana 1
        [
            {"dia": "lunes", "temp": 12},
            {"dia": "martes", "temp": 13},
            {"dia": "miercoles", "temp": 14},
            {"dia": "jueves", "temp": 12},
            {"dia": "viernes", "temp": 15},
            {"dia": "sabado", "temp": 14},
            {"dia": "domingo", "temp": 13}
        ],
        # Semana 2
        [
            {"dia": "lunes", "temp": 13},
            {"dia": "martes", "temp": 12},
            {"dia": "miercoles", "temp": 14},
            {"dia": "jueves", "temp": 13},
            {"dia": "viernes", "temp": 14},
            {"dia": "sabado", "temp": 15},
            {"dia": "domingo", "temp": 12}
        ],
        # Semana 3 
        [
            {"dia": "lunes", "temp": 14},
            {"dia": "martes", "temp": 15},
            {"dia": "miercoles", "temp": 14},
            {"dia": "jueves", "temp": 13},
            {"dia": "viernes", "temp": 16},
            {"dia": "sabado", "temp": 15},
            {"dia": "domingo", "temp": 14}
        ]
    ],
    # Ciudad: Patate
    [
        # Semana 1
        [
            {"dia": "lunes", "temp": 13},
            {"dia": "martes", "temp": 14},
            {"dia": "miercoles", "temp": 15},
            {"dia": "jueves", "temp": 13},
            {"dia": "viernes", "temp": 14},
            {"dia": "sabado", "temp": 15},
            {"dia": "domingo", "temp": 12}
        ],
        # Semana 2
        [
            {"dia": "lunes", "temp": 14},
            {"dia": "martes", "temp": 15},
            {"dia": "miercoles", "temp": 14},
            {"dia": "jueves", "temp": 12},
            {"dia": "viernes", "temp": 13},
            {"dia": "sabado", "temp": 14},
            {"dia": "domingo", "temp": 13}
        ],
        # Semana 3 
        [
            {"dia": "lunes", "temp": 16},
            {"dia": "martes", "temp": 15},
            {"dia": "miercoles", "temp": 16},
            {"dia": "jueves", "temp": 13},
            {"dia": "viernes", "temp": 16},
            {"dia": "sabado", "temp": 15},
            {"dia": "domingo", "temp": 14}
        ]
     ]
   ]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Pillaro", "Ambato", "Patate"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        if len(semana) > 0:  # Verificar que la semana no esté vacía
            promedio = suma_temperaturas / len(semana)
            print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")