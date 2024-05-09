print("bienvenido a otakusushi")
pikachu_roll=4500
otaku_roll=5000
pulpo_venenoso_roll=5200
anguila_electrica_roll=4800
total_productos=pikachu_roll+otaku_roll+pulpo_venenoso_roll+anguila_electrica_roll
pikachu_roll=int(input("¿cuantos pikachu roll quiere? "))
otaku_roll=int(input("¿cuantos otaku roll quiere? "))
pulpo_venenoso_roll=int(input("¿cuantos pulpo venenoso roll quiere? "))
anguila_electrica_roll=int(input("¿cuantos anguila electrica roll? "))
precio=float(input())
contraseña=input("ingrese contraseña: ")
if contraseña=="soyotaku":
    print("es correcto")
else:
    print("es incorrecto")
descuento=precio*0.10
limpiar_pantalla="cls"
print("********************************")
print(f"total productos {total_productos}")
print("********************************")
print("pikachu roll", pikachu_roll)
print("otaku roll", otaku_roll)
print("pulpo venenoso roll",pulpo_venenoso_roll)
print("anguila electrica roll", anguila_electrica_roll)
print("*********************************")
total=pikachu_roll*4500+otaku_roll*5000+pulpo_venenoso_roll*5200+anguila_electrica_roll*4800
total_final=total-descuento
print(f"el precio final a pagar es de ${total_final}")