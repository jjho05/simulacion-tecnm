"""
Unidad 2 - Ejemplo 1: Generador Congruencial Lineal (LCG)
Implementación y pruebas de calidad
"""

class GeneradorLCG:
    """Generador Congruencial Lineal"""
    
    def __init__(self, semilla, a=1103515245, c=12345, m=2**31):
        self.semilla = semilla
        self.a = a
        self.c = c
        self.m = m
        self.actual = semilla
    
    def siguiente(self):
        """Genera el siguiente número pseudoaleatorio"""
        self.actual = (self.a * self.actual + self.c) % self.m
        return self.actual / self.m
    
    def generar_n(self, n):
        """Genera n números"""
        return [self.siguiente() for _ in range(n)]

def prueba_uniformidad_visual(numeros):
    """Prueba visual de uniformidad"""
    import statistics
    
    print("\n" + "="*60)
    print("PRUEBA DE UNIFORMIDAD")
    print("="*60)
    
    # Dividir en 10 intervalos
    intervalos = [0] * 10
    for num in numeros:
        intervalo = min(int(num * 10), 9)
        intervalos[intervalo] += 1
    
    esperado = len(numeros) / 10
    
    print(f"\nNúmeros generados: {len(numeros)}")
    print(f"Frecuencia esperada por intervalo: {esperado:.1f}\n")
    print(f"{'Intervalo':<15} {'Observado':<12} {'Esperado':<12} {'Diferencia'}")
    print("-"*60)
    
    for i, obs in enumerate(intervalos):
        dif = obs - esperado
        print(f"[{i/10:.1f}, {(i+1)/10:.1f}){'':<5} {obs:<12} {esperado:<12.1f} {dif:+.1f}")
    
    # Chi-cuadrada
    chi2 = sum((obs - esperado)**2 / esperado for obs in intervalos)
    print(f"\nEstadístico χ²: {chi2:.4f}")
    print(f"Valor crítico (α=0.05, gl=9): 16.919")
    
    if chi2 < 16.919:
        print("✓ PASA la prueba de uniformidad")
    else:
        print("✗ NO PASA la prueba")

def prueba_independencia_visual(numeros):
    """Prueba visual de independencia (correlación)"""
    print("\n" + "="*60)
    print("PRUEBA DE INDEPENDENCIA (Correlación)")
    print("="*60)
    
    # Calcular correlación entre números consecutivos
    n = len(numeros) - 1
    suma_xy = sum(numeros[i] * numeros[i+1] for i in range(n))
    suma_x = sum(numeros[:-1])
    suma_y = sum(numeros[1:])
    
    correlacion = (n * suma_xy - suma_x * suma_y) / (n * n)
    
    print(f"\nCorrelación entre números consecutivos: {correlacion:.6f}")
    print(f"Esperado para números independientes: ~0.000")
    
    if abs(correlacion) < 0.05:
        print("✓ PASA la prueba de independencia")
    else:
        print("✗ Posible correlación detectada")

if __name__ == "__main__":
    # Crear generador
    gen = GeneradorLCG(semilla=42)
    
    # Generar números
    numeros = gen.generar_n(10000)
    
    print("="*60)
    print("GENERADOR CONGRUENCIAL LINEAL (LCG)")
    print("="*60)
    print(f"\nParámetros:")
    print(f"  a = {gen.a}")
    print(f"  c = {gen.c}")
    print(f"  m = {gen.m}")
    print(f"  semilla = {gen.semilla}")
    
    print(f"\nPrimeros 10 números generados:")
    primeros_10 = gen.generar_n(10)
    for i, num in enumerate(primeros_10, 1):
        print(f"  r{i} = {num:.6f}")
    
    # Pruebas
    prueba_uniformidad_visual(numeros)
    prueba_independencia_visual(numeros)
