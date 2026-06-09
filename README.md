# Simulación Probabilística: Rayuela Mortal 🎲

Este repositorio contiene el Trabajo Práctico Final desarrollado para la materia Pensamiento Computacional de la Facultad de Ciencias Exactas y Naturales (UBA). 

El proyecto modela y simula el juego "Rayuela Mortal" para analizar cómo variables aleatorias afectan el resultado de las partidas.

## 📋 Reglas del Modelo
El sistema simula un enfrentamiento con las siguientes condiciones:
* Dos equipos (A y B) inician en extremos opuestos.
* Avanzan casillero por casillero hasta encontrarse.
* Al chocar, el conflicto se resuelve mediante **Piedra, Papel o Tijera**.
* El ganador sigue avanzando; el perdedor vuelve a su punto de partida.
* El juego termina cuando un equipo llega al extremo contrario.

## 🔬 Modelo Matemático
El juego se puede describir como una **Cadena de Markov** con estados absorbentes. 

### Definición de Estados
Sea $L$ el largo del tablero. El estado se define por las posiciones $(x_A, x_B)$:
$$S = \{ (x_A, x_B) \in \mathbb{Z}^2 : 0 \le x_A \le x_B \le L-1 \}$$

### Probabilidades de Transición
En cada turno, la transición depende de la probabilidad de avance $P(adv_A)$:
1. **Movimiento**: 
   - A avanza con $P(adv_A)$
   - B avanza con $1 - P(adv_A)$
2. **Colisión**: Si $x_A + 1 = x_B$, ocurre un duelo de Piedra, Papel o Tijera.
   - Si gana A: $x_B \to L-1$
   - Si gana B: $x_A \to 0$

## 🛠️ Estructura del Proyecto
- `src/main.py`: Lógica principal de simulación y funciones de experimentos.
- `notebooks/Rayuela_Mortal_Analisis.ipynb`: Análisis visual e interactivo de los resultados.
- `assets/`: Gráficos generados y recursos visuales.
- `requirements.txt`: Dependencias necesarias (NumPy, Pandas, Matplotlib).

## 📊 Análisis y Visualizaciones
Se plantean tres hipótesis principales:
1. **Largo del Tablero**: La duración de la partida crece exponencialmente respecto al tamaño $L$.
2. **Estrategia Sesgada**: Modificar la probabilidad de elegir "Piedra" no altera el equilibrio 50/50 si el oponente es aleatorio.
3. **Velocidad de Avance**: Existe una correlación crítica entre la frecuencia de movimiento y la tasa de victoria.

## 👥 Autores
Proyecto desarrollado por:
* Joaquín Bustamante
* Lisa Muñoz
