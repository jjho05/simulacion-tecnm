#!/usr/bin/env python3
"""
Pruebas Estadísticas para Números Pseudoaleatorios
Implementa pruebas de uniformidad, independencia y aleatoriedad
"""

import math
from typing import List, Tuple, Dict
from collections import Counter


class PruebasEstadisticas:
    """Clase para realizar pruebas estadísticas a números pseudoaleatorios"""
    
    # Valores críticos de Chi-cuadrada (α = 0.05)
    CHI_CUADRADA_CRITICOS = {
        1: 3.841, 2: 5.991, 3: 7.815, 4: 9.488, 5: 11.070,
        6: 12.592, 7: 14.067, 8: 15.507, 9: 16.919, 10: 18.307,
        11: 19.675, 12: 21.026, 13: 22.362, 14: 23.685, 15: 24.996,
        16: 26.296, 17: 27.587, 18: 28.869, 19: 30.144, 20: 31.410
    }
    
    # Valores críticos de Kolmogorov-Smirnov (α = 0.05)
    KS_CRITICOS = {
        5: 0.565, 10: 0.409, 15: 0.338, 20: 0.294, 25: 0.264,
        30: 0.242, 35: 0.224, 40: 0.210, 45: 0.198, 50: 0.188,
        100: 0.134, 200: 0.095, 500: 0.061, 1000: 0.043
    }
    
    @staticmethod
    def prueba_chi_cuadrada(numeros: List[float], k: int = 10, 
                           alpha: float = 0.05) -> Dict:
        """
        Prueba Chi-cuadrada para uniformidad
        
        Args:
            numeros: Lista de números en [0,1]
            k: Número de clases/intervalos
            alpha: Nivel de significancia
            
        Returns:
            Diccionario con resultados de la prueba
        """
        n = len(numeros)
        frecuencias_observadas = [0] * k
        frecuencia_esperada = n / k
        
        # Contar frecuencias observadas
        for num in numeros:
            clase = min(int(num * k), k - 1)
            frecuencias_observadas[clase] += 1
        
        # Calcular estadístico Chi-cuadrada
        chi_cuadrado = sum(
            ((obs - frecuencia_esperada) ** 2) / frecuencia_esperada
            for obs in frecuencias_observadas
        )
        
        # Grados de libertad
        gl = k - 1
        
        # Valor crítico
        valor_critico = PruebasEstadisticas.CHI_CUADRADA_CRITICOS.get(gl, None)
        if valor_critico is None and gl > 20:
            # Aproximación para gl > 20
            valor_critico = gl + math.sqrt(2 * gl) * 1.645
        
        # Decisión
        acepta_h0 = chi_cuadrado < valor_critico if valor_critico else None
        
        return {
            'prueba': 'Chi-cuadrada',
            'estadistico': chi_cuadrado,
            'grados_libertad': gl,
            'valor_critico': valor_critico,
            'nivel_significancia': alpha,
            'acepta_h0': acepta_h0,
            'conclusion': 'ACEPTA uniformidad' if acepta_h0 else 'RECHAZA uniformidad',
            'frecuencias_observadas': frecuencias_observadas,
            'frecuencia_esperada': frecuencia_esperada
        }
    
    @staticmethod
    def prueba_kolmogorov_smirnov(numeros: List[float], 
                                 alpha: float = 0.05) -> Dict:
        """
        Prueba de Kolmogorov-Smirnov para uniformidad
        
        Args:
            numeros: Lista de números en [0,1]
            alpha: Nivel de significancia
            
        Returns:
            Diccionario con resultados de la prueba
        """
        n = len(numeros)
        numeros_ordenados = sorted(numeros)
        
        # Calcular D = max|F(x) - S(x)|
        d_max = 0
        for i, x in enumerate(numeros_ordenados):
            # F(x) para distribución uniforme [0,1] es simplemente x
            f_x = x
            # S(x) es la función de distribución empírica
            s_x = (i + 1) / n
            s_x_anterior = i / n
            
            # Calcular diferencias
            d1 = abs(f_x - s_x)
            d2 = abs(f_x - s_x_anterior)
            d_max = max(d_max, d1, d2)
        
        # Valor crítico
        valor_critico = None
        for tam, val in sorted(PruebasEstadisticas.KS_CRITICOS.items()):
            if n <= tam:
                valor_critico = val
                break
        
        if valor_critico is None:
            # Aproximación para n grande
            valor_critico = 1.36 / math.sqrt(n)
        
        # Decisión
        acepta_h0 = d_max < valor_critico
        
        return {
            'prueba': 'Kolmogorov-Smirnov',
            'estadistico_D': d_max,
            'valor_critico': valor_critico,
            'nivel_significancia': alpha,
            'n': n,
            'acepta_h0': acepta_h0,
            'conclusion': 'ACEPTA uniformidad' if acepta_h0 else 'RECHAZA uniformidad'
        }
    
    @staticmethod
    def prueba_corridas_arriba_abajo(numeros: List[float], 
                                     alpha: float = 0.05) -> Dict:
        """
        Prueba de corridas arriba y abajo para independencia
        
        Args:
            numeros: Lista de números en [0,1]
            alpha: Nivel de significancia
            
        Returns:
            Diccionario con resultados de la prueba
        """
        n = len(numeros)
        
        # Contar corridas
        corridas = 1
        for i in range(1, n):
            if (numeros[i] > numeros[i-1]) != (numeros[i-1] > numeros[i-2] if i > 1 else True):
                corridas += 1
        
        # Media y desviación estándar esperadas
        mu_r = (2 * n - 1) / 3
        sigma_r = math.sqrt((16 * n - 29) / 90)
        
        # Estadístico Z
        z = (corridas - mu_r) / sigma_r
        
        # Valor crítico (distribución normal)
        z_critico = 1.96  # Para α = 0.05 (bilateral)
        
        # Decisión
        acepta_h0 = abs(z) < z_critico
        
        return {
            'prueba': 'Corridas Arriba y Abajo',
            'corridas_observadas': corridas,
            'corridas_esperadas': mu_r,
            'desviacion_estandar': sigma_r,
            'estadistico_Z': z,
            'valor_critico': z_critico,
            'nivel_significancia': alpha,
            'acepta_h0': acepta_h0,
            'conclusion': 'ACEPTA independencia' if acepta_h0 else 'RECHAZA independencia'
        }
    
    @staticmethod
    def prueba_poker(numeros: List[float], digitos: int = 3, 
                    alpha: float = 0.05) -> Dict:
        """
        Prueba de Póker para aleatoriedad
        
        Args:
            numeros: Lista de números en [0,1]
            digitos: Número de dígitos a considerar
            alpha: Nivel de significancia
            
        Returns:
            Diccionario con resultados de la prueba
        """
        n = len(numeros)
        
        # Probabilidades teóricas para 3 dígitos
        prob_teoricas = {
            'TD': 0.720,  # Todos diferentes
            '1P': 0.270,  # Un par
            'T': 0.010,   # Tercia
        }
        
        # Contar categorías
        categorias = {'TD': 0, '1P': 0, 'T': 0}
        
        for num in numeros:
            # Extraer dígitos
            num_str = f"{num:.{digitos}f}".replace('.', '')[:digitos]
            contador = Counter(num_str)
            frecuencias = sorted(contador.values(), reverse=True)
            
            if frecuencias[0] == 3:
                categorias['T'] += 1
            elif frecuencias[0] == 2:
                categorias['1P'] += 1
            else:
                categorias['TD'] += 1
        
        # Calcular Chi-cuadrada
        chi_cuadrado = sum(
            ((categorias[cat] - n * prob_teoricas[cat]) ** 2) / (n * prob_teoricas[cat])
            for cat in categorias
        )
        
        # Grados de libertad
        gl = len(categorias) - 1
        valor_critico = PruebasEstadisticas.CHI_CUADRADA_CRITICOS.get(gl, 5.991)
        
        # Decisión
        acepta_h0 = chi_cuadrado < valor_critico
        
        return {
            'prueba': 'Póker',
            'estadistico': chi_cuadrado,
            'grados_libertad': gl,
            'valor_critico': valor_critico,
            'nivel_significancia': alpha,
            'categorias_observadas': categorias,
            'probabilidades_teoricas': prob_teoricas,
            'acepta_h0': acepta_h0,
            'conclusion': 'ACEPTA aleatoriedad' if acepta_h0 else 'RECHAZA aleatoriedad'
        }
    
    @staticmethod
    def ejecutar_todas_pruebas(numeros: List[float]) -> Dict:
        """
        Ejecuta todas las pruebas estadísticas
        
        Args:
            numeros: Lista de números en [0,1]
            
        Returns:
            Diccionario con resultados de todas las pruebas
        """
        return {
            'chi_cuadrada': PruebasEstadisticas.prueba_chi_cuadrada(numeros),
            'kolmogorov_smirnov': PruebasEstadisticas.prueba_kolmogorov_smirnov(numeros),
            'corridas': PruebasEstadisticas.prueba_corridas_arriba_abajo(numeros),
            'poker': PruebasEstadisticas.prueba_poker(numeros)
        }


