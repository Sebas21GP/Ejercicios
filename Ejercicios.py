
Texto = input("Ingrese el Texto: ").lower()
print(Texto)
Letra1 = input("Digite la primera Letra: ").lower() 
Letra2 = input("Digite la segunda Letra: ").lower() 
Letra3 = input("Digite la tercera Letra: ").lower()

Lista1=[] 
Lista1.append(Letra1) 
Lista1.append(Letra2)
Lista1.append(Letra3)

contar1=Texto.count(Letra1) 
print(f"total de la tercera letra escogida: ",contar1)

contar2=Texto.count(Letra2)
print(f"total de la segunda letra escogida: ",contar2)

contar3=Texto.count(Letra3)
print(f"total de la tercera letra escogida: ",contar3)


palabra = input("Ingrese su palabra: ").lower()
Lista2=[]
Lista2.append(Texto)
contar4=Texto.count(palabra)
print(f"La cantidad de palabras registradas en el texto son: ",contar4)

print(f"la primera letra del texto es: {Texto[0]} y la ultima letra es: {Texto[-1]}" )





invertir = Texto[::-1] 
print(invertir)
clave= input("Digite su palabra a buscar:").lower()
verficar = clave in Texto
if(verficar==True):
    print(f"la plabra {clave} si existe")
else:
    print(f"la plabra {clave} no existe")