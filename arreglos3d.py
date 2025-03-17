def temperatura_promedio(ciudades_temperaturas):
    """Esta funcion calcula la tempetura promedio de un conjunto de ciudades.
    Args:
        ciudades_temperaturas (dict): Un diccionario que contiene nombres de ciudades como claves y lista de temperaturas como valores.
    Returns:
        dict:Un diccionario que contiene nombres de ciudades como claves y temperaturas promedio como valores.
    """

    temperaturas_promedio = {}
    for ciudad, temperaturas in ciudades_temperaturas.items():
        if temperaturas: # Verifica que la lista de temperatura no este vacia 
           promedio = sum(temperaturas) / len (temperaturas)
           temperaturas_promedio[ciudad] = promedio
        else:
            temperaturas_promedio[ciudad] = None #si no hay datos asigna none 
    return temperaturas_promedio
# Crea una matriz 3D
# Primera dimensión: Ciudades ["Pillaro", "Ambato", "Patate"]
# Segunda dimensión: Días de la semana ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
# Tercera dimensión: Semanas (3 semanas)

# Creamos un diccionario de ciudades y temperaturas
temperaturas = { 
    "Pillaro": [
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
    "Ambato":[
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
    "Patate":  [
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
  }

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades_temperaturas = {}

for ciudad, semanas in temperaturas.items():
    #Aplanar la lista de temperaturas de todas las semnas
    temperaturas_a_aplanar = [temp ["temp"] for semana in semanas for temp in semana]
    ciudades_temperaturas[ciudad] = temperaturas_a_aplanar #Guardamos la lista de temperaturas 

#Llamamos a la funcion para calcular las temperaturas promedio
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

#Mostrar los resultados
print ("Temperaturas promedio por ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")
