acl = int(input("Ingrese numero de ACL: "))
if acl >= 1 and acl <= 99:
    print("Es un ACL Estandar")
elif acl >= 100 and acl <=199:
    print("Es un ACL Extendida")
else:
    print("Ingrese un numero dentro del rango 1 al 199.")