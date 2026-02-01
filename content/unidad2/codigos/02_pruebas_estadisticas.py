"""
Unidad 2 - Ejemplo 2: Pruebas Estadísticas Completas
Chi-cuadrada, Kolmogorov-Smirnov, Corridas
"""

import random
import math

def prueba_chi_cuadrada(numeros, k=10, alpha=0.05):
    """Prueba Chi-cuadrada de uniformidad"""
    n = len(numeros)
    intervalos = [0] * k
    
    for num in numeros:
        intervalo = min(int(num * k), k-1)
        intervalos[intervalo] += 1
    
    esperado = n / k
    chi2 = sum((obs - esperado)**2 / esperado for obs in intervalos)
    
    # Valores críticos aproximados
    criticos = {10: 16.919, 20: 30.144}
    critico = criticos.get(k, 16.919)
    
    print(f"\nPrueba Chi-cuadrada:")
    print(f"  χ² = {chi2:.4f}")
    print(f"  Valor crítico (α={alpha}): {critico}")
    print(f"  Resultado: {'✓ PASA' if chi2 < critico else '✗ FALLA'}")
    
    return chi2 < critico

def prueba_ks(numeros):
    """Prueba Kolmogorov-Smirnov"""
    n = len(numeros)
    numeros_ordenados = sorted(numeros)
    
    D = 0
    for i, x in enumerate(numeros_ordenados):
        F_empirica = (i + 1) / n
        F_teorica = x  # Para uniforme [0,1]
        D = max(D, abs(F_empirica - F_teorica))
    
    D_critico = 1.36 / math.sqrt(n)  # α=0.05
    
    print(f"\nPrueba Kolmogorov-Smirnov:")
    print(f"  D = {D:.4f}")
    print(f"  D crítico: {D_critico:.4f}")
    print(f"  Resultado: {'✓ PASA' if D < D_critico else '✗ FALLA'}")
    
    return D < D_critico

def prueba_corridas(numeros):
    """Prueba de corridas arriba/abajo"""
    n = len(numeros) - 1
    corridas = 1
    
    for i in range(n):
        if (numeros[i+1] > numeros[i]) != (numeros[i] > numeros[i-1] if i > 0 else True):
            corridas += 1
    
    # Valores esperados
    media_esperada = (2*n - 1) / 3
    varianza_esperada = (16*n - 29) / 90
    
    Z = (corridas - media_esperada) / math.sqrt(varianza_esperada)
    
    print(f"\nPrueba de Corridas:")
    print(f"  Corridas observadas: {corridas}")
    print(f"  Corridas esperadas: {media_esperada:.2f}")
    print(f"  Z = {Z:.4f}")
    print(f"  Resultado: {'✓ PASA' if abs(Z) < 1.96 else '✗ FALLA'}")
    
    return abs(Z) < 1.96

if __name__ == "__main__":
    random.seed(42)
    numeros = [random.random() for _ in range(1000)]
    
    print("="*60)
    print("BATERÍA DE PRUEBAS ESTADÍSTICAS")
    print("="*60)
    print(f"\nNúmeros generados: {len(numeros)}")
    
    p1 = prueba_chi_cuadrada(numeros)
    p2 = prueba_ks(numeros)
    p3 = prueba_corridas(numeros)
    
    print(f"\n{'='*60}")
    print(f"RESUMEN: {sum([p1,p2,p3])}/3 pruebas pasadas")
    print("="*60)
