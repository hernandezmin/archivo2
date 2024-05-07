import mymath

print("Bienvenido al conversor")
print("1. Velocidad, 2. Distancia, 3. Tiempo, 4. Area, 5. Volumen, 6. Perimetro, 7. Gramos a Moles 8. Concentración molar, 9.Porcentaje de rendimiento, 10.Densidad ")
distancia= 0
tiempo=0
velocidad=0
opcion=input("¿Qué tipo de conversión quiere realizar?")

if opcion == "1":
    distancia=float(input("Ingrese distancia"))
    tiempo=float(input("Ingrese tiempo"))
    print('Tu velocidad MRU es: {0}m/s'.format(mymath.velocidad_mru(distancia,tiempo)))

elif opcion == "2":
    velocidad=float(input("Ingrese velocidad"))
    tiempo=float(input("Ingrese tiempo"))
    print('Tu distancia MRU es: {0}metros'.format(mymath.distancia_mru(velocidad,tiempo)))

elif opcion == "3":
    distancia=float(input("Ingrese distancia"))
    velocidad=float(input("Ingrese velocidad"))
    print('Tu tiempo MRU es: {0}segundos'.format(mymath.tiempo_mru(distancia,velocidad)))

elif opcion == "4":
    base=float(input("Ingrese base"))
    altura=float(input("Ingrese altura"))
    print('Tu altura es: {0}metros'.format(mymath.area_mate(base,altura)))

elif opcion == "5":
    longitud=float(input("Ingrese longitud"))
    ancho=float(input("Ingrese ancho"))
    altura=float(input("Ingrese altura"))
    print('Tu volumen es: {0}mts cubicos'.format(mymath.volumen_mate(longitud,ancho,altura)))

elif opcion == "6":
    lado1=float(input("Ingrese lado"))
    lado2=float(input("Ingrese segundo lado"))
    lado3=float(input("Ingrese tercer lado"))
    lado4=float(input("Ingrese cuarto lado")) 
    print('Tu perimetro es: {0}mts cuadrados'.format(mymath.perimetro_mate(lado1,lado2,lado3,lado4)))

elif opcion == "7":
    masa=float(input("Ingrese masa"))
    masamolar=float(input("Ingrese masa Molar"))
    print('Tus Moles son: {0}n'.format(mymath.gramos_moles(masa,masamolar)))

elif opcion == "8":
    molesoluto=float(input("Ingrese Moles de soluto"))
    volumensolucion=float(input("Ingrese  Volumen de la solución"))
    print('Tu Concentración molar  son: {0}M'.format(mymath.concentración_molar(molesoluto,volumensolucion)))

elif opcion == "9":
    masaexperimental=float(input("Ingrese su masa experimental"))
    masateorica=float(input("Ingrese su masa teorica"))
    print('Tu porcentaje de rendimiento es son: {0}%'.format(mymath.concentración_molar(masaexperimental,masateorica)))

elif opcion == "10":
    masa=float(input("Ingrese masa"))
    volumen=float(input("Ingrese  Volumen"))
    print('Tu densidad es: {0}kg'.format(mymath.densidad_quimica(masa,volumen)))


