d = {'key1': 'item1', 'key2': 'item2'}
print(d)
# aparece esto{'key1': 'item1', 'key2': 'item2'}

type(d)
# aparece dict
d['key1']  # accedde al eemento que tiene la clave 'key1' aparece 'item1'

# un ejemplo de uso d diccionarios
pepito = {'edad': 20, 'Nombre': 'Pepito',
        'Apellido': 'Perez', 'Estatura': 1.77}
print(pepito)
# aparece {'edad': 20, 'Nombre': 'Pepito', 'Apellido': 'Perez', 'Estatura': 1.77}
print(pepito['Nombre'])
# Observar que esta clave empieza con Mayuscula, Python es case sensitive
print(pepito['Apellido'])

print(pepito['edad'])
print(pepito['Estatura'])

print(
    f"El nombre del páciente es {pepito['Nombre']} {pepito['Apellido']}, tiene {pepito['edad']}, y su estatura es {pepito['Estatura']}")
print(pepito.keys())
#aparece dict_keys([&#39;edad&#39;, &#39;nombre&#39;, &#39;Apellido&#39;, &#39;estatura&#39;])
# Que ocurre si quiero obtener todos los valores del diccionario?
# pepito[:]
#Booleans (Logicos)
# las palabras True y False son palabras restringidas
# valor Verdadero
#True
#True
# valor Falso
#False
#False
v1 = True
v2 = False
print(f"Valor de v1 = {v1} y v2 = {v2}")
#Valor de v1 = True y v2 = False
type(v1) # tipo de dato
#aparece bool