"""
U2: Ejemplos Ejecutables de Generación y Monte Carlo
Este archivo contiene implementaciones directas para probar en clase.
"""

import random

def ejemplo_lcg_mixto():
    """Generador manual con parámetros pequeños para seguir la lógica."""
    print("--- 2.1.2 Algoritmo Congruencial Lineal ---")
    x0 = 7  # Semilla
    a = 5   # Multiplicador
    c = 3   # Constante aditiva
    m = 16  # Módulo
    
    print(f"Propiedades: x0={x0}, a={a}, c={c}, m={m}")
    x = x0
    for i in range(1, 11):
        x = (a * x + c) % m
        r = x / m
        print(f"Iteración {i}: X = {x}, r = {r:.4f}")

def estimar_pi_montecarlo(n=10000):
    """Estimación de Pi usando Monte Carlo (2.3.2)"""
    print("\n--- 2.3.2 Estimación de Pi (Monte Carlo) ---")
    dentro = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if (x**2 + y**2) <= 1:
            dentro += 1
    
    pi_aprox = 4 * (dentro / n)
    print(f"Con N={n} puntos, el valor aproximado de Pi es: {pi_aprox}")

if __name__ == "__main__":
    ejemplo_lcg_mixto()
    estimar_pi_montecarlo()
