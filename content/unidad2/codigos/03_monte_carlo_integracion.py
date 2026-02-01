"""
Unidad 2 - Ejemplo 3: Monte Carlo para Integración
Calcula integrales usando simulación
"""
import random, math

def integrar_monte_carlo(f, a, b, n=10000):
    """Integra f(x) de a a b usando Monte Carlo"""
    suma = sum(f(random.uniform(a, b)) for _ in range(n))
    return (b - a) * suma / n

def ejemplo_integracion():
    # Integral de x^2 de 0 a 1 (resultado exacto = 1/3)
    f = lambda x: x**2
    resultado = integrar_monte_carlo(f, 0, 1, 100000)
    exacto = 1/3
    print(f"∫x² dx de 0 a 1:")
    print(f"  Monte Carlo: {resultado:.6f}")
    print(f"  Exacto: {exacto:.6f}")
    print(f"  Error: {abs(resultado-exacto):.6f}")

if __name__ == "__main__":
    random.seed(42)
    ejemplo_integracion()
