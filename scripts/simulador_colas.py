#!/usr/bin/env python3
"""
Simulador de Líneas de Espera (Teoría de Colas)
Implementa simulación de sistemas M/M/1, M/M/c y análisis de resultados
"""

import math
from typing import List, Dict, Tuple
from dataclasses import dataclass
import heapq


@dataclass
class Cliente:
    """Representa un cliente en el sistema"""
    id: int
    tiempo_llegada: float
    tiempo_inicio_servicio: float = 0
    tiempo_fin_servicio: float = 0
    
    @property
    def tiempo_en_cola(self) -> float:
        """Tiempo que esperó en la cola"""
        return self.tiempo_inicio_servicio - self.tiempo_llegada
    
    @property
    def tiempo_en_sistema(self) -> float:
        """Tiempo total en el sistema"""
        return self.tiempo_fin_servicio - self.tiempo_llegada
    
    @property
    def tiempo_servicio(self) -> float:
        """Tiempo de servicio"""
        return self.tiempo_fin_servicio - self.tiempo_inicio_servicio


class SimuladorColas:
    """Simulador de sistemas de colas"""
    
    def __init__(self, semilla: int = 1234):
        """
        Inicializa el simulador
        
        Args:
            semilla: Semilla para el generador de números aleatorios
        """
        self.semilla = semilla
        self.x = semilla
        self.clientes_atendidos: List[Cliente] = []
        self.eventos = []  # Cola de prioridad de eventos
    
    def _uniforme(self) -> float:
        """Genera número uniforme en [0,1]"""
        a, c, m = 1103515245, 12345, 2**31
        self.x = (a * self.x + c) % m
        return self.x / m
    
    def _exponencial(self, lambd: float) -> float:
        """Genera tiempo exponencial"""
        return -math.log(self._uniforme()) / lambd
    
    def simular_mm1(self, lambd: float, mu: float, 
                    tiempo_simulacion: float) -> Dict:
        """
        Simula sistema M/M/1 (1 servidor, llegadas Poisson, servicio exponencial)
        
        Args:
            lambd: Tasa de llegadas (clientes/unidad de tiempo)
            mu: Tasa de servicio (clientes/unidad de tiempo)
            tiempo_simulacion: Tiempo total de simulación
            
        Returns:
            Diccionario con estadísticas del sistema
        """
        # Verificar estabilidad
        rho = lambd / mu
        if rho >= 1:
            return {
                'error': 'Sistema inestable (ρ ≥ 1)',
                'rho': rho
            }
        
        # Inicializar
        tiempo_actual = 0
        tiempo_fin_servicio = float('inf')
        clientes_atendidos = []
        cola = []
        cliente_id = 0
        
        # Generar primer cliente
        tiempo_proxima_llegada = self._exponencial(lambd)
        
        # Estadísticas
        suma_tiempo_cola = 0
        suma_tiempo_sistema = 0
        suma_clientes_cola = 0
        suma_clientes_sistema = 0
        num_muestras = 0
        
        while tiempo_actual < tiempo_simulacion:
            # Determinar próximo evento
            if tiempo_proxima_llegada < tiempo_fin_servicio:
                # Evento: Llegada
                tiempo_actual = tiempo_proxima_llegada
                cliente_id += 1
                cliente = Cliente(id=cliente_id, tiempo_llegada=tiempo_actual)
                
                if tiempo_fin_servicio == float('inf'):
                    # Servidor libre, atender inmediatamente
                    cliente.tiempo_inicio_servicio = tiempo_actual
                    tiempo_servicio = self._exponencial(mu)
                    cliente.tiempo_fin_servicio = tiempo_actual + tiempo_servicio
                    tiempo_fin_servicio = cliente.tiempo_fin_servicio
                else:
                    # Servidor ocupado, agregar a cola
                    cola.append(cliente)
                
                # Generar próxima llegada
                tiempo_proxima_llegada = tiempo_actual + self._exponencial(lambd)
            else:
                # Evento: Fin de servicio
                tiempo_actual = tiempo_fin_servicio
                
                # Registrar cliente atendido
                if hasattr(self, 'cliente_en_servicio'):
                    clientes_atendidos.append(self.cliente_en_servicio)
                    suma_tiempo_cola += self.cliente_en_servicio.tiempo_en_cola
                    suma_tiempo_sistema += self.cliente_en_servicio.tiempo_en_sistema
                
                if cola:
                    # Atender siguiente cliente en cola
                    self.cliente_en_servicio = cola.pop(0)
                    self.cliente_en_servicio.tiempo_inicio_servicio = tiempo_actual
                    tiempo_servicio = self._exponencial(mu)
                    self.cliente_en_servicio.tiempo_fin_servicio = tiempo_actual + tiempo_servicio
                    tiempo_fin_servicio = self.cliente_en_servicio.tiempo_fin_servicio
                else:
                    # No hay clientes, servidor queda libre
                    tiempo_fin_servicio = float('inf')
            
            # Registrar estadísticas
            suma_clientes_cola += len(cola)
            suma_clientes_sistema += len(cola) + (1 if tiempo_fin_servicio != float('inf') else 0)
            num_muestras += 1
        
        # Calcular métricas
        n = len(clientes_atendidos)
        if n == 0:
            return {'error': 'No se atendieron clientes en el tiempo de simulación'}
        
        L_sim = suma_clientes_sistema / num_muestras
        Lq_sim = suma_clientes_cola / num_muestras
        W_sim = suma_tiempo_sistema / n
        Wq_sim = suma_tiempo_cola / n
        
        # Métricas teóricas
        L_teo = rho / (1 - rho)
        Lq_teo = (rho ** 2) / (1 - rho)
        W_teo = 1 / (mu - lambd)
        Wq_teo = rho / (mu - lambd)
        
        return {
            'sistema': 'M/M/1',
            'parametros': {
                'lambda': lambd,
                'mu': mu,
                'rho': rho
            },
            'clientes_atendidos': n,
            'tiempo_simulacion': tiempo_simulacion,
            'metricas_simuladas': {
                'L': L_sim,
                'Lq': Lq_sim,
                'W': W_sim,
                'Wq': Wq_sim
            },
            'metricas_teoricas': {
                'L': L_teo,
                'Lq': Lq_teo,
                'W': W_teo,
                'Wq': Wq_teo
            },
            'errores_porcentuales': {
                'L': abs(L_sim - L_teo) / L_teo * 100,
                'Lq': abs(Lq_sim - Lq_teo) / Lq_teo * 100 if Lq_teo > 0 else 0,
                'W': abs(W_sim - W_teo) / W_teo * 100,
                'Wq': abs(Wq_sim - Wq_teo) / Wq_teo * 100 if Wq_teo > 0 else 0
            }
        }
    
    def calcular_metricas_teoricas_mm1(self, lambd: float, mu: float) -> Dict:
        """
        Calcula métricas teóricas para sistema M/M/1
        
        Args:
            lambd: Tasa de llegadas
            mu: Tasa de servicio
            
        Returns:
            Diccionario con métricas teóricas
        """
        rho = lambd / mu
        
        if rho >= 1:
            return {'error': 'Sistema inestable (ρ ≥ 1)', 'rho': rho}
        
        return {
            'rho': rho,
            'L': rho / (1 - rho),
            'Lq': (rho ** 2) / (1 - rho),
            'W': 1 / (mu - lambd),
            'Wq': rho / (mu - lambd),
            'P0': 1 - rho,
            'utilizacion': rho * 100
        }
    
    def calcular_metricas_teoricas_mmc(self, lambd: float, mu: float, c: int) -> Dict:
        """
        Calcula métricas teóricas para sistema M/M/c
        
        Args:
            lambd: Tasa de llegadas
            mu: Tasa de servicio por servidor
            c: Número de servidores
            
        Returns:
            Diccionario con métricas teóricas
        """
        rho = lambd / (c * mu)
        
        if rho >= 1:
            return {'error': 'Sistema inestable (ρ ≥ 1)', 'rho': rho}
        
        # Calcular P0 (probabilidad de sistema vacío)
        suma = sum((lambd / mu) ** n / math.factorial(n) for n in range(c))
        termino_c = ((lambd / mu) ** c) / (math.factorial(c) * (1 - rho))
        P0 = 1 / (suma + termino_c)
        
        # Calcular Lq (número promedio en cola)
        Lq = P0 * ((lambd / mu) ** c) * rho / (math.factorial(c) * ((1 - rho) ** 2))
        
        # Otras métricas
        L = Lq + lambd / mu
        Wq = Lq / lambd
        W = Wq + 1 / mu
        
        return {
            'servidores': c,
            'rho': rho,
            'P0': P0,
            'L': L,
            'Lq': Lq,
            'W': W,
            'Wq': Wq,
            'utilizacion_por_servidor': rho * 100,
            'utilizacion_total': (lambd / mu) / c * 100
        }


