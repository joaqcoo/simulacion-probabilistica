import random
import matplotlib.pyplot as plt

def crear_rayeula(n_ulaulas):    
    lista_vacia = [""]
    rayuela = lista_vacia * n_ulaulas
    rayuela[0] = "A"
    rayuela[len(rayuela)-1] = "B"
    return rayuela

def elegir_PPoT():
    resultado = random.randint(1, 3)
    if resultado == 1:
        return "piedra"
    elif resultado == 2:
        return "papel"
    else:
        return "tijera"

def jugar_PPoT(eleccion_A, eleccion_B):
    dic_ppot = {"piedra": "tijera", "tijera": "papel", "papel": "piedra"}
    
    if eleccion_A == eleccion_B:
        return ""

    elif dic_ppot[eleccion_A] == eleccion_B: 
        return "A"
    
    else:
        return "B"
    
def enfrentamiento_PPoT():
    ganador = ""
    while ganador == "":
        ganador = jugar_PPoT(elegir_PPoT(), elegir_PPoT())
    return ganador

def posicion(equipo, rayuela):
    for i in range(len(rayuela)):
        if rayuela[i] == equipo:
            return i
        
def hay_enfrentamiento(rayuela):
    pos_a = posicion("A", rayuela)
    pos_b = posicion("B", rayuela)
    
    if pos_a+1 == pos_b:
        return True
    else: 
        return False

def avanzar(equipo, rayuela):
    if equipo == "A":
        pos_a = posicion("A", rayuela)+1
        rayuela[pos_a] = "A"
        rayuela[pos_a - 1] = ""
    if equipo == "B":
        pos_b = posicion("B", rayuela)-1
        rayuela[pos_b] = "B"
        rayuela[pos_b + 1] = ""
    
    return rayuela

def avanzar_por_turno(turno, rayuela):
    if turno % 2 == 0:
        rayuela_avanzada = avanzar("A", rayuela)
    else:
        rayuela_avanzada = avanzar("B", rayuela)
        
    return rayuela_avanzada

def concluir_enfrentamiento(ganador, rayuela):
    pos_a = posicion("A", rayuela)
    pos_b = posicion("B", rayuela)
    if ganador == "A":
        rayuela[pos_b] = ""
        rayuela[len(rayuela) - 1] = "B"
    else:
        rayuela[pos_a] = ""
        rayuela[0] = "A"
   
    return rayuela
        
def ganador_partida(rayuela):
    pos_a = posicion("A", rayuela)
    pos_b = posicion("B", rayuela)
    if pos_a == len(rayuela)-2:
        return "A"
    elif pos_b == 1:
        return "B"
    else:
        return ""
    
def rayuela_mortal(n_ulaulas):
    rayuela = crear_rayeula(n_ulaulas)
    contador = 0
    while ganador_partida(rayuela) == "":
        avanzar_por_turno(contador, rayuela)
        if hay_enfrentamiento(rayuela):
            concluir_enfrentamiento(enfrentamiento_PPoT(), rayuela)            
        contador += 1
        print(rayuela)
    return contador
    
def primera_pregunta():                                 # 1 #
    resultados = []
    contador = []
    promedios = []
    for i in range(4,20):
        for j in range(10):
            resultados.append(rayuela_mortal(i))
        promedio = sum(resultados) / 10
        promedios.append(promedio)
        contador.append(i)

    x = contador
    y = promedios
    plt.plot(x,y)
    plt.title("Duracion de la partida en funcion del largo de la rayuela")
    plt.xlabel("Largo de la rayuela")
    plt.ylabel("Duracion de la partida")
    

                                      # 2 #
def partida_trucada(prob_piedra):
    resultado = random.random()
    calculo = (1 - resultado) / 2
    if resultado <= prob_piedra:
        return "piedra"
    elif resultado <= prob_piedra + calculo :
        return "papel"
    else:
        return "tijera"
    
def enfrentamiento_PPoT2(prob_piedra):
    ganador = ""
    while ganador == "":
        ganador = jugar_PPoT(partida_trucada(prob_piedra), elegir_PPoT())
    return ganador
    
def rayuela_mortal2(n_ulaulas, prob_piedra):
    rayuela = crear_rayeula(n_ulaulas)
    contador = 0
    while ganador_partida(rayuela) == "":
        avanzar_por_turno(contador, rayuela)
        if hay_enfrentamiento(rayuela):
            concluir_enfrentamiento(enfrentamiento_PPoT2(prob_piedra), rayuela)            
        contador += 1  
    return ganador_partida(rayuela)
        
def simulac2(n_ulaulas, prob_piedra):
    vacio = []
    contador = 0
    contador2 = 0
    while contador <= 100:
        vacio.append(rayuela_mortal2(n_ulaulas, prob_piedra))
        contador += 1
    for i in range(len(vacio)):
        if vacio[i] == "A":
            contador2 += 1
    return contador2/100

def grafico_simulacion(n_ulaulas):
    resultados = []
    contador_probs = []
    for i in range(0,100):
        resultados.append(simulac2(n_ulaulas ,i/100))
        contador_probs.append(i/100)
        

    x = contador_probs
    y = resultados
    plt.plot(x,y)
    plt.title("Probabilidad de que gane A en funcion de la probabilidad de piedra")
    plt.xlabel("Probabilidad de piedra")
    plt.ylabel("Probabilidad de que gane A")
    
    
                          #3#
                          

def avanzar_por_turno2(probA, rayuela):
    A_prob = random.random()
    if A_prob <=  probA:
        rayuela_avanzada = avanzar("A", rayuela)
    else:
        rayuela_avanzada = avanzar("B", rayuela)
            
    return rayuela_avanzada

def rayuela_mortal3(n_ulaulas, probA):
    rayuela = crear_rayeula(n_ulaulas)
    contador = 0
    while ganador_partida(rayuela) == "":
        avanzar_por_turno2(probA, rayuela)
        if hay_enfrentamiento(rayuela):
            concluir_enfrentamiento(enfrentamiento_PPoT(), rayuela)            
        contador += 1  
    return ganador_partida(rayuela)

def simulac3 (n_ulaulas, probA):
    vacio = []
    contador = 0
    contador3 = 0
    while contador <= 100:
        vacio.append(rayuela_mortal3(n_ulaulas, probA))
        contador += 1
    for i in range(len(vacio)):
        if vacio[i] == "A":
            contador3 += 1
    promedio_a = contador3/100

    
    if promedio_a > 1:
        promedio_a = 1
    elif promedio_a < 0:
        promedio_a = 0
    
    return promedio_a
    
def grafico_simulacion2(n_ulaulas):
    resultados_a = []
    resultados_b = []
    contador_probsA = []
    contador_probsB = []
    
    for i in range(0,100):
        res_a = simulac3(n_ulaulas ,i/100)
        res_b = 1 - res_a
        contador_probsA.append(i/100)
        contador_probsB.append(1-(i/100))
        resultados_a.append(res_a)
        resultados_b.append(res_b)
        
    x = contador_probsA
    y = resultados_a
    y2 = resultados_b
    plt.plot(x,y, label="Línea 1: A")
    plt.plot(x,y2, label="Línea 2: B")  
    plt.title("Probabilidad de que ganen en funcion de la probabilidad de que avance A")
    plt.xlabel("Probabilidad de que avance A")
    plt.ylabel("Probabilidad de que gane cada equipo")
    plt.legend()
    
    
    
    
