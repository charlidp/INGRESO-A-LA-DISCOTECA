

# Paso 1: Solicitar al usuario que ingrese la edad del cliente.

edad= int(input("Por favor ingrese la edad del cliente: "))

# Paso 2: Verificar si la edad ingresada cumple con el requisito para ingresar a la Disco.

Permitido = True if edad >= 18 else False

# Paso 3: Mostrar al usuario si su cliente está apto para ingresar.

if Permitido:
    print("Podés ingresar tranquilo")
else:
    print("No podés ingresar")