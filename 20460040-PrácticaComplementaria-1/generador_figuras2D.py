#20460040 Lilia Soto Llamas

import math

def main():
    print()
    print("Menú\n1.- Crear figura\n2.- Listar una clasificación de figuras\n3.- Listar todas las figuras\n4.- Mostrar suma de todas las áreas\n5.- Mostrar la suma de todos los perímetros\n6.- Limpiar lista\n0.- Salir")

def menu_figuras ():
    print("Menú figuras\n1.- Cuadrado\n2.- Triángulo\n3.- Círculo")

figuras = []

def area_cuadrado(lado):
    área = float(lado)*float(lado)
    return área

def perimetro_cuadrado(lado):
    perimetro = float(lado)*4
    return perimetro

def crear_cuadrado(lado):
    tipo = "Cuadrado"
    dic_cuadrado = {
                    "Tipo": tipo, 
                    "Área": area_cuadrado(float(lado)), 
                    "Perímetro": perimetro_cuadrado(float(lado))
                    }
    return dic_cuadrado

def area_triangulo(lado_a, lado_b, lado_c):
    sp = (float(lado_a) + float(lado_b) + float(lado_c))/2
    area = (sp*(sp-lado_a)*(sp-lado_b)*(sp-lado_c))**(1/2)
    return area

def perimetro_triangulo(lado_a, lado_b, lado_c):
    perimetro = float(lado_a) + float(lado_b) + float(lado_c)
    return perimetro 

def crear_triangulo(lado_a, lado_b, lado_c):
    if lado_a == lado_b == lado_c:
        tipo = "Triángulo equilátero"
    if ((lado_a == lado_b) and (lado_a != lado_c)) or ((lado_a == lado_c) and (lado_a != lado_b)) or ((lado_c == lado_b) and (lado_c != lado_a)):
        tipo = "Triángulo rectángulo" 
    if lado_a != lado_b and lado_b != lado_c and lado_a != lado_c:
        tipo = "Triángulo escaleno"
    dic_triangulo = {
                     "Tipo": tipo,
                     "Área": area_triangulo(float(lado_a), float(lado_b), float(lado_c)), 
                     "Perímetro": perimetro_triangulo(float(lado_a), float(lado_b), float(lado_c))
                     }      
    return dic_triangulo        

def area_circulo(radio):
    area = (float(radio)**2)*math.pi
    return area

def perimetro_circulo(radio):
    perimetro = (float(radio)*2)*math.pi
    return perimetro

def crear_circulo(radio):
    tipo = "Círculo"
    dic_circulo =  {
                     "Tipo": tipo, 
                     "Área": area_circulo(float(radio)), 
                     "Perímetro": perimetro_circulo(float(radio))
                     } 
    return dic_circulo

def listar_clasificación(clasificación):
    print()
    if clasificación == "Cuadrado":
        for i in figuras:
            if i["Tipo"] == clasificación:
                print (i)
    if clasificación == "Círculo":
        for i in figuras:
            if i["Tipo"] == clasificación:
                print (i)
    if clasificación == "Triángulo":
        tipo_trian = input("¿Qué tipo de triángulo desea ver?\nEscriba \"equilátero\", \"rectángulo\" o \"escaleno\": ")
        if tipo_trian == "equilátero":
            for i in figuras:
                if i["Tipo"] == "Triángulo equilátero":
                    print (i)
        if tipo_trian == "rectángulo":
            for i in figuras:
                if i["Tipo"] == "Triángulo rectángulo":
                    print (i)
        if tipo_trian == "escaleno":
            for i in figuras:
                if i["Tipo"] == "Triángulo escaleno":
                    print (i)
        if ((tipo_trian != "equilátero") and (tipo_trian != "rectángulo") and (tipo_trian != "escaleno")):
            print("ERROR\nAsegúrate de escribir las palabras exactamente como se indica.")            
    if ((clasificación != "Cuadrado") and (clasificación != "Círculo") and (clasificación != "Triángulo")):
        print("ERROR\nAsegúrate de escribir las palabras exactamente como se indica.")   

def imprimir():
    print()
    for i in figuras:
        print(i)