def ejemplo_uso():
    """Ejemplo de uso del simulador de colas"""
    print("=" * 70)
    print("SIMULADOR DE LÍNEAS DE ESPERA (TEORÍA DE COLAS) - TecNM")
    print("=" * 70)
    
    sim = SimuladorColas(semilla=12345)
    
    # Ejemplo 1: Sistema M/M/1 - Banco con 1 cajero
    print("\n" + "=" * 70)
    print("EJEMPLO 1: BANCO CON 1 CAJERO (M/M/1)")
    print("=" * 70)
    
    lambd = 0.8  # 0.8 clientes por minuto
    mu = 1.0     # 1 cliente por minuto
    tiempo_sim = 1000  # 1000 minutos
    
    print(f"\nParámetros:")
    print(f"  Tasa de llegadas (λ): {lambd} clientes/min")
    print(f"  Tasa de servicio (μ): {mu} clientes/min")
    print(f"  Tiempo de simulación: {tiempo_sim} min")
    
    # Métricas teóricas
    print(f"\nMétricas Teóricas:")
    teoricas = sim.calcular_metricas_teoricas_mm1(lambd, mu)
    print(f"  ρ (utilización): {teoricas['rho']:.4f} ({teoricas['utilizacion']:.2f}%)")
    print(f"  L (clientes en sistema): {teoricas['L']:.4f}")
    print(f"  Lq (clientes en cola): {teoricas['Lq']:.4f}")
    print(f"  W (tiempo en sistema): {teoricas['W']:.4f} min")
    print(f"  Wq (tiempo en cola): {teoricas['Wq']:.4f} min")
    print(f"  P0 (prob. sistema vacío): {teoricas['P0']:.4f}")
    
    # Simulación
    print(f"\nResultados de Simulación:")
    resultado = sim.simular_mm1(lambd, mu, tiempo_sim)
    
    if 'error' not in resultado:
        print(f"  Clientes atendidos: {resultado['clientes_atendidos']}")
        print(f"\n  Métricas Simuladas:")
        print(f"    L: {resultado['metricas_simuladas']['L']:.4f}")
        print(f"    Lq: {resultado['metricas_simuladas']['Lq']:.4f}")
        print(f"    W: {resultado['metricas_simuladas']['W']:.4f} min")
        print(f"    Wq: {resultado['metricas_simuladas']['Wq']:.4f} min")
        
        print(f"\n  Errores Porcentuales:")
        print(f"    L: {resultado['errores_porcentuales']['L']:.2f}%")
        print(f"    Lq: {resultado['errores_porcentuales']['Lq']:.2f}%")
        print(f"    W: {resultado['errores_porcentuales']['W']:.2f}%")
        print(f"    Wq: {resultado['errores_porcentuales']['Wq']:.2f}%")
    
    # Ejemplo 2: Sistema M/M/c - Banco con múltiples cajeros
    print("\n" + "=" * 70)
    print("EJEMPLO 2: BANCO CON 3 CAJEROS (M/M/3)")
    print("=" * 70)
    
    lambd = 2.4  # 2.4 clientes por minuto
    mu = 1.0     # 1 cliente por minuto por cajero
    c = 3        # 3 cajeros
    
    print(f"\nParámetros:")
    print(f"  Tasa de llegadas (λ): {lambd} clientes/min")
    print(f"  Tasa de servicio (μ): {mu} clientes/min por cajero")
    print(f"  Número de cajeros (c): {c}")
    
    teoricas_mmc = sim.calcular_metricas_teoricas_mmc(lambd, mu, c)
    
    if 'error' not in teoricas_mmc:
        print(f"\nMétricas Teóricas:")
        print(f"  ρ (utilización por servidor): {teoricas_mmc['rho']:.4f} ({teoricas_mmc['utilizacion_por_servidor']:.2f}%)")
        print(f"  Utilización total: {teoricas_mmc['utilizacion_total']:.2f}%")
        print(f"  P0 (prob. sistema vacío): {teoricas_mmc['P0']:.4f}")
        print(f"  L (clientes en sistema): {teoricas_mmc['L']:.4f}")
        print(f"  Lq (clientes en cola): {teoricas_mmc['Lq']:.4f}")
        print(f"  W (tiempo en sistema): {teoricas_mmc['W']:.4f} min")
        print(f"  Wq (tiempo en cola): {teoricas_mmc['Wq']:.4f} min")
    
    # Comparación de escenarios
    print("\n" + "=" * 70)
    print("COMPARACIÓN: ¿Cuántos cajeros necesitamos?")
    print("=" * 70)
    
    lambd = 2.0
    mu = 1.0
    
    print(f"\nTasa de llegadas: {lambd} clientes/min")
    print(f"Tasa de servicio: {mu} clientes/min por cajero\n")
    print(f"{'Cajeros':<10}{'ρ':<10}{'Lq':<15}{'Wq (min)':<15}{'Factible':<10}")
    print("-" * 70)
    
    for c in range(1, 6):
        metricas = sim.calcular_metricas_teoricas_mmc(lambd, mu, c)
        if 'error' not in metricas:
            factible = "✓" if metricas['Wq'] < 2 else "✗"
            print(f"{c:<10}{metricas['rho']:<10.4f}{metricas['Lq']:<15.4f}"
                  f"{metricas['Wq']:<15.4f}{factible:<10}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    ejemplo_uso()
