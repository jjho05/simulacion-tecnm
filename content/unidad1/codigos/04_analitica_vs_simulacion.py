"""
Unidad 1 - Ejemplo 4: Comparación Simulación vs Solución Analítica
Demuestra cuándo usar simulación vs fórmulas
"""

import random
import math

# Sistema M/M/1
def solucion_analitica_mm1(lambd, mu):
    """Solución analítica para M/M/1"""
    rho = lambd / mu
    
    if rho >= 1:
        return None  # Sistema inestable
    
    L = rho / (1 - rho)
    Lq = rho**2 / (1 - rho)
    W = 1 / (mu - lambd)
    Wq = rho / (mu - lambd)
    
    return {'L': L, 'Lq': Lq, 'W': W, 'Wq': Wq, 'rho': rho}

def simulacion_mm1(lambd, mu, tiempo_sim=1000):
    """Simulación de M/M/1"""
    tiempo = 0
    tiempo_prox_llegada = -math.log(random.random()) / lambd
    tiempo_fin_servicio = float('inf')
    
    cola = []
    servidor_ocupado = False
    tiempos_espera = []
    
    while tiempo < tiempo_sim:
        if tiempo_prox_llegada < tiempo_fin_servicio:
            tiempo = tiempo_prox_llegada
            
            if not servidor_ocupado:
                servidor_ocupado = True
                tiempo_servicio = -math.log(random.random()) / mu
                tiempo_fin_servicio = tiempo + tiempo_servicio
                tiempos_espera.append(0)
            else:
                cola.append(tiempo)
            
            tiempo_prox_llegada = tiempo - math.log(random.random()) / lambd
        else:
            tiempo = tiempo_fin_servicio
            
            if cola:
                tiempo_llegada = cola.pop(0)
                tiempo_espera = tiempo - tiempo_llegada
                tiempos_espera.append(tiempo_espera)
                tiempo_servicio = -math.log(random.random()) / mu
                tiempo_fin_servicio = tiempo + tiempo_servicio
            else:
                servidor_ocupado = False
                tiempo_fin_servicio = float('inf')
    
    if tiempos_espera:
        Wq_sim = sum(tiempos_espera) / len(tiempos_espera)
        return {'Wq': Wq_sim, 'clientes': len(tiempos_espera)}
    return None

def comparar_metodos():
    """Compara solución analítica vs simulación"""
    print("="*70)
    print("COMPARACIÓN: SOLUCIÓN ANALÍTICA vs SIMULACIÓN")
    print("="*70)
    
    lambd, mu = 3, 4
    
    # Solución analítica
    analitica = solucion_analitica_mm1(lambd, mu)
    
    # Simulación (30 réplicas)
    resultados_sim = []
    for _ in range(30):
        sim = simulacion_mm1(lambd, mu, tiempo_sim=1000)
        if sim:
            resultados_sim.append(sim['Wq'])
    
    Wq_sim = sum(resultados_sim) / len(resultados_sim)
    
    print(f"\nParámetros: λ={lambd}, μ={mu}")
    print(f"\n{'Métrica':<20} {'Analítica':<15} {'Simulación':<15} {'Error %'}")
    print("-"*70)
    print(f"{'Wq (tiempo cola)':<20} {analitica['Wq']:<15.4f} {Wq_sim:<15.4f} {abs(Wq_sim-analitica['Wq'])/analitica['Wq']*100:.2f}%")
    
    print(f"\n✓ Solución analítica: Instantánea, exacta")
    print(f"✓ Simulación: Flexible, aproximada")
    print(f"\nConclusión: Para M/M/1 simple, usar fórmulas.")
    print(f"Para sistemas complejos, usar simulación.")

if __name__ == "__main__":
    random.seed(42)
    comparar_metodos()
