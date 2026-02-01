"""
Unidad 3 - Ejemplo 2: Método de Box-Muller
Genera variables normales
"""
import random, math

def box_muller(mu=0, sigma=1):
    """Genera 2 variables N(mu, sigma) usando Box-Muller"""
    u1, u2 = random.random(), random.random()
    z1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    z2 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
    return mu + sigma * z1, mu + sigma * z2

if __name__ == "__main__":
    random.seed(42)
    normales = []
    for _ in range(5000):
        n1, n2 = box_muller(100, 15)
        normales.extend([n1, n2])
    
    print("Método de Box-Muller - Normal(100, 15)")
    print(f"  Media teórica: 100.00")
    print(f"  Media simulada: {sum(normales)/len(normales):.2f}")
    print(f"  Desv.Est. teórica: 15.00")
    print(f"  Desv.Est. simulada: {(sum((x-sum(normales)/len(normales))**2 for x in normales)/len(normales))**0.5:.2f}")