def sumador_areas():
    print()
    suma_area_cua = 0
    suma_area_teq = 0
    suma_area_tre = 0
    suma_area_tes = 0
    suma_area_cir = 0
    for i in figuras:
        if i["Tipo"] == "Cuadrado":
            suma_area_cua +=  i.get("Área")
    for i in figuras:
        if i["Tipo"] == "Triángulo equilátero":
            suma_area_teq +=  i.get("Área")
    for i in figuras:
        if i["Tipo"] == "Triángulo rectángulo":
            suma_area_tre +=  i.get("Área")
    for i in figuras:
        if i["Tipo"] == "Triángulo escaleno":
            suma_area_tes +=  i.get("Área")
    for i in figuras:
        if i["Tipo"] == "Círculo":
            suma_area_cir +=  i.get("Área")
    if suma_area_cua != 0:
        print(f"La suma del área de todos los cuadrados es: {suma_area_cua}")
    if suma_area_teq != 0:
        print(f"La suma del área de todos los triángulos equiláteros es: {suma_area_teq}")
    if suma_area_tre != 0:
        print(f"La suma del área de todos los triángulos rectángulos es: {suma_area_tre}")
    if suma_area_tes != 0:
        print(f"La suma del área de todos los triángulos escalenos es: {suma_area_tes}")
    if suma_area_cir != 0:
        print(f"La suma del área de todos los círculos es: {suma_area_cir}")                

def sumador_perimetros():
    print()
    suma_peri_cua = 0
    suma_peri_teq = 0
    suma_peri_tre = 0
    suma_peri_tes = 0
    suma_peri_cir = 0
    for i in figuras:
        if i["Tipo"] == "Cuadrado":
            suma_peri_cua +=  i.get("Perímetro")
    for i in figuras:
        if i["Tipo"] == "Triángulo equilátero":
            suma_peri_teq +=  i.get("Perímetro")
    for i in figuras:
        if i["Tipo"] == "Triángulo rectángulo":
            suma_peri_tre +=  i.get("Perímetro")
    for i in figuras:
        if i["Tipo"] == "Triángulo escaleno":
            suma_peri_tes +=  i.get("Perímetro")
    for i in figuras:
        if i["Tipo"] == "Círculo":
            suma_peri_cir +=  i.get("Perímetro")
    if suma_peri_cua != 0:
        print(f"La suma del perímetro de todos los cuadrados es: {suma_peri_cua}")
    if suma_peri_teq != 0:
        print(f"La suma del perímetro de todos los triángulos equiláteros es: {suma_peri_teq}")
    if suma_peri_tre != 0:
        print(f"La suma del perímetro de todos los triángulos rectángulos es: {suma_peri_tre}")
    if suma_peri_tes != 0:
        print(f"La suma del perímetro de todos los triángulos escalenos es: {suma_peri_tes}")
    if suma_peri_cir != 0:
        print(f"La suma del perímetro de todos los círculos es: {suma_peri_cir}")    
                                         

op = ""

while op != "0":
    main()
    op=input("Elija una opción del menú: ")
    if op == "1":
        print()
        op_figuras = ""
        menu_figuras()
        op_figuras = input("Elija una opción del menú: ")
        print()
        if op_figuras == "1":
            print("Crear cuadrado")
            lado_cuadrado = input("¿Cuál es la medida del lado?: ")
            print()
            print("Figura creada:")
            print(crear_cuadrado(lado_cuadrado))
            figuras.append(crear_cuadrado(lado_cuadrado))
        if op_figuras == "2":
            print("Crear triángulo")
            lado_1 = input("¿Cuál es la medida del primer lado?: ")
            lado_2 = input("¿Cuál es la medida del segundo lado?: ")
            lado_3 = input("¿Cuál es la medida del tercer lado?: ")
            print()
            print("Figura creada:")
            print(crear_triangulo(lado_1, lado_2, lado_3))
            figuras.append(crear_triangulo(lado_1, lado_2, lado_3))
        if op_figuras == "3":
            print("Crear círculo")
            radio_circulo = input("¿Cuál es el radio del círculo?: ")
            print()
            print("Figura creada:")
            print(crear_circulo(radio_circulo))
            figuras.append(crear_circulo(radio_circulo))
    if op == "2":
        print()
        print("Listar clasificaciones")
        clasificacion_figuras = input ("¿Qué clasificación de figuras desea ver?\nEscriba \"Cuadrado\", \"Triángulo\" o \"Círculo\": ")
        listar_clasificación(clasificacion_figuras)
    if op == "3":
        print()
        print("Todas las figuras que han sido creadas:")
        imprimir()
    if op == "4":
        sumador_areas()
    if op == "5":
        sumador_perimetros()
    if op == "6":
        print()
        figuras.clear()
        print("Se ha limpiado la lista de figuras.")
    if op == "0":
        print()
        print("Ha decidido salir, gracias por utilizar este programa.")
        print()