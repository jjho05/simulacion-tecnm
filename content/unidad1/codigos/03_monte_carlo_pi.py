"""
Unidad 1 - Ejemplo 3: Simulación Monte Carlo - Estimación de Pi
Demuestra el método Monte Carlo básico
"""

import random
import math

def estimar_pi_monte_carlo(num_puntos):
    """
    Estima π usando el método Monte Carlo
    
    Lanza puntos aleatorios en un cuadrado [0,1] x [0,1]
    y cuenta cuántos caen dentro del círculo de radio 1
    """
    puntos_dentro = 0
    
    for _ in range(num_puntos):
        x = random.random()
        y = random.random()
        
        # Verificar si el punto está dentro del círculo
        distancia = math.sqrt(x**2 + y**2)
        if distancia <= 1:
            puntos_dentro += 1
    
    # π ≈ 4 * (puntos_dentro / total_puntos)
    pi_estimado = 4 * puntos_dentro / num_puntos
    return pi_estimado

def convergencia_monte_carlo():
    """Demuestra la convergencia del método Monte Carlo"""
    print("="*60)
    print("MÉTODO MONTE CARLO - ESTIMACIÓN DE π")
    print("="*60)
    
    tamaños = [100, 1000, 10000, 100000, 1000000]
    
    print(f"\n{'Puntos':<12} {'π Estimado':<15} {'Error':<10} {'Error %'}")
    print("-"*60)
    
    for n in tamaños:
        pi_est = estimar_pi_monte_carlo(n)
        error = abs(pi_est - math.pi)
        error_pct = error / math.pi * 100
        
        print(f"{n:<12} {pi_est:<15.6f} {error:<10.6f} {error_pct:.3f}%")
    
    print(f"\nValor real de π: {math.pi:.10f}")

if __name__ == "__main__":
    random.seed(42)
    convergencia_monte_carlo()
