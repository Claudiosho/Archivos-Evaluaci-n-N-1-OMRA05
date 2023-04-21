rango_acl_estandar = range(1, 100)
rango_acl_extendida = range(100, 1000)
numero_acl = input("Ingrese el número de ACL IPv4: ")
numero_acl = int(numero_acl)

if numero_acl in rango_acl_estandar:
    print("El número de ACL IPv4", numero_acl, "corresponde a una ACL estándar.")

elif numero_acl in rango_acl_extendida:
    print("El número de ACL IPv4", numero_acl, "corresponde a una ACL extendida.")

else:
    print("El número de ACL IPv4", numero_acl, "no corresponde a una lista de acceso.")