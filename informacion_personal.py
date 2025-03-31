# Crear un Diccionario
informacion_personal = {
    "nombre": "Hugo Ramirez",
    "edad": 24,
    "ciudad": "Pillaro",
    "profesion": "Tec.Enfermeria"
}

# Acceder y Modificar Valores
# Acceder al valor asociado con la clave "ciudad"
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual: {ciudad_actual}")

# Modificar la ciudad
informacion_personal["ciudad"] = "Ambato"
print(f"Nueva ciudad: {informacion_personal['ciudad']}")

# Agregar una nueva clave-valor para la "profesion"
informacion_personal["profesion"] = "Enfermero"

# Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    # Agregar la clave "telefono" con un número ficticio
    informacion_personal["telefono"] = "0985903981"

# Eliminar una Clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el Diccionario Final
print("Diccionario final:")
print(informacion_personal)