def ejemplo_uso():
    """Ejemplo de uso de las pruebas estadísticas"""
    print("=" * 70)
    print("PRUEBAS ESTADÍSTICAS PARA NÚMEROS PSEUDOALEATORIOS - TecNM")
    print("=" * 70)
    
    # Generar números de ejemplo (usando congruencial lineal)
    numeros = []
    x = 5735
    a, c, m = 1103515245, 12345, 2**31
    
    for _ in range(100):
        x = (a * x + c) % m
        numeros.append(x / m)
    
    print(f"\nNúmeros generados: {len(numeros)}")
    print(f"Primeros 10: {[f'{n:.6f}' for n in numeros[:10]]}")
    
    # Ejecutar pruebas
    print("\n" + "=" * 70)
    print("RESULTADOS DE LAS PRUEBAS")
    print("=" * 70)
    
    # Chi-cuadrada
    print("\n1. PRUEBA CHI-CUADRADA (Uniformidad)")
    print("-" * 70)
    resultado = PruebasEstadisticas.prueba_chi_cuadrada(numeros)
    print(f"   Estadístico χ²: {resultado['estadistico']:.4f}")
    print(f"   Valor crítico: {resultado['valor_critico']:.4f}")
    print(f"   Grados de libertad: {resultado['grados_libertad']}")
    print(f"   Conclusión: {resultado['conclusion']}")
    
    # Kolmogorov-Smirnov
    print("\n2. PRUEBA KOLMOGOROV-SMIRNOV (Uniformidad)")
    print("-" * 70)
    resultado = PruebasEstadisticas.prueba_kolmogorov_smirnov(numeros)
    print(f"   Estadístico D: {resultado['estadistico_D']:.6f}")
    print(f"   Valor crítico: {resultado['valor_critico']:.6f}")
    print(f"   Conclusión: {resultado['conclusion']}")
    
    # Corridas
    print("\n3. PRUEBA DE CORRIDAS ARRIBA Y ABAJO (Independencia)")
    print("-" * 70)
    resultado = PruebasEstadisticas.prueba_corridas_arriba_abajo(numeros)
    print(f"   Corridas observadas: {resultado['corridas_observadas']}")
    print(f"   Corridas esperadas: {resultado['corridas_esperadas']:.2f}")
    print(f"   Estadístico Z: {resultado['estadistico_Z']:.4f}")
    print(f"   Valor crítico: ±{resultado['valor_critico']}")
    print(f"   Conclusión: {resultado['conclusion']}")
    
    # Póker
    print("\n4. PRUEBA DE PÓKER (Aleatoriedad)")
    print("-" * 70)
    resultado = PruebasEstadisticas.prueba_poker(numeros)
    print(f"   Estadístico χ²: {resultado['estadistico']:.4f}")
    print(f"   Valor crítico: {resultado['valor_critico']:.4f}")
    print(f"   Categorías observadas: {resultado['categorias_observadas']}")
    print(f"   Conclusión: {resultado['conclusion']}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    ejemplo_uso()
