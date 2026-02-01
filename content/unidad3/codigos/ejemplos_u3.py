"""
U3: Ejemplos de Generación de Variables Aleatorias
Implementaciones ejecutables para aprendizaje práctico.
"""

import random
import math

def generar_exponencial(lambd):
    """Método de la transformada inversa (3.4.1)"""
    r = random.random()
    return -(1/lambd) * math.log(r)

def generar_normal_box_muller(mu=0, sigma=1):
    """Método de Box-Muller (3.5)"""
    r1 = random.random()
    r2 = random.random()
    z = math.sqrt(-2 * math.log(r1)) * math.cos(2 * math.pi * r2)
    return mu + sigma * z

def generar_triangular(a, b, c):
    """Distribución triangular (3.3)"""
    r = random.random()
    fc = (c - a) / (b - a)
    if r < fc:
        return a + math.sqrt(r * (b - a) * (c - a))
    else:
        return b - math.sqrt((1 - r) * (b - a) * (b - c))

def generar_poisson(lambd):
    """Método de búsqueda secuencial (3.5)"""
    x = 0
    p = math.exp(-lambd)
    f = p
    r = random.random()
    while r > f:
        x += 1
        p = p * lambd / x
        f = f + p
    return x

def generar_erlang(k, lambd):
    """Método de convolución (3.4.2)"""
    producto = 1.0
    for _ in range(k):
        producto *= random.random()
    return -(1/lambd) * math.log(producto)

if __name__ == "__main__":
    print("=== Ejemplos de Generación de Variables Aleatorias ===\n")
    
    print("1. Exponencial (λ=2):")
    for i in range(5):
        print(f"   X{i+1} = {generar_exponencial(2):.4f}")
    
    print("\n2. Normal (μ=100, σ=15):")
    for i in range(5):
        print(f"   X{i+1} = {generar_normal_box_muller(100, 15):.2f}")
    
    print("\n3. Triangular (a=10, b=50, c=30):")
    for i in range(5):
        print(f"   X{i+1} = {generar_triangular(10, 50, 30):.2f}")
    
    print("\n4. Poisson (λ=5):")
    for i in range(5):
        print(f"   X{i+1} = {generar_poisson(5)}")
    
    print("\n5. Erlang-3 (λ=1):")
    for i in range(5):
        print(f"   X{i+1} = {generar_erlang(3, 1):.4f}")
