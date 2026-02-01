#!/usr/bin/env python3
"""
Generador de Números Pseudoaleatorios
Implementa varios métodos de generación para la materia de Simulación - TecNM
"""

import math
from typing import List, Tuple


class GeneradorPseudoaleatorios:
    """Clase para generar números pseudoaleatorios usando diferentes métodos"""
    
    def __init__(self, semilla: int = 1234):
        """
        Inicializa el generador con una semilla
        
        Args:
            semilla: Valor inicial para la generación
        """
        self.semilla_original = semilla
        self.semilla_actual = semilla
        self.numeros_generados = []
    
    def cuadrados_medios(self, n: int, digitos: int = 4) -> List[float]:
        """
        Método de Cuadrados Medios (Von Neumann)
        
        Args:
            n: Cantidad de números a generar
            digitos: Número de dígitos de la semilla
            
        Returns:
            Lista de números pseudoaleatorios en [0,1]
        """
        numeros = []
        x = self.semilla_actual
        
        for _ in range(n):
            # Elevar al cuadrado
            cuadrado = x ** 2
            
            # Convertir a string y rellenar con ceros
            str_cuadrado = str(cuadrado).zfill(digitos * 2)
            
            # Extraer dígitos del medio
            inicio = (len(str_cuadrado) - digitos) // 2
            x = int(str_cuadrado[inicio:inicio + digitos])
            
            # Normalizar a [0,1]
            r = x / (10 ** digitos)
            numeros.append(r)
        
        self.numeros_generados = numeros
        return numeros
    
    def congruencial_lineal(self, n: int, a: int = 1103515245, 
                           c: int = 12345, m: int = 2**31) -> List[float]:
        """
        Método Congruencial Lineal
        X(n+1) = (a * X(n) + c) mod m
        
        Args:
            n: Cantidad de números a generar
            a: Multiplicador
            c: Incremento
            m: Módulo
            
        Returns:
            Lista de números pseudoaleatorios en [0,1]
        """
        numeros = []
        x = self.semilla_actual
        
        for _ in range(n):
            x = (a * x + c) % m
            r = x / m
            numeros.append(r)
        
        self.semilla_actual = x
        self.numeros_generados = numeros
        return numeros
    
    def congruencial_multiplicativo(self, n: int, a: int = 16807, 
                                   m: int = 2147483647) -> List[float]:
        """
        Método Congruencial Multiplicativo
        X(n+1) = (a * X(n)) mod m
        
        Args:
            n: Cantidad de números a generar
            a: Multiplicador (debe ser raíz primitiva de m)
            m: Módulo (debe ser primo)
            
        Returns:
            Lista de números pseudoaleatorios en [0,1]
        """
        numeros = []
        x = self.semilla_actual
        
        for _ in range(n):
            x = (a * x) % m
            r = x / m
            numeros.append(r)
        
        self.semilla_actual = x
        self.numeros_generados = numeros
        return numeros
    
    def congruencial_mixto(self, n: int, a: int = 1664525, 
                          c: int = 1013904223, m: int = 2**32) -> List[float]:
        """
        Método Congruencial Mixto (parámetros optimizados)
        
        Args:
            n: Cantidad de números a generar
            a: Multiplicador
            c: Incremento
            m: Módulo
            
        Returns:
            Lista de números pseudoaleatorios en [0,1]
        """
        return self.congruencial_lineal(n, a, c, m)
    
    def reiniciar(self):
        """Reinicia el generador a la semilla original"""
        self.semilla_actual = self.semilla_original
        self.numeros_generados = []
    
    def obtener_estadisticas(self) -> dict:
        """
        Calcula estadísticas básicas de los números generados
        
        Returns:
            Diccionario con media, varianza, min y max
        """
        if not self.numeros_generados:
            return {}
        
        n = len(self.numeros_generados)
        media = sum(self.numeros_generados) / n
        varianza = sum((x - media) ** 2 for x in self.numeros_generados) / n
        
        return {
            'cantidad': n,
            'media': media,
            'varianza': varianza,
            'desviacion_estandar': math.sqrt(varianza),
            'minimo': min(self.numeros_generados),
            'maximo': max(self.numeros_generados)
        }


def ejemplo_uso():
    """Ejemplo de uso del generador"""
    print("=" * 60)
    print("GENERADOR DE NÚMEROS PSEUDOALEATORIOS - TecNM")
    print("=" * 60)
    
    # Crear generador
    gen = GeneradorPseudoaleatorios(semilla=5735)
    
    # Método de Cuadrados Medios
    print("\n1. Método de Cuadrados Medios (10 números):")
    numeros = gen.cuadrados_medios(10, digitos=4)
    for i, num in enumerate(numeros, 1):
        print(f"   r{i} = {num:.6f}")
    
    # Reiniciar generador
    gen.reiniciar()
    
    # Método Congruencial Lineal
    print("\n2. Método Congruencial Lineal (10 números):")
    numeros = gen.congruencial_lineal(10)
    for i, num in enumerate(numeros, 1):
        print(f"   r{i} = {num:.6f}")
    
    # Estadísticas
    print("\n3. Estadísticas de los números generados:")
    stats = gen.obtener_estadisticas()
    for clave, valor in stats.items():
        if isinstance(valor, float):
            print(f"   {clave}: {valor:.6f}")
        else:
            print(f"   {clave}: {valor}")
    
    # Reiniciar generador
    gen.reiniciar()
    
    # Método Congruencial Multiplicativo
    print("\n4. Método Congruencial Multiplicativo (10 números):")
    numeros = gen.congruencial_multiplicativo(10)
    for i, num in enumerate(numeros, 1):
        print(f"   r{i} = {num:.6f}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    ejemplo_uso()
