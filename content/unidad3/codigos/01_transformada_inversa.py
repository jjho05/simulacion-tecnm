"""
Unidad 3 - Ejemplo 1: Método de la Transformada Inversa
Genera variables aleatorias usando F^-1(U)
"""
import random, math

def exponencial_inversa(lambd):
    """Genera exponencial usando transformada inversa"""
    u = random.random()
    return -math.log(1 - u) / lambd

def triangular_inversa(a, b, c):
    """Genera triangular usando transformada inversa"""
    u = random.random()
    F_c = (c - a) / (b - a)
    if u < F_c:
        return a + math.sqrt(u * (b - a) * (c - a))
    else:
        return b - math.sqrt((1 - u) * (b - a) * (b - c))

if __name__ == "__main__":
    random.seed(42)
    print("Método de la Transformada Inversa\n")
    
    # Exponencial
    exp_vals = [exponencial_inversa(2) for _ in range(1000)]
    print(f"Exponencial(λ=2):")
    print(f"  Media teórica: {1/2:.2f}")
    print(f"  Media simulada: {sum(exp_vals)/len(exp_vals):.2f}\n")
    
    # Triangular
    tri_vals = [triangular_inversa(0, 10, 7) for _ in range(1000)]
    print(f"Triangular(0, 10, 7):")
    print(f"  Media teórica: {(0+10+7)/3:.2f}")
    print(f"  Media simulada: {sum(tri_vals)/len(tri_vals):.2f}")
