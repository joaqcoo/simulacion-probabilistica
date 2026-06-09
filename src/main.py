import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def crear_rayuela(n_ulaulas):    
    # Representación de la rayuela como lista
    rayuela = [""] * n_ulaulas
    rayuela[0] = "A"
    rayuela[-1] = "B"
    return rayuela

def elegir_PPoT():
    # Elección aleatoria uniforme
    return random.choice(["piedra", "papel", "tijera"])

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
    try:
        return rayuela.index(equipo)
    except ValueError:
        return -1
        
def hay_enfrentamiento(rayuela):
    pos_a = posicion("A", rayuela)
    pos_b = posicion("B", rayuela)
    return pos_a + 1 == pos_b

def avanzar(equipo, rayuela):
    pos = posicion(equipo, rayuela)
    if equipo == "A":
        rayuela[pos] = ""
        rayuela[pos + 1] = "A"
    elif equipo == "B":
        rayuela[pos] = ""
        rayuela[pos - 1] = "B"
    return rayuela

def avanzar_por_turno(turno, rayuela):
    if turno % 2 == 0:
        return avanzar("A", rayuela)
    else:
        return avanzar("B", rayuela)

def concluir_enfrentamiento(ganador, rayuela):
    pos_a = posicion("A", rayuela)
    pos_b = posicion("B", rayuela)
    if ganador == "A":
        rayuela[pos_b] = ""
        rayuela[-1] = "B"
    else:
        rayuela[pos_a] = ""
        rayuela[0] = "A"
    return rayuela
        
def ganador_partida(rayuela):
    pos_a = posicion("A", rayuela)
    pos_b = posicion("B", rayuela)
    if pos_a == len(rayuela) - 2:
        return "A"
    elif pos_b == 1:
        return "B"
    else:
        return ""
    
def rayuela_mortal(n_ulaulas, verbose=False):
    rayuela = crear_rayuela(n_ulaulas)
    contador = 0
    while ganador_partida(rayuela) == "":
        avanzar_por_turno(contador, rayuela)
        if hay_enfrentamiento(rayuela):
            concluir_enfrentamiento(enfrentamiento_PPoT(), rayuela)            
        contador += 1
        if verbose:
            print(rayuela)
    return contador

# --- Experimentos ---

def primera_pregunta():
    print("Ejecutando Experimento 1: Duración vs Largo...")
    resultados_dict = {"Largo": [], "Promedio_Duracion": []}
    for i in range(4, 20):
        duraciones = [rayuela_mortal(i) for _ in range(10)]
        resultados_dict["Largo"].append(i)
        resultados_dict["Promedio_Duracion"].append(np.mean(duraciones))
    
    df = pd.DataFrame(resultados_dict)
    plt.plot(df["Largo"], df["Promedio_Duracion"])
    plt.title("Duración de la partida en función del largo de la rayuela")
    plt.xlabel("Largo de la rayuela")
    plt.ylabel("Duración de la partida")
    plt.show()
    return df

def partida_trucada(prob_piedra):
    resultado = random.random()
    calculo = (1 - resultado) / 2
    if resultado <= prob_piedra:
        return "piedra"
    elif resultado <= prob_piedra + calculo:
        return "papel"
    else:
        return "tijera"

def rayuela_mortal2(n_ulaulas, prob_piedra):
    rayuela = crear_rayuela(n_ulaulas)
    contador = 0
    while ganador_partida(rayuela) == "":
        if contador % 2 == 0:
            avanzar("A", rayuela)
        else:
            avanzar("B", rayuela)
        if hay_enfrentamiento(rayuela):
            ganador_duelo = ""
            while ganador_duelo == "":
                ganador_duelo = jugar_PPoT(partida_trucada(prob_piedra), elegir_PPoT())
            concluir_enfrentamiento(ganador_duelo, rayuela)
        contador += 1
    return ganador_partida(rayuela)

def grafico_simulacion(n_ulaulas):
    print("Ejecutando Experimento 2: Estrategia Sesgada...")
    probs = np.linspace(0, 1, 20)
    win_rates = []
    for p in probs:
        wins_a = sum(1 for _ in range(100) if rayuela_mortal2(n_ulaulas, p) == "A")
        win_rates.append(wins_a / 100)
    
    plt.plot(probs, win_rates)
    plt.title("Probabilidad de que gane A en función de la probabilidad de piedra")
    plt.xlabel("Probabilidad de piedra")
    plt.ylabel("Probabilidad de que gane A")
    plt.show()

def rayuela_mortal3(n_ulaulas, probA):
    rayuela = crear_rayuela(n_ulaulas)
    while ganador_partida(rayuela) == "":
        if random.random() <= probA:
            avanzar("A", rayuela)
        else:
            avanzar("B", rayuela)
        if hay_enfrentamiento(rayuela):
            concluir_enfrentamiento(enfrentamiento_PPoT(), rayuela)
    return ganador_partida(rayuela)

def grafico_simulacion2(n_ulaulas):
    print("Ejecutando Experimento 3: Velocidad de Avance...")
    probs_a = np.linspace(0, 1, 20)
    resultados_a = []
    for p in probs_a:
        wins_a = sum(1 for _ in range(100) if rayuela_mortal3(n_ulaulas, p) == "A")
        resultados_a.append(wins_a / 100)
    
    plt.plot(probs_a, resultados_a, label="Equipo A")
    plt.plot(probs_a, [1-r for r in resultados_a], label="Equipo B")
    plt.title("Probabilidad de victoria en función de la velocidad de avance")
    plt.xlabel("Probabilidad de que avance A")
    plt.ylabel("Probabilidad de victoria")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Para ejecutar manualmente los experimentos
    # primera_pregunta()
    # grafico_simulacion(10)
    # grafico_simulacion2(10)
    pass
