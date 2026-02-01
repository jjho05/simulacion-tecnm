#!/usr/bin/env python3
"""
Generador de Variables Aleatorias
Implementa métodos para generar variables aleatorias discretas y continuas
"""

import math
from typing import List, Callable


class GeneradorVariablesAleatorias:
    """Clase para generar variables aleatorias usando diferentes distribuciones"""
    
    def __init__(self, generador_uniforme: Callable[[], float] = None):
        """
        Inicializa el generador
        
        Args:
            generador_uniforme: Función que genera números uniformes en [0,1]
                               Si es None, usa un generador congruencial simple
        """
        if generador_uniforme is None:
            self.x = 1234
            self.generador_uniforme = self._uniforme_default
        else:
            self.generador_uniforme = generador_uniforme
    
    def _uniforme_default(self) -> float:
        """Generador uniforme por defecto (congruencial lineal)"""
        a, c, m = 1103515245, 12345, 2**31
        self.x = (a * self.x + c) % m
        return self.x / m
    
    # ========== DISTRIBUCIONES DISCRETAS ==========
    
    def uniforme_discreta(self, a: int, b: int) -> int:
        """
        Genera variable aleatoria uniforme discreta en [a, b]
        
        Args:
            a: Límite inferior
            b: Límite superior
            
        Returns:
            Valor entero en [a, b]
        """
        u = self.generador_uniforme()
        return a + int((b - a + 1) * u)
    
    def bernoulli(self, p: float) -> int:
        """
        Genera variable aleatoria de Bernoulli
        
        Args:
            p: Probabilidad de éxito
            
        Returns:
            1 con probabilidad p, 0 con probabilidad 1-p
        """
        u = self.generador_uniforme()
        return 1 if u <= p else 0
    
    def binomial(self, n: int, p: float) -> int:
        """
        Genera variable aleatoria binomial usando método directo
        
        Args:
            n: Número de ensayos
            p: Probabilidad de éxito
            
        Returns:
            Número de éxitos en n ensayos
        """
        return sum(self.bernoulli(p) for _ in range(n))
    
    def geometrica(self, p: float) -> int:
        """
        Genera variable aleatoria geométrica (número de ensayos hasta el primer éxito)
        
        Args:
            p: Probabilidad de éxito
            
        Returns:
            Número de ensayos hasta el primer éxito
        """
        u = self.generador_uniforme()
        return int(math.log(1 - u) / math.log(1 - p)) + 1
    
    def poisson(self, lambd: float) -> int:
        """
        Genera variable aleatoria de Poisson usando transformada inversa
        
        Args:
            lambd: Parámetro λ (tasa promedio)
            
        Returns:
            Número de eventos
        """
        a = math.exp(-lambd)
        b = 1.0
        i = 0
        
        while b >= a:
            u = self.generador_uniforme()
            b *= u
            i += 1
        
        return i - 1
    
    # ========== DISTRIBUCIONES CONTINUAS ==========
    
    def uniforme_continua(self, a: float, b: float) -> float:
        """
        Genera variable aleatoria uniforme continua en [a, b]
        
        Args:
            a: Límite inferior
            b: Límite superior
            
        Returns:
            Valor en [a, b]
        """
        u = self.generador_uniforme()
        return a + (b - a) * u
    
    def exponencial(self, lambd: float) -> float:
        """
        Genera variable aleatoria exponencial usando transformada inversa
        
        Args:
            lambd: Parámetro λ (tasa)
            
        Returns:
            Tiempo hasta el siguiente evento
        """
        u = self.generador_uniforme()
        return -math.log(u) / lambd
    
    def normal(self, mu: float = 0, sigma: float = 1) -> float:
        """
        Genera variable aleatoria normal usando método Box-Muller
        
        Args:
            mu: Media
            sigma: Desviación estándar
            
        Returns:
            Valor de distribución normal
        """
        u1 = self.generador_uniforme()
        u2 = self.generador_uniforme()
        
        z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        return mu + sigma * z
    
    def normal_par(self, mu: float = 0, sigma: float = 1) -> tuple:
        """
        Genera par de variables normales usando Box-Muller
        
        Args:
            mu: Media
            sigma: Desviación estándar
            
        Returns:
            Tupla con dos valores normales independientes
        """
        u1 = self.generador_uniforme()
        u2 = self.generador_uniforme()
        
        z1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        z2 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
        
        return (mu + sigma * z1, mu + sigma * z2)
    
    def triangular(self, a: float, b: float, c: float) -> float:
        """
        Genera variable aleatoria triangular
        
        Args:
            a: Límite inferior
            b: Límite superior
            c: Moda (valor más probable)
            
        Returns:
            Valor de distribución triangular
        """
        u = self.generador_uniforme()
        
        if u <= (c - a) / (b - a):
            return a + math.sqrt(u * (b - a) * (c - a))
        else:
            return b - math.sqrt((1 - u) * (b - a) * (b - c))
    
    def weibull(self, alpha: float, beta: float) -> float:
        """
        Genera variable aleatoria de Weibull
        
        Args:
            alpha: Parámetro de escala
            beta: Parámetro de forma
            
        Returns:
            Valor de distribución Weibull
        """
        u = self.generador_uniforme()
        return alpha * (-math.log(u)) ** (1 / beta)
    
    def lognormal(self, mu: float, sigma: float) -> float:
        """
        Genera variable aleatoria lognormal
        
        Args:
            mu: Media del logaritmo
            sigma: Desviación estándar del logaritmo
            
        Returns:
            Valor de distribución lognormal
        """
        z = self.normal(0, 1)
        return math.exp(mu + sigma * z)
    
    # ========== MÉTODOS GENERALES ==========
    
    def generar_muestra(self, distribucion: str, n: int, **params) -> List[float]:
        """
        Genera una muestra de n valores de una distribución
        
        Args:
            distribucion: Nombre de la distribución
            n: Tamaño de la muestra
            **params: Parámetros de la distribución
            
        Returns:
            Lista de valores generados
        """
        metodos = {
            'uniforme_discreta': lambda: self.uniforme_discreta(**params),
            'bernoulli': lambda: self.bernoulli(**params),
            'binomial': lambda: self.binomial(**params),
            'geometrica': lambda: self.geometrica(**params),
            'poisson': lambda: self.poisson(**params),
            'uniforme_continua': lambda: self.uniforme_continua(**params),
            'exponencial': lambda: self.exponencial(**params),
            'normal': lambda: self.normal(**params),
            'triangular': lambda: self.triangular(**params),
            'weibull': lambda: self.weibull(**params),
            'lognormal': lambda: self.lognormal(**params)
        }
        
        if distribucion not in metodos:
            raise ValueError(f"Distribución '{distribucion}' no soportada")
        
        return [metodos[distribucion]() for _ in range(n)]


