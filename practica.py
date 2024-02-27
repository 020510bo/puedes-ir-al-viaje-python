edad=int(input("inserte aqui su edad:"))
anos_pais=int(input("inserte aqui cuantos anos llevas en el pais:"))
cantidad=int(input("inserte aqui cuantas personas van:"))


if edad <18:
	print("lo sentimos, no puede ir al viaje debido a su edad")
else :
	print("su edad es correspondiente a nuestros requisitos")
if anos_pais<=4:
	print("lo sentimos, no puedes ir al viaje debido a su tiempo en el pais")
else:
	print("su tiempo en el pais es correspondiente a nuestros requisitos")
if cantidad>4:
	print("lo sentimos, no puede ir al viaje debido a la cantidad de personas que van")
else:
	print("la cantidad de personas es correspondiente a nuestros requisitos")