def ejemplo_uso():
    """Ejemplo de uso del generador de variables aleatorias"""
    print("=" * 70)
    print("GENERADOR DE VARIABLES ALEATORIAS - TecNM")
    print("=" * 70)
    
    gen = GeneradorVariablesAleatorias()
    
    # Distribuciones discretas
    print("\n" + "=" * 70)
    print("DISTRIBUCIONES DISCRETAS")
    print("=" * 70)
    
    print("\n1. Uniforme Discreta [1, 6] (dado):")
    dados = [gen.uniforme_discreta(1, 6) for _ in range(10)]
    print(f"   {dados}")
    
    print("\n2. Bernoulli (p=0.7):")
    bernoullis = [gen.bernoulli(0.7) for _ in range(10)]
    print(f"   {bernoullis}")
    
    print("\n3. Binomial (n=10, p=0.5):")
    binomiales = [gen.binomial(10, 0.5) for _ in range(10)]
    print(f"   {binomiales}")
    
    print("\n4. Poisson (λ=3):")
    poissons = [gen.poisson(3) for _ in range(10)]
    print(f"   {poissons}")
    
    print("\n5. Geométrica (p=0.3):")
    geometricas = [gen.geometrica(0.3) for _ in range(10)]
    print(f"   {geometricas}")
    
    # Distribuciones continuas
    print("\n" + "=" * 70)
    print("DISTRIBUCIONES CONTINUAS")
    print("=" * 70)
    
    print("\n6. Uniforme Continua [0, 10]:")
    uniformes = [gen.uniforme_continua(0, 10) for _ in range(5)]
    print(f"   {[f'{x:.4f}' for x in uniformes]}")
    
    print("\n7. Exponencial (λ=0.5):")
    exponenciales = [gen.exponencial(0.5) for _ in range(5)]
    print(f"   {[f'{x:.4f}' for x in exponenciales]}")
    
    print("\n8. Normal (μ=100, σ=15):")
    normales = [gen.normal(100, 15) for _ in range(5)]
    print(f"   {[f'{x:.4f}' for x in normales]}")
    
    print("\n9. Triangular (a=0, b=10, c=7):")
    triangulares = [gen.triangular(0, 10, 7) for _ in range(5)]
    print(f"   {[f'{x:.4f}' for x in triangulares]}")
    
    print("\n10. Weibull (α=2, β=1.5):")
    weibulls = [gen.weibull(2, 1.5) for _ in range(5)]
    print(f"   {[f'{x:.4f}' for x in weibulls]}")
    
    # Ejemplo de aplicación: Simulación de tiempos de llegada
    print("\n" + "=" * 70)
    print("EJEMPLO: Simulación de llegadas a un banco")
    print("=" * 70)
    print("\nTiempo entre llegadas ~ Exponencial(λ=0.2 clientes/min)")
    print("Tiempo de servicio ~ Normal(μ=4 min, σ=1 min)")
    
    tiempos_llegada = [gen.exponencial(0.2) for _ in range(5)]
    tiempos_servicio = [max(0, gen.normal(4, 1)) for _ in range(5)]
    
    print("\nPrimeros 5 clientes:")
    tiempo_acumulado = 0
    for i, (t_llegada, t_servicio) in enumerate(zip(tiempos_llegada, tiempos_servicio), 1):
        tiempo_acumulado += t_llegada
        print(f"   Cliente {i}: Llega en t={tiempo_acumulado:.2f} min, "
              f"Servicio={t_servicio:.2f} min")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    ejemplo_uso()
